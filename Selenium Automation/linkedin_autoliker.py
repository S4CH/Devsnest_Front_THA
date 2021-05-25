 
import os
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
 from webdriver_manager.firefox import GeckoDriverManager

links = [
    "link_1",
    "link_2"
]



options = webdriver.ChromeOptions()
options.add_argument("user-data-dir={}\driver_data".format(os.getcwd()))

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install()

driver.get("https://linkedin.com")


while "1" != input("press 1 when signed in: "):
    pass
for link in links:
    try:
        print("accessing link ", link)
        driver.get(link)
        sleep(2)
        el = driver.find_element_by_class_name("react-button__trigger")
        if "false" == el.get_attribute("aria-pressed"):
            print("liking")
            el.click()
            print("liked")
            sleep(1)
        else:
            print("already processed link ", link)
    except Exception as e:
        print("error processing link\nlink: ", link, "\nerror",  e)

driver.close()
