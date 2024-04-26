from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get("http://localhost:3000/")


# Find the input fields and submit button

time.sleep(2)

email_input = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.CSS_SELECTOR,"input[type='email']")))
password_input = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

# Fill in the login form
email_input.send_keys("user@gmail.com")  # Enter your email
password_input.send_keys("1234")   # Enter your password

# Submit the form
submit_button.click()

# Wait for the page to load
time.sleep(2)  # Adjust the waiting time as needed

try:
    WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div/div[1]/div/button')))
    print("Login successful")
except:
    print("Login unsuccessful")

time.sleep(2) 

# Close the browser window
# driver.quit()


# ================================ REGISTER =====================================





driver = webdriver.Chrome()

driver.get("http://localhost:3000/registerPage")


# Find the input fields and submit button

time.sleep(2)

fname_input = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.NAME,'firstName')))
lname_input = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.NAME,'lastName')))
email_input = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.NAME,'email')))
password_input = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.NAME,'password')))
compassword_input = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.NAME,'confirmPassword')))

submit_button = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div/div[1]/div/form/button')))


fname_input.send_keys("Ishara ")  # Enter your email
lname_input.send_keys("Ashen")   # Enter your password
email_input.send_keys("isharatest1@gmail.com")  # Enter your email
password_input.send_keys("1234")   # Enter your password
compassword_input.send_keys("1234")
# Submit the form
submit_button.click()

# Wait for the page to load
time.sleep(8)  # Adjust the waiting time as needed

try:
    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    if alert.text == "Registration successful":
        print("Register successful")
    else:
        print("Register unsuccessful")
    # Close the alert
    alert.accept()
except:
    print("alertbox not unsuccessful")

time.sleep(2) 

# Close the browser window
driver.quit()













driver = webdriver.Chrome()

driver.get("http://localhost:3000/userPage")


# Find the input fields and submit button

time.sleep(2)



logout_button = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div/div[1]/div/button')))

logout_button.click()

try:
    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert.accept()
    try:
        WebDriverWait(driver,30).until(EC.presence_of_element_located((By.CSS_SELECTOR,"input[type='email']")))
        print("Logout successful")
    except:
        print("Logout unsuccessful")
except:
    print("Alertbox not unsuccessful")

time.sleep(2) 

# Close the browser window
driver.quit()










