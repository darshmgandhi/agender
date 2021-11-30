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
time.sleep(1)

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

#builder
TITLE = 'Employee Details'
INPUTNAME = 'USERNAME'
INPUTPLACE = 'Enter your Name'
ELEMENTS = '3'
RADIONAME = 'TITLE'
RADIOLABELS = 'MISS, MR, MRS'
CHECKNAME = 'VEHICLE'
CHECKLABELS = 'CAR, BUS, BIKE'
driver.get('http://127.0.0.1:8000/builder')
time.sleep(1)

title = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/form/label[1]/span[2]')
title.click()
title_input = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div/form/label[3]/input')
title_input.send_keys(TITLE)
add_input = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div/form/button')
add_input.click()
time.sleep(1)

input = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/form/label[2]/span[2]')
input.click()
input_input1 = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div/form/label[3]/input')
input_input1.send_keys(INPUTNAME)
input_input2 = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div/form/label[4]/input')
input_input2.send_keys(INPUTPLACE)
add_input.click()
time.sleep(1)

radio = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/form/label[3]/span[2]')
radio.click()
radio_input1 = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div/form/label[1]/input')
radio_input1.send_keys(ELEMENTS)
radio_input2 = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div/form/label[3]/input')
radio_input2.send_keys(RADIONAME)
radio_input3 = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div/form/label[5]/input')
radio_input3.send_keys(RADIOLABELS)
add_input.click()
time.sleep(1)

check = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/form/label[4]/span[2]')
check.click()
check_input1 = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div/form/label[1]/input')
check_input1.send_keys(ELEMENTS)
check_input2 = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div/form/label[3]/input')
check_input2.send_keys(CHECKNAME)
check_input3 = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div/form/label[5]/input')
check_input3.send_keys(CHECKLABELS)
add_input.click()
time.sleep(1)

image = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/form/label[5]/span[2]')
image.click()
add_input.click()
time.sleep(2)

generate = driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/button[1]')
generate.click()
time.sleep(2)

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
time.sleep(1)