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
desire_caps['deviceName'] = "ayas' phone"
desire_caps['udid'] = "RR8R7027AZH"
desire_caps['noReset'] = True
desire_caps['autoGrantpermissions'] = True
desire_caps['forceAppLaunch'] = True

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_caps)

@pytest.mark.coba
def test_coba():
    elemenBesarDav = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.GridView/android.widget.LinearLayout[1]/android.widget.LinearLayout"
    akun = '//android.widget.TextView[@content-desc="Maul"]'
    editMessage = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[3]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText'
    send = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[3]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button'
    
    time.sleep(2)
    driver.find_element(By.ID, 'com.instagram.android:id/action_bar_inbox_button').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.view.ViewGroup/android.widget.FrameLayout/android.widget.TextView').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText').send_keys("maul")
    time.sleep(1)

    '''try:
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, dav), "Maul"))
        time.sleep(1)
        driver.find_element(By.XPATH, elemenBesarDav).click()
        time.sleep(1)
    except TimeoutException:
        raise Exception("akun tidak ditemukan")'''
    
    if driver.find_element(By.XPATH, akun).text == "Maul":
        driver.find_element(By.XPATH, elemenBesarDav).click()
        time.sleep(1)
    else:
        raise Exception("Akun tidak ditemukan!!!")

    
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

    try:
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, nonOfTheAbove)))
        driver.find_element(By.XPATH, nonOfTheAbove).click()
        time.sleep(1)
        driver.back()
    except TimeoutException:
        pass

    try:
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, logo)))
        time.sleep(1)
        driver.find_element(By.XPATH, username).send_keys("yahahaha@gmail.com")
        time.sleep(1)
    except TimeoutException:
        pass

    driver.find_element(By.XPATH, password).send_keys("yahahahahahaha")
    driver.find_element(By.XPATH, login).click() #534 1297

@pytest.mark.follow
def test_follow_orang():
    searchButton = 'com.instagram.android:id/search_tab'
    searchBar = 'com.instagram.android:id/action_bar_search_edit_text'
    akunMaul = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TextView'
    fotoProfil = 'com.instagram.android:id/row_profile_header_imageview'
    followBack = 'com.instagram.android:id/profile_header_follow_button'
    buttonMessage = 'com.instagram.android:id/button_container'
    editMessage = 'com.instagram.android:id/row_thread_composer_edittext'
    buttonSend = 'com.instagram.android:id/row_thread_composer_button_send'

    driver.find_element(By.ID, searchButton).click()
    driver.find_element(By.ID, searchBar).click()
    time.sleep(1)
    driver.find_element(By.ID, searchBar).send_keys("maul")
    time.sleep(2)

    if "maul" in driver.find_element(By.XPATH, akunMaul).text:
        driver.find_element(By.XPATH, akunMaul).click()
        time.sleep(2)
    else:
        raise Exception("Akun tidak ditemukan!!!")
    
    try:
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, fotoProfil)))
        print("Ketemu yahahahaha")
        time.sleep(2)
    except TimeoutException:
        raise Exception("Akun tidak ditemukan!!!")

    if driver.find_element(By.ID, followBack).text == "Follow Back":
        driver.find_element(By.ID, followBack).click()
        driver.find_element(By.ID, buttonMessage).click()
        time.sleep(2)
    elif driver.find_element(By.ID, followBack).text == "Following":
        driver.find_element(By.ID, buttonMessage).click()
        time.sleep(2)

    driver.find_element(By.ID, editMessage).click()
    driver.find_element(By.ID, editMessage).send_keys("Saya sudah follow back yaa")
    driver.find_element(By.ID, buttonSend).click()
    time.sleep(2)

    driver.close_app()


@pytest.mark.sendAttachFile
def test_send_attach():
    driver.implicitly_wait(10)

    buttonDm = 'com.instagram.android:id/action_bar_inbox_button' #ID
    searchbar = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.view.ViewGroup/android.widget.FrameLayout/android.widget.TextView' #XPATH
    searchbar2 = 'com.instagram.android:id/search_bar_real_field'
    elemenBesarDav = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.GridView/android.widget.LinearLayout[1]/android.widget.LinearLayout" #XPATH
    akun = '//android.widget.TextView[@content-desc="Dav"]' #XPATH
    buttonGaleri = 'com.instagram.android:id/row_thread_composer_button_gallery'    #ID
    memang = '//android.widget.CheckBox[@content-desc="Photo thumbnail, Added on 18 hours ago"]' #XPATH
    buttonSend2 = 'com.instagram.android:id/bb_primary_action_container' #ID
    iconMengirim = 'com.instagram.android:id/action_icon' #ID
    editMessage = 'com.instagram.android:id/row_thread_composer_edittext' #ID
    buttonSend = 'com.instagram.android:id/row_thread_composer_button_send' #ID

    driver.find_element(By.ID, buttonDm).click()
    driver.find_element(By.XPATH, searchbar).click()
    driver.find_element(By.ID, searchbar2).send_keys("dav")

    if driver.find_element(By.XPATH, akun).text == "Dav":
        driver.find_element(By.XPATH, akun).click()
    else:
        raise Exception("Akun tidak ditemukan !!!")
    
    driver.find_element(By.ID, buttonGaleri).click()
    driver.find_element(By.XPATH, memang).click()
    driver.find_element(By.ID, buttonSend2).click()

    try:
        WebDriverWait(driver, 5).until(EC.invisibility_of_element_located((By.ID, iconMengirim)))
    except TimeoutException:
        raise Exception("meme tidak terkirim :(")
    
    driver.find_element(By.ID, editMessage).send_keys("memenya sudah saya kirim :)")
    driver.find_element(By.ID, buttonSend).click()
    time.sleep(3)

    driver.close_app()


@pytest.mark.addStory
def test_add_story():
    driver.implicitly_wait(10)

    buttonLihat = '//androidx.recyclerview.widget.RecyclerView[@content-desc="reels_tray_container"]/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View' #XPATH
    buttonPlus = 'com.instagram.android:id/reel_viewer_profile_picture' #ID
    pilihanGambar = '(//android.view.View[@content-desc="Photo thumbnail"])[2]' #XPATH
    pilihan = 'com.instagram.android:id/overflow_button' #ID
    draw = '//android.widget.Button[@content-desc="Draw"]' #XPATH
    buttonDone = 'com.instagram.android:id/done_button' #ID
    shareToStory = '//android.widget.FrameLayout[@content-desc="Share to Your Story"]' #XPATH
    buttonCloseFriend = '//android.widget.FrameLayout[@content-desc="Close friends"]/android.widget.TextView' #XPATH
    logo = 'com.instagram.android:id/title_logo' #ID

    driver.find_element(By.XPATH, buttonLihat).click()
    driver.find_element(By.ID, buttonPlus).click()
    driver.find_element(By.XPATH, pilihanGambar).click()
    driver.find_element(By.ID, pilihan).click()
    driver.find_element(By.XPATH, draw).click()

    driver.swipe(800, 1800, 530, 600, 500)  # 800, 1800
    driver.swipe(530, 600, 200, 1800, 500)  # 530, 600
    driver.swipe(200, 1800, 800, 750, 500)  # 200, 1800
    driver.swipe(800, 750, 200, 750, 500)   # 800, 750
    driver.swipe(200, 750, 800, 1800, 500)  # 200, 750

    driver.find_element(By.ID, buttonDone).click()
    driver.find_element(By.XPATH, buttonCloseFriend).click()

    try:
        WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.ID, logo)))
        time.sleep(3)
    except TimeoutException:
        pass

    driver.close_app()

    









