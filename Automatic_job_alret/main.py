from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time


EMAIL = ""
PASSWORD = ""



def abort_application():
    # Click Close Button
    close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()

    time.sleep(2)
    # Click Discard Button
    discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard_button.click()


chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_option)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3969845064&f_AL=true&f_TPR=r86400&geoId=112376381&keywords=python%20develper&location=Bangalore%20Urban%2C%20Karnataka%2C%20India&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true")

# # Click Reject Cookies Button
# time.sleep(2)
# reject_button = driver.find_element(by=By.CSS_SELECTOR, value='button[action-type="DENY"]')
# reject_button.click()

time.sleep(2)
sign_in_btn = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_btn.click()

time.sleep(5)
email_id = driver.find_element(By.ID, value="username")
password_field = driver.find_element(By.ID, value="password")

email_id.send_keys(EMAIL)
password_field.send_keys(PASSWORD)
password_field.send_keys(Keys.ENTER)

#input("Press Enter when you have solved the Captcha")

#Locate the apply button
# time.sleep(5)
# apply_button = driver.find_element(By.ID, value="ember50")
# apply_button.click()

# Get Listings
time.sleep(5)
all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

# Apply for Jobs
for listing in all_listings:
    print("Opening Listing")
    listing.click()
    time.sleep(2)
    try:
        # Click Apply Button
        apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
        apply_button.click()

        # Insert Phone Number
        # # Find an <input> element where the id contains phoneNumber
        # time.sleep(5)
        # phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        # if phone.text == "":
        #     phone.send_keys(PHONE)

        # Check the Submit Button
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            abort_application()
            print("Complex application, skipped.")
            continue
        else:
            # Click Submit Button
            print("Submitting job application")
            submit_button.click()

        time.sleep(2)
        # Click Close Button
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        abort_application()
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()