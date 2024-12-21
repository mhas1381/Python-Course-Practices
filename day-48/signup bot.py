from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import  Keys
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option('detach' , True)

driver = webdriver.Edge(options=edge_options)
driver.get("http://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element(By.NAME , 'fName')
fname.send_keys("Mamad")

lname = driver.find_element(By.NAME , 'lName')
lname.send_keys("Danaee")

email = driver.find_element(By.NAME , 'email')
email.send_keys("test@gmail.com")

btn = driver.find_element(By.CLASS_NAME , 'btn')
btn.send_keys(Keys.ENTER)

driver.quit()