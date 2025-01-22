# Qubika Website Test Automation

## Overview
This project automates the testing of a workflow on the Qubika website (https://www.qubika.com) using Python and Pytest. The goal is to validate the behavior of the "Contact Us" form, ensuring that required fields display appropriate error messages when left empty and verifying that the form behaves as expected when partially completed.

## Key Features
- Tests are executed on three browser engines: **Chromium**, **Firefox**, and **Webkit**, to ensure compatibility across different browsers.
- A single test function encompasses the entire workflow, reflecting the sequential and dependent nature of the specified steps.
- URL validation includes verifying the redirected URL (`https://qubika.com/`).
- There are two "Contact Us" buttons. The test focuses on one "Contact Us" button for clarity, as both buttons on the website lead to the same modal.
- Adjustments were made to match the actual website's structure and behavior, including validating "First Name" and "Last Name" fields instead of a single "Name" field and testing the "Submit" button instead of a non-existent "Get in touch" button.

## Workflow
1) Navigate to Qubika Website  
2) Validate that the website is displayed correctly, validating:  
   a) URL  
   b) Qubika logo  
3) Click ‘Contact us’ button  
4) Validate contact form is displayed, validating:  
   a) Name field is displayed  
   b) Email field is displayed  
   c) ‘Get in touch’ button is displayed  
5) Click ‘Get in touch’ button without filling any field  
6) Validate that all mandatory fields have an error message  
7) Validate that only ‘Name’ field is marked with red color  
8) Write ‘Test name’ on the ‘Name’ field  
9) Click ‘Get in touch’ button  
10) Validate that all mandatory fields have an error message except ‘Name’ field  
11) Validate that only ‘Email’ field is marked with red color

## Known Deviations
- **Red Highlight Behavior**: Steps 7 and 11 suggest that the first unfilled required field should be marked in red. This behavior was not observed during testing. Instead, the test performed consists of validating that when an error message is displayed for a required empty field, this message is red.
- **Field Naming**: The "Name" field is split into "First Name" and "Last Name," which were validated separately.
- **Button Label**: The button labeled "Submit" was tested instead of the non-existent "Get in touch" button.

## Enhancements
- The test runs on three browser engines to ensure cross-browser compatibility.
- A helper function (`check_error_messages`) was implemented to validate error messages for required fields efficiently.

## Project Structure
```
project-root/
|-- tests/
|   |-- test_Exercise3.py  # Main test script
|
|-- reports/
|   |-- report.html        # HTML execution report
|
|-- requirements.txt       # Python dependencies
|
|-- README.md              # Project documentation (this file)
```

## Prerequisites
1. Python 3.8+
2. [Playwright](https://playwright.dev/python/docs/intro) installed.

## Installation
1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Install Playwright browsers and dependencies:
   ```bash
   playwright install
   playwright install-deps
   ```

## Running the Tests
1. Navigate to the `tests` folder:
   ```bash
   cd tests
   ```
2. Run the test and generate an HTML report:
   ```bash
   pytest test_Exercise3.py --html=../reports/report.html --self-contained-html
   ```

## Viewing the Report
1. Open the HTML report:
   ```bash
   open ../reports/report.html
   ```
   or open it manually using your browser.

## Notes
- Ensure you do not submit any information in the forms during testing, as per the exercise instructions.
- If you encounter issues, verify that all dependencies are correctly installed and that the Playwright browsers are set up.

