from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Edge()
driver.get("http://orteil.dashnet.org/experiments/cookie/")


cookie = driver.find_element(By.ID, "cookie")

items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
five_min = time.time() + 60 * 5

while True:
    cookie.click()

    if time.time() > timeout:

        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        item_prices = []


        for price in all_prices:
            element_text = price.text
            if element_text != "":
                try:
                    cost = int(element_text.split("-")[1].strip().replace(",", ""))
                    item_prices.append(cost)
                except IndexError:
                    continue


        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]


        money_element = driver.find_element(By.ID, "money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)


        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count >= cost:
                affordable_upgrades[cost] = id


        if affordable_upgrades:
            highest_price_affordable_upgrade = max(affordable_upgrades)
            to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]
            try:
                driver.find_element(By.ID, to_purchase_id).click()
            except Exception as e:
                print(f"Error purchasing {to_purchase_id}: {e}")

        timeout = time.time() + 5

    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.ID, "cps").text
        print(f"Cookies per second: {cookie_per_s}")
        break
