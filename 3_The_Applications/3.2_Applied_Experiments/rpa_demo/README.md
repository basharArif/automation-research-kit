# Robotic Process Automation (RPA) Demo

This experiment demonstrates an automated web scraping workflow that logs into a website, extracts data, and stores it in CSV format.

## Description

The `workflow.py` script implements an RPA workflow using Selenium to automate a multi-step process: navigating to a website, extracting data from tables, and saving the results to CSV files. The experiment measures success rate, execution time, and error types over multiple runs.

## Installation

To run this experiment, you need to install the dependencies listed in the main `requirements.txt` file and ensure you have a compatible Chrome browser and ChromeDriver.

```bash
pip install -r ../../../requirements.txt
```

## Running the Experiment

To run the experiment, execute the `workflow.py` script from within this directory:

```bash
python workflow.py
```

## Expected Results

The script will run the automated workflow once (with the default configuration) and output a results DataFrame showing success rate and mean execution time. It will also create `output_run_0.csv` with the extracted data.

## Required Setup

This experiment requires:
- Google Chrome browser installed
- ChromeDriver in your PATH (or properly configured)
- Internet connection to access the target website

## Customization

To adapt this demo for other websites:
1. Modify the URL in the function call
2. Update the CSS selectors to match the target website's structure
3. Adjust the data extraction logic as needed

## Troubleshooting

If you encounter any issues, please ensure:
- Chrome browser is installed
- ChromeDriver is properly configured
- Internet connection is working
- The target website is accessible