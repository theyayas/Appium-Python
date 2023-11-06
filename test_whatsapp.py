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

desire_caps['appPackage'] = "com.whatsapp"
desire_caps['appActivity'] = "com.whatsapp.HomeActivity"
desire_caps['platformName'] = "Android"
desire_caps['udid'] =  "emulator-5554" # RR8R7027AZH, emulator-5554
desire_caps['noReset'] = True
desire_caps['autoGrantpermissions'] = True
desire_caps['forceAppLaunch'] = True

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_caps)

@pytest.mark.spam
def test_spanm():
    driver.implicitly_wait(10)

    buttonSearch = 'com.whatsapp:id/menuitem_search' #id
    searchInput = 'com.whatsapp:id/search_input' #id
    akun = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.TextView' #xpath
    editMessage = 'com.whatsapp:id/entry' #id
    buttonAttach = 'com.whatsapp:id/input_attach_button' #id
    pickEmoji = 'com.whatsapp:id/emoji_picker_btn' #id
    emoji = '//android.view.View[@content-desc="😱"]' #xpath
    buttonSend = 'com.whatsapp:id/send' #id
    attachDokumen = 'com.whatsapp:id/pickfiletype_document_holder' #id
    searchDokumen = 'com.whatsapp:id/menuitem_search' #id
    editSearchDokumen = 'com.whatsapp:id/search_view_edit_text' #id
    dokumenPDF = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView' #xpath


    driver.find_element(By.ID, buttonSearch).click()
    driver.find_element(By.ID, searchInput).send_keys("didik")

    if "Didik" in driver.find_element(By.XPATH, akun).text:
        driver.find_element(By.XPATH, akun).click()
    else:
        raise Exception("Akun tidak ditemukan !!!")
    
    with open('email-password-recovery-code.csv') as fileCSV:
        read = csv.reader(fileCSV, delimiter = ',')
        for baris in read:
            driver.find_element(By.ID, editMessage).send_keys("Nama : ", baris[4], " ", baris[5], "\n", 
                                                              "ID : ", baris[1], "\n",
                                                              "Departemen : ", baris[6], "\n",
                                                              "Email : ", baris[0], "\n",
                                                              "One-time Password : ", baris[2], "\n",
                                                              "Recovery Code : ", baris[3], "\n",
                                                              "Lokasi : ", baris[7])
            driver.find_element(By.ID, buttonSend).click()
    
    driver.find_element(By.ID, pickEmoji).click()
    for i in range (0, 10):
        driver.find_element(By.XPATH, emoji).click()
    driver.find_element(By.ID, buttonSend).click()

    driver.find_element(By.ID, buttonAttach).click()
    driver.find_element(By.ID, attachDokumen).click()
    driver.find_element(By.ID, searchDokumen).click()
    driver.find_element(By.ID, editSearchDokumen).send_keys("100103")
    driver.back()

    if "100103" in driver.find_element(By.XPATH, dokumenPDF).text:
        driver.find_element(By.XPATH, dokumenPDF).click()
    else:
        raise Exception("Dokumen tidak ditemukan !!!")
    
    driver.find_element(By.ID, buttonSend).click()
    
    time.sleep(3)
    driver.close_app()

@pytest.mark.fotoHD
def test_foto_HD():
    driver.implicitly_wait(10)

    buttonSearch = 'com.whatsapp:id/menuitem_search' #id
    searchInput = 'com.whatsapp:id/search_input' #id
    akun = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.TextView' #xpath
    buttonKamera = 'com.whatsapp:id/camera_btn' #id
    buttonShutter = 'com.whatsapp:id/shutter' #id
    gambar4 = '(//android.widget.ImageView[@content-desc="Photo"])[3]' #xpath
    buttonHD = 'com.whatsapp:id/media_upload_quality_settings' #id
    high = 'com.whatsapp:id/media_quality_hd' #id
    caption = 'com.whatsapp:id/caption' #id
    buttonSend = 'com.whatsapp:id/send' #id


    driver.find_element(By.ID, buttonSearch).click()
    driver.find_element(By.ID, searchInput).send_keys("me")

    if "Me" in driver.find_element(By.XPATH, akun).text:
        driver.find_element(By.XPATH, akun).click()
    else:
        raise Exception("Akun tidak ditemukan !!!")
    
    driver.find_element(By.ID, buttonKamera).click()
    driver.find_element(By.XPATH, gambar4).click()
    driver.find_element(By.ID, buttonHD).click()
    driver.find_element(By.ID, high).click()
    #
    driver.find_element(By.ID, caption).click()
    driver.find_element(By.ID, caption).send_keys("Makan tuh foto HD !!!")
    
    time.sleep(2)
    driver.find_element(By.ID, buttonSend).click()

    time.sleep(10)
    driver.close_app()

@pytest.mark.rekamSuara
def test_rekam_suara():
    driver.implicitly_wait(10)

    buttonSearch = 'com.whatsapp:id/menuitem_search' #id
    searchInput = 'com.whatsapp:id/search_input' #id
    akun = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.TextView' #xpath
    buttonRekam = 'com.whatsapp:id/voice_note_btn' #id

    driver.find_element(By.ID, buttonSearch).click()
    driver.find_element(By.ID, searchInput).send_keys("me")

    if "Me" in driver.find_element(By.XPATH, akun).text:
        driver.find_element(By.XPATH, akun).click()
    else:
        raise Exception("Akun tidak ditemukan !!!")
    
    driver.find_element(By.ID, buttonRekam).click()
    TouchAction(driver).long_press(driver.find_element(By.ID, buttonRekam), duration = 5000).release().perform()

@pytest.mark.zoomFoto
def test_foto_HD():
    driver.implicitly_wait(10)

    buttonSearch = 'com.whatsapp:id/menuitem_search' #id
    searchInput = 'com.whatsapp:id/search_input' #id
    akun = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.TextView' #xpath
    buttonKamera = 'com.whatsapp:id/camera_btn' #id
    buttonShutter = 'com.whatsapp:id/shutter' #id
    gambar3 = '(//android.widget.ImageView[@content-desc="Photo"])[3]' #xpath
    buttonHD = 'com.whatsapp:id/media_upload_quality_settings' #id
    high = 'com.whatsapp:id/media_quality_hd' #id
    caption = 'com.whatsapp:id/caption' #id
    buttonSend = 'com.whatsapp:id/send' #id


    driver.find_element(By.ID, buttonSearch).click()
    driver.find_element(By.ID, searchInput).send_keys("me")

    if "Me" in driver.find_element(By.XPATH, akun).text:
        driver.find_element(By.XPATH, akun).click()
    else:
        raise Exception("Akun tidak ditemukan !!!")
    
    driver.find_element(By.ID, buttonKamera).click()
    driver.find_element(By.XPATH, gambar3).click()
    time.sleep(3)

    # Penggunaan MultiAction untuk melakukan zoom in
    a1 = TouchAction(driver).long_press(None, 715, 1100).move_to(None, 715, 800).wait(1000).release()
    a2 = TouchAction(driver).long_press(None, 715, 1600).move_to(None, 715, 1900).wait(1000).release()

    #MultiAction(driver).add(touch1, touch2).
    #MultiAction(driver).add(touch1.perform(), touch2.release())

    zoom = MultiAction(driver)
    zoom.add(a1)
    zoom.add(a2)
    zoom.perform()

    driver.find_element(By.ID, buttonSend).click()