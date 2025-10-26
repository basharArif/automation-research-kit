# main.py - RPA Demo Experiment

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape_quote():
    """Scrapes the first quote from quotes.toscrape.com."""
    # Initialize the Chrome driver
    # This will automatically download and manage the chromedriver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    try:
        # Navigate to the website
        driver.get("http://quotes.toscrape.com")

        # Wait for the page to load
        time.sleep(2)

        # Find the first quote element
        quote_element = driver.find_element(By.CLASS_NAME, "text")

        # Get the text of the quote
        quote = quote_element.text

        print(f"Successfully scraped quote: \"{quote}\"")

    finally:
        # Close the browser
        driver.quit()

def main():
    """Main function to run the RPA demo."""
    print("Running RPA demo...")
    scrape_quote()

if __name__ == "__main__":
    main()
