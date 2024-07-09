from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time

EMAIL = ""
PASSWORD =""


chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)


driver = webdriver.Chrome(chrome_option)
driver.get("https://tinder.com/")

time.sleep(3)
accept_btn = driver.find_element(By.XPATH, value='//*[@id="u-1419960890"]/div/div[2]/div/div/div[1]/div[1]/button')
accept_btn.click()

# Click login button
time.sleep(3)
login_button = driver.find_element(By.XPATH, value='//*[text()="Log in"]')
login_button.click()




# time.sleep(5)
# #more option btn
# more_option = driver.find_element(By.CSS_SELECTOR, value="#u1146625330 > div > div > div > div.Ta\(c\).H\(100\%\).D\(f\).Fxd\(c\).Pos\(r\) > div > div > div.H\(100\%\).D\(f\).Fxd\(c\) > div.Mt\(a\) > span > button")
# more_option.click()

# Login with FaceBook account
time.sleep(3)
fb_login = driver.find_element(By.XPATH, value='//*[@id="u1146625330"]/div/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
fb_login.click()

#Switch to Facebook login window
time.sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

time.sleep(5)
email = driver.find_element(By.XPATH, value='//*[@id="email"]')
email.send_keys(EMAIL)
password = driver.find_element(By.XPATH, value='//*[@id="pass"]')
password.send_keys(PASSWORD)
email.send_keys(Keys.ENTER)

#Switch back to Tinder window
driver.switch_to.window(base_window)
print(driver.title)

#Delay by 5 seconds to allow page to load.
time.sleep(5)

#Allow location
allow_location_button = driver.find_element(By.XPATH, value='/html/body/div[2]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()

#Disallow notifications
notifications_button = driver.find_element(By.XPATH, value='//*[@id="u1146625330"]/div/div/div/div/div[3]/button[1]')
notifications_button.click()

#Allow cookies
cookies = driver.find_element(By.XPATH, value='//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()


#Tinder free tier only allows 100 "Likes" per day. If you have a premium account, feel free to change to a while loop.
for n in range(100):

    #Add a 1 second delay between likes.
    time.sleep(1)

    try:
        print("called")
        like_button = driver.find_element(By.XPATH, value=
            '//*[@id="u-1419960890"]/div/div[1]/div/div/main/div/div/div[1]/div/div[3]/div/div[4]/button')
        like_button.click()

    #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
            match_popup.click()

        #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            time.sleep(2)
