from selenium import webdriver
import time

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the website
driver.get("https://www.swisstransfer.com/d/0c57f8ac-7578-4f32-a9c6-8eddbad46055")

# Find the class element and click on it 100 times
for _ in range(100):
    # Find the element
    download_icon = driver.find_element_by_css_selector('.ng-star-inserted .icon-download2')
    
    # Scroll a little down
    driver.execute_script("arguments[0].scrollIntoView();", download_icon)
    
    # Click on the element
    download_icon.click()
    
    # Wait for a few seconds before clicking again
    time.sleep(2)

# Close the browser
driver.quit()