from selenium import webdriver
import time

# signup
NAME = 'Muskan Goel'
USERNAME = 'muskangoel7200@gmail.com'
PASSWORD = 'Mg150800*'

driver = webdriver.Chrome('chromedriver.exe')
driver.get('http://127.0.0.1:8000/signup')
time.sleep(1)

user_input = driver.find_element_by_id('name')
user_input.send_keys(NAME)
email_input = driver.find_element_by_id('email')
email_input.send_keys(USERNAME)
password_input = driver.find_element_by_id('password')
password_input.send_keys(PASSWORD)
cpass_input = driver.find_element_by_id('cpassword')
cpass_input.send_keys(PASSWORD)

signup_button = driver.find_element_by_xpath("//input[@class='btn btn-block register-btn btn-light mb-4']")
signup_button.click()
time.sleep(1)

#login
driver.get('http://127.0.0.1:8000/login')
time.sleep(1)

user_input = driver.find_element_by_id('email')
user_input.send_keys(USERNAME)

password_input = driver.find_element_by_id('password')
password_input.send_keys(PASSWORD)

login_button = driver.find_element_by_id('login')
login_button.click()
time.sleep(1)

#form
FIRST_NAME = 'Madhur'
LAST_NAME = 'Goel'
USERNAME = 'madhurgoel7200@gmail.com'
PASSWORD = 'Mg150800*'

driver.get('http://127.0.0.1:8000/form')
time.sleep(1)

first_input = driver.find_element_by_name('first_name')
first_input.send_keys(FIRST_NAME)
last_input = driver.find_element_by_name('last_name')
last_input.send_keys(LAST_NAME)
email_input = driver.find_element_by_name('email')
email_input.send_keys(USERNAME)
title_input = driver.find_element_by_xpath('/html/body/form/p[4]/label[2]')
title_input.click()
vehicle_input = driver.find_element_by_xpath('/html/body/form/p[6]/label[1]')
vehicle_input.click()

time.sleep(1)

submit_button = driver.find_element_by_xpath('/html/body/form/p[7]/button')
submit_button.click()