 

import time
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir={}\driver_data".format(os.getcwd()))

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install()

driver.get("https://linkedin.com")

driver.get("https://www.linkedin.com/mynetwork/")
sleep(4)
buttons = driver.find_elements_by_class_name("invitation-card__action-btn")

for button in buttons:
    word=button.get_attribute("aria-label")
    if word.split(" ")[0] == "Accept":
        print("Clicking....")
        button.click()
        print("Clicked!!")
        sleep(1)

print("Done")

driver.close()
