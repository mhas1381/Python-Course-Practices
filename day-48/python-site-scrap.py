from selenium import webdriver
from selenium.webdriver.common.by import By

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option('detach' , True)

driver = webdriver.Edge(options = edge_options)
driver.get('https://python.org')

events = driver.find_elements(By.CLASS_NAME , 'event-widget li')


news_dict = {}

for event in range(len(events)):
    data = events[event].text.split("\n")
    item = {"time":data[0] ,"name": data[1]}
    news_dict[event] = item

print(news_dict)


driver.quit()