from selenium import webdriver
from selenium.webdriver.common.by import By
import time
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option('detach' , True)

driver = webdriver.Edge(options=edge_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID , 'cookie')
money = driver.find_element(By.ID , 'money')
stores = driver.find_elements(By.CLASS_NAME , 'grayed')
for store in stores:
    print(store.text)

# timeout = time.time() + 5
# while True:
#     cookie.click()
#     if time.time() > timeout:

driver.quit()




