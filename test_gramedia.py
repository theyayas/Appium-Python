from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import pytest
import time
import csv

desire_caps = {}

desire_caps['appPackage'] = "com.gramedia.retail"
desire_caps['appActivity'] = "com.gramedia.retail.activity.SplashScreenActivity"
desire_caps['platformName'] = "Android"
desire_caps['udid'] = "emulator-5554" # RR8R7027AZH, emulator-5554
desire_caps['noReset'] = True
desire_caps['autoGrantpermissions'] = True
desire_caps['forceAppLaunch'] = True

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_caps)
driver.implicitly_wait(10)

@pytest.mark.login
def test_login():
    Permission = 'com.android.permissioncontroller:id/permission_message' #id
    allowPermission = 'com.android.permissioncontroller:id/permission_allow_button' #id
    # Allow Gramedia to make and manage phone calls?
    # Allow Gramedia to access photos and media on your device?
    akun = 'com.gramedia.retail:id/txt_bot_menu_account' #id
    halamanLogin = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.TextView' #xpath
    email = 'com.gramedia.retail:id/txt_input_edt_email' #id
    password = 'com.gramedia.retail:id/txt_input_edt_password' #id
    buttonLogin = 'com.gramedia.retail:id/btn_login' #id
    savePassword = 'android:id/autofill_save_title' #id
    dontSavePassword = 'android:id/autofill_save_no' #id
    gambarAkun = 'com.gramedia.retail:id/img_user' #id
    textEmail = 'com.gramedia.retail:id/txt_email' #id

    for i in range(3):
        try:
            WebDriverWait(driver, 5).until(EC.alert_is_present())
            driver._switch_to.alert.accept()
        except TimeoutException:
            pass

    driver.find_element(By.ID, akun).click()

    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, halamanLogin)))
        print("masuk ke halaman login")
    except TimeoutException:
        raise Exception("tidak masuk ke halaman login")
    
    driver.find_element(By.ID, email).send_keys("yasingammarkanari@gmail.com")
    driver.find_element(By.ID, password).send_keys("H4l1dk4n4r1")
    driver.find_element(By.ID, email).click() # button login butuh trigger dari field password atau email. jika tidak diklik maka akan gagal login
    driver.find_element(By.ID, buttonLogin).click()

    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, savePassword)))
        driver.find_element(By.ID, dontSavePassword).click()
    except TimeoutException:
        pass

    if (driver.find_element(By.ID, gambarAkun) is not None) and (driver.find_element(By.ID, textEmail) is not None):
        driver.save_screenshot('D:\Bismillahirrohmaanirrahim\Appium-Python\login_gramedia.png')
    else:
        raise Exception("gagal login")
    
    time.sleep(3)
    driver.quit()

@pytest.mark.scroll_to_element
def test_scroll():
    internationalBook = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.widget.TextView[1]' #xpath
    lihatSemua = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.widget.TextView[2]' #xpath
    halamanFiksiFavorit = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView' #xpath

    '''while WebDriverWait(driver, 50).until(EC.invisibility_of_element_located((By.XPATH, fiksiFavorit))):
        driver.swipe(715, 1600, 715, 1100, 500)
        if driver.find_element(By.XPATH, fiksiFavorit) is None:
            print("fiksi favorit belum ketemu")
            continue
        else:
            print("fiksi favorit ketemu")
            break'''
    
    while EC.invisibility_of_element_located((driver.find_element(By.XPATH, internationalBook))):
        driver.swipe(715, 1600, 715, 1100, 500)
        if driver.find_element(By.XPATH, internationalBook) is not None:
            print("fiksi favorit ketemu")
            break
    
    time.sleep(2)

    '''while WebDriverWait(driver, 50).until(EC.invisibility_of_element_located((By.XPATH, fiksiFavorit))):
        driver.swipe(715, 1600, 715, 1100, 500)
        if driver.find_element(By.XPATH, fiksiFavorit) is not None:
            print("fiksi favorit ketemu")
            break'''
    
    '''ActionChains(driver).move_to_element(driver.find_element(By.XPATH, fiksiFavorit)).perform()'''

    '''driver.execute_script("argument[0].scrollIntoView();", driver.find_element(By.XPATH, fiksiFavorit))'''

    driver.find_element(By.XPATH, lihatSemua).click()

    assert driver.find_element(By.XPATH, halamanFiksiFavorit) is not None
    time.sleep(3)
    driver.quit()
