from appium import webdriver
from selenium.webdriver.common.by import By
import time

desire_caps = {}

desire_caps['appPackage'] = "com.example.i_mun"
desire_caps['appActivity'] = "com.example.i_mun.login"
desire_caps['platformName'] = "Android"
desire_caps['deviceName'] = "A50s milik Muhammad"
desire_caps['udid'] = "RR8N100ZCWP"

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_caps)
time.sleep(1)

driver.find_element(By.ID, "com.example.i_mun:id/go_register").click()
time.sleep(1)

driver.find_element(By.ID, "com.example.i_mun:id/editTextTextPersonName").click()
driver.find_element(By.ID, "com.example.i_mun:id/editTextTextPersonName").send_keys("yahaha")
time.sleep(1)

driver.find_element(By.ID, "com.example.i_mun:id/editTextTextEmailAddress").click()
driver.find_element(By.ID, "com.example.i_mun:id/editTextTextEmailAddress").send_keys("yahaha")
time.sleep(1)

driver.find_element(By.ID, "com.example.i_mun:id/address").click()
driver.find_element(By.ID, "com.example.i_mun:id/address").send_keys("yahaha")
time.sleep(1)
driver.back()

driver.find_element(By.ID, "com.example.i_mun:id/editTextTextPassword2").click()
driver.find_element(By.ID, "com.example.i_mun:id/editTextTextPassword2").send_keys("yahaha")
time.sleep(1)
driver.back()

driver.find_element(By.ID, "com.example.i_mun:id/editTextTextPassword").click()
driver.find_element(By.ID, "com.example.i_mun:id/editTextTextPassword").send_keys("yahaha")
time.sleep(1)
driver.back()
driver.quit()

'''driver.find_element(By.XPATH, "com.example.i_mun:id/btn_login").click()
time.sleep(3)

id register com.example.i_mun:id/go_register

id nama com.example.i_mun:id/editTextTextPersonName
id email com.example.i_mun:id/editTextTextEmailAddress
id alamat com.example.i_mun:id/address
id passsword1 com.example.i_mun:id/editTextTextPassword2
id password2 com.example.i_mun:id/editTextTextPassword

id register com.example.i_mun:id/btn_register'''
