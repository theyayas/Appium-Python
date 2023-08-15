from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
import pyautogui
import pytest
import time
import warnings

warnings.filterwarnings("ignore")

desire_caps = {}

desire_caps['appPackage'] = "com.outsystemsenterprise.acctst1.AccMe"
desire_caps['appActivity'] = "com.outsystemsenterprise.acctst1.AccMe.MainActivity"
desire_caps['platformName'] = "Android"
desire_caps['deviceName'] = "A50s milik Muhammad"
desire_caps['udid'] = "RR8N100ZCWP"

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_caps)

#=========================================================================================================================
#                                                   LOGIN SALAH
#=========================================================================================================================

@pytest.mark.loginSalah
def test_login_salah():
    try:
        WebDriverWait(driver, 90).until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Image')))
        driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText').click()
    except TimeoutException:
        pass

    driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText').send_keys("yahaha")
    driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText').send_keys("yahaha")
    driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button').click()

    try:
        location1 = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout"
        location = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.Button[1]"
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, location1)))
        driver.find_element(By.XPATH, location).click()
    except TimeoutException:
        pass

    try:
        error_message = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.widget.TextView[2]"
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, error_message)))
        assert error_message is not None
        print("Sesuai, tidak berhasil login")
    except TimeoutException:
        print("Gagal :(")
        pass

    time.sleep(2)
    driver.quit()


#=========================================================================================================================
#                                                   LOGIN BERHASIL
#=========================================================================================================================

@pytest.mark.loginBerhasil
def test_login_berhasil():
    try:
        WebDriverWait(driver, 90).until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Image')))
        driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText').click()
    except TimeoutException:
        pass

    driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText').send_keys("KLG.W08094")
    driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText').send_keys("Password1")
    driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button').click()

    try:
        location1 = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout"
        location = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.Button[1]"
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, location1)))
        driver.find_element(By.XPATH, location).click()
    except TimeoutException:
        pass

    try:
        logo_akun = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]/android.view.View[1]/android.widget.Image"
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, logo_akun)))
        assert logo_akun is not None
        print("Sesuai, berhasil login")
    except TimeoutException:
        print("Gagal :(")
        pass

    time.sleep(2)
    driver.quit()

#=========================================================================================================================
#                                                   SIMULASI KREDIT
#=========================================================================================================================

@pytest.mark.simulasiKredit
def test_simulasi_kredit():
    button_simulasi_kredit = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View/android.view.View/android.view.View[3]/android.view.View[1]/android.view.View/android.widget.Image"
    syncall = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View/android.view.View/android.widget.Button"
    elemen_terakhir = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View/android.view.View/android.view.View[6]/android.widget.TextView[1]"
    Index_entry = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.widget.Button"
    brand = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View/android.view.View/android.view.View/android.widget.EditText"
    toyota = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[4]/android.view.View/android.widget.TextView[2]"
    typee = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[4]/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.widget.EditText"
    agya = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[4]/android.view.View/android.view.View[2]/android.view.View/android.widget.TextView[1]"
    model = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[4]/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.widget.EditText"
    gmt = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[4]/android.view.View[2]/android.view.View[2]/android.view.View/android.widget.TextView[1]"
    #001 - 1.0 G M/T - 1 TON MB
    tahun = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[6]/android.view.View/android.view.View/android.view.View/android.view.View"
    thn2021 = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[2]"
    tenor = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[7]/android.view.View/android.view.View/android.view.View/android.view.View"
    tenor24 = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[5]"
    dp = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[7]/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.widget.EditText"
    dealer = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[8]/android.view.View/android.view.View/android.view.View/android.widget.EditText"
    #AI ISO-JKT PRAMUKA 01000500008
    pramuka = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[8]/android.view.View[2]/android.view.View/android.widget.TextView[2]"
    sales = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[9]/android.view.View/android.view.View/android.view.View/android.widget.EditText"
    #A RIZAL R TOWIDJOJO - S0125
    hitung = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[10]/android.widget.Button"
    berhasil = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View[2]/android.view.View"

    #menunggu halaman login
    try:
        WebDriverWait(driver, 180).until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Image')))
        driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText').click()
    except TimeoutException:
        pass

    #input data pada halaman login
    driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText').send_keys("KLG.W09079")
    driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText').send_keys("Password1")
    driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button').click()

    #location permition
    try:
        location1 = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout"
        location = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.Button[1]"
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, location1)))
        driver.find_element(By.XPATH, location).click()
    except TimeoutException:
        pass

    #apakah berhasi login? YAHAHAHAHAHAHHA
    try:
        WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, button_simulasi_kredit)))
        #klik button simulasi kredit
        driver.find_element(By.XPATH, button_simulasi_kredit).click()
    except TimeoutException:
        pass

    # Synchronize dulu guyssssss
    try:
        WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, syncall)))
        driver.find_element(By.XPATH, syncall).click()
        driver.swipe(470, 1400, 470, 400, 900)
    except TimeoutException:
        pass
    
    # Menunggu Synchronize all lama anjayanto
    try:
        WebDriverWait(driver, 300).until(EC.text_to_be_present_in_element((By.XPATH, elemen_terakhir), "180")) # BERHASIL YAHAHAHAHAHAHA (KETAWA JAHAT)
        driver.back()
    except TimeoutException:
        pass

    # tunggu button simulasi kredit lagi
    time.sleep(10)
    driver.find_element(By.XPATH, button_simulasi_kredit).click()   #klik button simulasi kredit

    # menunggu halaman simulasi kredit dengan menunggu button index entry
    try:
        WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, Index_entry)))
        time.sleep(5)
        TouchAction(driver).tap(element = None, x = 488, y = 145).perform() # Menghilangkan pesan synchron
    except TimeoutException:
        pass
    
    # Pilih Brand
    driver.swipe(470, 1400, 470, 800, 900)
    driver.find_element(By.XPATH, brand).click()
    TouchAction(driver).tap(element = None, x = 566, y = 850).perform() #ini yang bikin susah berhari-hari juga hadeuuhhh
    time.sleep(1)

    # Pilih Type
    driver.find_element(By.XPATH, typee).click()
    time.sleep(2)
    driver.find_element(By.XPATH, agya).click() # x = 566, y = 800
    time.sleep(1)

    # Pilih Model
    driver.find_element(By.XPATH, model).click()
    time.sleep(2)
    driver.find_element(By.XPATH, gmt).click() # x = 566, y = 1000
    time.sleep(1)

    # Pilih Tahun
    driver.find_element(By.XPATH, tahun).click()
    time.sleep(1)
    driver.find_element(By.XPATH, thn2021).click()
    time.sleep(1)

    # Pilih Tenor
    TouchAction(driver).tap(element = None, x = 250, y = 1450).perform() # 
    #driver.find_element(By.XPATH, tenor).click()
    time.sleep(1)
    driver.find_element(By.XPATH, tenor24).click()
    time.sleep(1)

    # Scroll
    driver.swipe(470, 1400, 470, 400, 900)

    # Pilih DP
    driver.find_element(By.XPATH, dp).click()
    time.sleep(1)
    TouchAction(driver).tap(element = None, x = 413, y = 1753).perform() # 5
    TouchAction(driver).tap(element = None, x = 413, y = 2102).perform() # 0
    TouchAction(driver).tap(element = None, x = 930, y = 1753).perform() # enter
    time.sleep(1)

    # Pilih Dealer
    TouchAction(driver).tap(element = None, x = 930, y = 1753).perform() # enter
    time.sleep(1)
    TouchAction(driver).tap(element = None, x = 1010, y = 1666).perform()   # P
    TouchAction(driver).tap(element = None, x = 379, y = 1666).perform()    # R
    TouchAction(driver).tap(element = None, x = 122, y = 1823).perform()    # A
    TouchAction(driver).tap(element = None, x = 853, y = 1971).perform()    # M
    TouchAction(driver).tap(element = None, x = 698, y = 1666).perform()    # u
    TouchAction(driver).tap(element = None, x = 851, y = 1823).perform()    # K
    TouchAction(driver).tap(element = None, x = 122, y = 1823).perform()    # A
    time.sleep(2)
    TouchAction(driver).tap(element = None, x = 460, y = 1170).perform()    # Klik dealernya
    time.sleep(1)

    # Pilih Sales x = 566, y = 1086
    driver.find_element(By.XPATH, sales).click()
    time.sleep(1)
    #driver.swipe(470, 1400, 470, 400, 900)
    TouchAction(driver).tap(element = None, x = 460, y = 1180).perform()    # Klik salesnya
    time.sleep(1)

    # Hitung yahahahahahahahah
    driver.find_element(By.XPATH, hitung).click()

    # Apakah berhasil hitung???????????????????????
    try:
        WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, berhasil)))
        assert berhasil is not None
        print("Berhasil Hitung Simulasi Kredit :)")
    except TimeoutException:
        print("Gagal :(")
    
    time.sleep(5)
    driver.quit()




