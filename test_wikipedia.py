from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

desire_caps = {}

desire_caps['appPackage'] = "com.gramedia.retail"
desire_caps['appActivity'] = "com.gramedia.retail.activity.MainActivity"
desire_caps['platformName'] = "Android"
desire_caps['deviceName'] = "A50s milik Muhammad"
desire_caps['udid'] = "RR8N100ZCWP"

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_caps)