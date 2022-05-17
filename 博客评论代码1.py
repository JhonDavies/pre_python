import time
from selenium import webdriver
driver = webdriver.Chrome()

driver.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php')
time.sleep(2)

input_user = driver.find_element_by_name('log')
input_user.send_keys('crawer222')

password = driver.find_element_by_name('pwd')
password.send_keys('3190241059')

button = driver.find_element_by_name('wp-submit')
button.click()

driver.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/all-about-the-future_03/')
time.sleep(2)
test = driver.find_element_by_class_name('comment-form-comment').find_element_by_name('comment')
test.send_keys('selenium pratices')

buttons = driver.find_element_by_class_name('form-submit').find_element_by_name('submit')
buttons.click()
time.sleep(5)
driver.close()