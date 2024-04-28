from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# driver = webdriver.Chrome()

# driver.get("http://localhost:3000/")




# time.sleep(2)

# email_input = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.CSS_SELECTOR,"input[type='email']")))
# password_input = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
# submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")


# email_input.send_keys("user@gmail.com") 
# password_input.send_keys("1234")  


# submit_button.click()


# time.sleep(2)  

# try:
#     WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div/div[1]/div/button')))
#     print("Login successful")
# except:
#     print("Login unsuccessful")

# time.sleep(2) 


# # driver.quit()





driver = webdriver.Chrome()

driver.get("http://localhost:3000/registerPage")




time.sleep(2)

fname_input = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.NAME,'firstName')))
lname_input = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.NAME,'lastName')))
email_input = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.NAME,'email')))
password_input = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.NAME,'password')))
compassword_input = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.NAME,'confirmPassword')))
submit_button = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div/div[1]/div/form/button')))


fname_input.send_keys("Ishara ")  
lname_input.send_keys("Ashen")   
email_input.send_keys("isharatest212@gmail.com")  
password_input.send_keys("1234")   
compassword_input.send_keys("1234")

submit_button.click()


time.sleep(8)  

try:
    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    if alert.text == "Registration successful":
        print("Register successful")
    else:
        print("Register unsuccessful")
   
    alert.accept()
except:
    print("alertbox not unsuccessful")

time.sleep(2) 


# driver.quit()




email_input = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.CSS_SELECTOR,"input[type='email']")))
password_input = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.CSS_SELECTOR,"input[type='password']")))
submit_button = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.CSS_SELECTOR,"button[type='submit']")))



email_input.send_keys("user@gmail.com") 
password_input.send_keys("1234")   


submit_button.click()


time.sleep(8)  

try:
    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    if alert.text == "Login successful":
        print("Login successful")
    else:
        print("Login unsuccessful")
  
    alert.accept()
except:
    print("alertbox not unsuccessful")

time.sleep(2) 


# driver.quit()









content_input = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div/div[2]/textarea')))
predicr_button = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div/div[2]/button')))

content_input.send_keys("I love you") 
predicr_button.click()




time.sleep(2)  

try:
    WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div/div[2]/div[1]/p')))
    print("Petection successful")
except:
    print("Petection unsuccessful")








# driver = webdriver.Chrome()

# driver.get("http://localhost:3000/userPage")


# time.sleep(2)



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


driver.quit()










