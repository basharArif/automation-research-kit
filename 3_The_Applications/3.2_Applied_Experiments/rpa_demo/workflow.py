# File: experiments/rpa_demo/workflow.py
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

def rpa_workflow(url, num_runs=5):
    results = []
    for run in range(num_runs):
        start_time = time.time()
        driver = webdriver.Chrome()
        try:
            driver.get(url)
            quotes = []
            authors = []
            for i in range(10):
                quote_elements = driver.find_elements(By.CLASS_NAME, "quote")
                for element in quote_elements:
                    quotes.append(element.find_element(By.CLASS_NAME, "text").text)
                    authors.append(element.find_element(By.CLASS_NAME, "author").text)
                try:
                    next_button = driver.find_element(By.PARTIAL_LINK_TEXT, "Next")
                    next_button.click()
                except:
                    break
            
            df = pd.DataFrame({"quote": quotes, "author": authors})
            df.to_csv(f"output_run_{run}.csv", index=False)
            
            elapsed = time.time() - start_time
            results.append({"run": run, "success": True, "time": elapsed, "records": len(df)})
        except Exception as e:
            results.append({"run": run, "success": False, "time": time.time() - start_time, "error": str(e)})
        finally:
            driver.quit()
    
    return pd.DataFrame(results)

results_df = rpa_workflow("http://quotes.toscrape.com", num_runs=1)
print(results_df)
print(f"Success Rate: {results_df['success'].mean()*100:.1f}%")
print(f"Mean Time: {results_df[results_df['success']]['time'].mean():.2f}s")