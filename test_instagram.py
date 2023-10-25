from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import pytest
import time

desire_caps = {}

desire_caps['appPackage'] = "com.instagram.android"
desire_caps['appActivity'] = "com.instagram.mainactivity.InstagramMainActivity"
desire_caps['platformName'] = "Android"
desire_caps['deviceName'] = "ayas's phone"
desire_caps['udid'] = "RR8R7027AZH"
desire_caps['noReset'] = True
desire_caps['autoGrantpermissions'] = True
desire_caps['forceAppLaunch'] = True

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_caps)

@pytest.mark.coba
def test_coba():
    elemenBesarDav = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.GridView/android.widget.LinearLayout[1]/android.widget.LinearLayout"
    dav = '//android.widget.TextView[@content-desc="Dav"]'
    editMessage = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[3]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText'
    send = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[3]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button'
    
    time.sleep(2)
    driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="3 unread messages"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.view.ViewGroup/android.widget.FrameLayout/android.widget.TextView').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText').send_keys("dav")
    time.sleep(1)

    try:
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, dav), "Dav"))
        time.sleep(1)
        driver.find_element(By.XPATH, elemenBesarDav).click()
        time.sleep(1)
    except TimeoutException:
        raise Exception("akun tidak ditemukan")
    
    driver.find_element(By.XPATH, editMessage).send_keys("Pesan ini dikirim menggunakan Appium")
    driver.find_element(By.XPATH, send).click()
    time.sleep(3)
    
    #driver.close_app()