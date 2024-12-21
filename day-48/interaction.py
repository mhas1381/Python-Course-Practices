from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import  Keys
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option('detach' , True)

driver = webdriver.Edge(options = edge_options)
driver.get('https://en.wikipedia.org/wiki/Main_Page')

number_of_articles = driver.find_element(By.CSS_SELECTOR , '#articlecount a')
print(number_of_articles.text)

search = driver.find_element(By.NAME , 'search')
search.send_keys('Python')
search.send_keys(Keys.ENTER)


driver.quit()