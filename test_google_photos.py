from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

import pytest
import time
import csv

desire_caps = {}

desire_caps['appPackage'] = "com.google.android.apps.photos"
desire_caps['appActivity'] = "com.google.android.apps.photos.home.HomeActivity"
desire_caps['platformName'] = "Android"
desire_caps['udid'] = "emulator-5554"
desire_caps['noReset'] = True
desire_caps['autoGrantpermissions'] = True
desire_caps['forceAppLaunch'] = True

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_caps)

@pytest.mark.zoomFoto
def test_zoom_foto():
    driver.implicitly_wait(10)

    library = 'com.google.android.apps.photos:id/tab_library' #id
    whatsapp = '//android.widget.LinearLayout[@content-desc="WhatsApp Images"]' #xpath
    foto = '//android.view.ViewGroup[@content-desc="Photo taken on Nov 1, 2023 11:34:37"]' #xpath

    driver.find_element(By.ID, library).click()
    driver.find_element(By.XPATH, whatsapp).click()
    driver.find_element(By.XPATH, foto).click()

    touch1 = TouchAction(driver).long_press(None, 715, 1380).move_to(None, 1000, 1000).release()
    touch2 = TouchAction(driver).long_press(None, 715, 1420).move_to(None, 400, 1800).release()

    zoom = MultiAction(driver)
    zoom.add(touch1)
    zoom.add(touch2)
    zoom.perform()

    time.sleep(5)
    driver.quit()