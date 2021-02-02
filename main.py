from selenium import webdriver
import time
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support import expected_condition as EC  
#from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome("C:\Cdriver\chromedriver87.exe")

#opening the site and waiting 3 secs to let it load
driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.maximize_window()
time.sleep(3)


cookie = driver.find_element_by_id("bigCookie")  #Locating the bigCookie to click
cookieCount = driver.find_element_by_id("cookies")#Locating the Cookie COunter
items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(1,-1,-1)]#Locating the Products to Upgrade (as a List)

#Setting the actionChain
actions = ActionChains(driver)
actions.click(cookie)

for i in range(5000):
	actions.perform()
	count = int(cookieCount.text.split(" ")[0])
	for item in items:
		value = int(item.text)
		if (value<=count):
			upgrade_actions = ActionChains(driver)
			upgrade_actions.move_to_element(item)
			upgrade_actions.click()
			upgrade_actions.perform()

    


