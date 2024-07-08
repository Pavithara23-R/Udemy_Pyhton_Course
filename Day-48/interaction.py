from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_option)
driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, value="fName")
last_name = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")

#fill out the keys
first_name.send_keys("Pavi")
last_name.send_keys("thara")
email.send_keys("pavi@gamil.com")


submit = driver.find_elements(By.CSS_SELECTOR, value="form button")
submit.click()


# article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# #article_count.click()
#
# all_portal = driver.find_element(By.LINK_TEXT, value="Content portals")
# #all_portal.click()
#
# #find the "search" <input> by name
# search = driver.find_element(By.NAME, value="search")
#
#
# #sending keyword input
# search.send_keys("Python")
#
# #driver.quit()