import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function", params=["chromium", "firefox", "webkit"])
def page(request):
    browser_type = request.param
    with sync_playwright() as p:
        browser = getattr(p, browser_type).launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()


def check_error_messages(contact_modal, completed_fields=None):
    """Helper function to check error messages for required fields."""
    if completed_fields is None:
        completed_fields = []

    required_fields = contact_modal.locator('[required]')
    for i in range(required_fields.count()):
        field = required_fields.nth(i)
        field_name = field.get_attribute("name")

        parent_div = field.locator('xpath=ancestor::div[contains(@class, "hs-form-field")]')
        error_msg_locator = parent_div.locator('.hs-error-msgs .hs-error-msg')

        if field_name in completed_fields:
            assert not error_msg_locator.is_visible(), f"Error message found for field: {field_name}"
        else:
            assert error_msg_locator.is_visible(), f"No error message found for field: {field_name}"
            error_msg_color = error_msg_locator.evaluate('element => window.getComputedStyle(element).color')
            assert error_msg_color == "rgb(255, 0, 0)", f"The error message color is {error_msg_color}, not red."


def test_workflow(page):

    # Step 1: Navigate to the Qubika Website
    url = "https://www.qubika.com"
    page.goto(url)

    # Step 2a: Validate the website URL
    expected_final_url = "https://qubika.com/"

    assert page.url == expected_final_url, (
        f"The current URL '{page.url}' does not match the expected final URL '{expected_final_url}'"
    )

    # Step 2b: Validate the Qubika logo
    logo = page.locator('body > div.overflower > header > div.content > a.logo')
    assert logo.is_visible(), "The logo is not visible"

    # Step 3: Click ‘Contact us’ button
    contact_us_button = page.locator('body > div.overflower > section.hero.active > div.content.text-intro > div > a')
    contact_us_button.click()

    # Step 4: Validate contact form is displayed
    contact_modal = page.locator('body > div.overflower > div.modal.contact-us-modal.show > div')
    contact_modal.wait_for(state="visible")
    assert contact_modal.is_visible(), "The contact modal is not visible"

    # Step 4a: Validate First Name and Last Name fields are displayed
    first_name_field = contact_modal.locator('[name="firstname"]')
    first_name_field.wait_for(state="visible")
    assert first_name_field.is_visible(), "The 'First Name' field is not visible"
    last_name_field = contact_modal.locator('[name="lastname"]')
    assert last_name_field.is_visible(), "The 'Last Name' field is not visible"

    # Step 4b: Validate Email field is displayed
    email_field = contact_modal.locator('[name="email"]')
    assert email_field.is_visible(), "The 'Email' field is not visible"

    # Step 4c: Validate Submit button
    submit_button = contact_modal.locator('#hsForm_5e204c31-ede2-4976-a096-6919a081b2df > div.hs_submit.hs-submit > div.actions > input')
    assert submit_button.is_visible(), "The 'Submit' button is not visible"

    # Step 5: Click Submit button without filling any field
    submit_button.click()

    # Step 6: Validate that all mandatory fields have an error message
    # Step 7: Validate that the error messages are displayed in red
    check_error_messages(contact_modal)

    # Step 8: Write ‘Test name’ on the First Name field
    first_name_field.fill('Test name')

    # Step 9: Click Submit button
    submit_button.click()

    # Step 10: Validate that all mandatory fields have an error message except First Name field
    # Step 11: Validate that the error messages are displayed in red
    completed_fields = ["firstname"]
    check_error_messages(contact_modal, completed_fields)