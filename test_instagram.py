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
desire_caps['deviceName'] = "A54 milik Didik Maulana"
desire_caps['udid'] = "RRCW4017X0E"
#desire_caps['noReset'] = True
desire_caps['autoGrantpermissions'] = True
desire_caps['forceAppLaunch'] = True

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_caps)

@pytest.mark.coba
def test_coba():
    elemenBesarDav = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.GridView/android.widget.LinearLayout[1]/android.widget.LinearLayout"
    dav = '//android.widget.TextView[@content-desc="Maul"]'
    editMessage = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[3]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText'
    send = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[3]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button'
    
    time.sleep(2)
    driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="2 unread messages"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.view.ViewGroup/android.widget.FrameLayout/android.widget.TextView').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText').send_keys("maul")
    time.sleep(1)

    try:
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, dav), "Maul"))
        time.sleep(1)
        driver.find_element(By.XPATH, elemenBesarDav).click()
        time.sleep(1)
    except TimeoutException:
        raise Exception("akun tidak ditemukan")
    
    driver.find_element(By.XPATH, editMessage).send_keys("Pesan ini dikirim menggunakan Appium")
    driver.find_element(By.XPATH, send).click()
    time.sleep(3)
    
    #driver.close_app()

@pytest.mark.loginBenar
def test_login_benar():
    nonOfTheAbove = '//android.widget.LinearLayout[@content-desc="Choose a Credential"]/android.widget.LinearLayout/android.widget.Button'
    username = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText'
    password = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText'
    login = '//android.widget.Button[@content-desc="Login"]'
    logo = '//android.widget.ImageView[@content-desc="Instagram from Meta"]'

    time.sleep(3)
    driver.back()

    try:
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, logo)))
        time.sleep(1)
        driver.find_element(By.XPATH, username).send_keys("yasingammarkanari@gmail.com")
        time.sleep(1)
    except TimeoutException:
        pass

    driver.find_element(By.XPATH, password).send_keys("yahahahahahhah")
    driver.find_element(By.XPATH, login).click() #534 1297