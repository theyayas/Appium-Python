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

desire_caps['appPackage'] = "com.instagram.android"
desire_caps['appActivity'] = "com.instagram.mainactivity.InstagramMainActivity"
desire_caps['platformName'] = "Android"
desire_caps['udid'] = "emulator-5554" # RR8R7027AZH, emulator-5554
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
    driver.implicitly_wait(10)

    nonOfTheAbove = '//android.widget.LinearLayout[@content-desc="Choose a Credential"]/android.widget.LinearLayout/android.widget.Button'
    username = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText'
    password = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText'
    login = '//android.widget.Button[@content-desc="Log in"]'
    logo = '//android.widget.ImageView[@content-desc="Instagram from Meta"]'

    '''try:
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, nonOfTheAbove)))
        driver.find_element(By.XPATH, nonOfTheAbove).click()
        time.sleep(1)
        driver.back()
    except TimeoutException:
        pass'''

    try:
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, logo)))
        time.sleep(1)
        driver.find_element(By.XPATH, username).send_keys("yahahahaha@gmail.com")
        time.sleep(1)
    except TimeoutException:
        pass

    driver.find_element(By.XPATH, password).send_keys("yahahahaha")
    driver.find_element(By.XPATH, login).click() #534 1297

    time.sleep(80)
    driver.close_app()

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
    driver.implicitly_wait(20)

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
    driver.swipe(200, 1800, 800, 1000, 500) # 200, 1800
    driver.swipe(800, 1000, 200, 1000, 500) # 800, 750
    driver.swipe(200, 1000, 800, 1800, 500) # 200, 750

    driver.find_element(By.ID, buttonDone).click()
    driver.find_element(By.XPATH, buttonCloseFriend).click()

    try:
        WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.ID, logo)))
        time.sleep(3)
    except TimeoutException:
        pass

    driver.close_app()

@pytest.mark.sendAPost
def test_send_a_post():
    driver.implicitly_wait(10)

    searchTab = 'com.instagram.android:id/search_tab' #id
    postEmpat = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[4]' #xpath
    share = 'com.instagram.android:id/row_feed_button_share' #id
    editText = 'com.instagram.android:id/search_edit_text' #id
    akun = '//android.widget.TextView[@content-desc="Dav"]' #xpath
    writeMessage = 'com.instagram.android:id/direct_private_share_message_box' #id
    buttonSend = 'com.instagram.android:id/direct_send_button_multi_select' #id
    homeTab = 'com.instagram.android:id/feed_tab' #id
    buttonDm = 'com.instagram.android:id/action_bar_inbox_button' #id
    pesanterkirim = '//android.widget.TextView[@content-desc="coba liat ini lucu deh awokawokawokaoakw !!!"]' #xpath

    driver.find_element(By.ID, searchTab).click()
    driver.find_element(By.XPATH, postEmpat).click()
    driver.find_element(By.ID, share).click()
    driver.find_element(By.ID, editText).send_keys("dav")
    driver.find_element(By.XPATH, akun).click()
    driver.find_element(By.ID, writeMessage).send_keys("coba liat ini lucu deh awokawokawokaoakw !!!")
    driver.find_element(By.ID, buttonSend).click()
    driver.find_element(By.ID, homeTab).click()
    driver.find_element(By.ID, buttonDm).click()

    if driver.find_element(By.XPATH, akun).text == "Dav":
        driver.find_element(By.XPATH, akun).click()
    else:
        raise Exception("Akun tidak ditemukan !!!")
    
    assert driver.find_element(By.XPATH, pesanterkirim).text == "coba liat ini lucu deh awokawokawokaoakw !!!"
    time.sleep(2)
    driver.close_app()

@pytest.mark.ngespam
def test_data_binding():
    driver.implicitly_wait(10)

    buttonDm = 'com.instagram.android:id/action_bar_inbox_button' #ID
    searchbar = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.view.ViewGroup/android.widget.FrameLayout/android.widget.TextView' #XPATH
    searchbar2 = 'com.instagram.android:id/search_bar_real_field'
    akun = '//android.widget.TextView[@content-desc="Maul"]' #XPATH
    editMessage = 'com.instagram.android:id/row_thread_composer_edittext' #ID
    buttonSend = 'com.instagram.android:id/row_thread_composer_button_send' #ID
    buttonRecord = 'com.instagram.android:id/row_thread_composer_voice' #id
    iconMengirim = 'com.instagram.android:id/action_icon' #ID

    driver.find_element(By.ID, buttonDm).click()
    driver.find_element(By.XPATH, searchbar).click()
    driver.find_element(By.ID, searchbar2).send_keys("maul")

    if driver.find_element(By.XPATH, akun).text == "Maul":
        driver.find_element(By.XPATH, akun).click()
    else:
        raise Exception("Akun tidak ditemukan !!!")    

    with open('email-password-recovery-code.csv') as fileKita:
        reader = csv.reader(fileKita, delimiter = ',')  #csv.DictReader = membuat baris pertama pada file menjadi keyword setiap data (nama, alamat, dsb)
        for baris in reader:
            driver.find_element(By.ID, editMessage).send_keys("Nama : ", baris[4], " ", baris[5], "\n", 
                                                              "ID : ", baris[1], "\n",
                                                              "Departemen : ", baris[6], "\n",
                                                              "Email : ", baris[0], "\n",
                                                              "One-time Password : ", baris[2], "\n",
                                                              "Recovery Code : ", baris[3], "\n",
                                                              "Lokasi : ", baris[7])
            '''driver.find_element(By.ID, editMessage).send_keys("ID : ", baris[1])
            driver.find_element(By.ID, editMessage).send_keys("Departemen : ", baris[6])
            driver.find_element(By.ID, editMessage).send_keys("Email : ", baris[0])
            driver.find_element(By.ID, editMessage).send_keys("One-time Password : ", baris[2])
            driver.find_element(By.ID, editMessage).send_keys("Recovery Code : ", baris[3])
            driver.find_element(By.ID, editMessage).send_keys("Lokasi : ", baris[7])'''
            driver.find_element(By.ID, buttonSend).click()
    
    TouchAction(driver).long_press(driver.find_element(By.ID, buttonRecord), duration = 5000).release().perform()
    
    time.sleep(5)
    driver.close_app()


@pytest.mark.kirimDMVideo
def test_kirim_dm_video():
    driver.implicitly_wait(10)

    buttonDm = 'com.instagram.android:id/action_bar_inbox_button' #ID
    searchbar = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.view.ViewGroup/android.widget.FrameLayout/android.widget.TextView' #XPATH
    searchbar2 = 'com.instagram.android:id/search_bar_real_field'
    akun = '//android.widget.TextView[@content-desc="Maul"]' #XPATH
    buttonCamera = 'com.instagram.android:id/row_thread_composer_button_camera' #id
    # swipe 400,2500 -> 715,2500
    shutter = 'com.instagram.android:id/camera_shutter_button_inner_container' #id
    buttonSendDirect = 'com.instagram.android:id/direct_reply_avatar_button_toggle_container' #id
    iconMengirim = 'com.instagram.android:id/action_icon' #ID

    driver.find_element(By.ID, buttonDm).click()
    driver.find_element(By.XPATH, searchbar).click()
    driver.find_element(By.ID, searchbar2).send_keys("maul")

    if driver.find_element(By.XPATH, akun).text == "Maul":
        driver.find_element(By.XPATH, akun).click()
    else:
        raise Exception("Akun tidak ditemukan !!!")

    driver.find_element(By.ID, buttonCamera).click()
    time.sleep(3)
    driver.swipe(400, 2500, 715, 2500, 500) 
    TouchAction(driver).long_press(driver.find_element(By.ID, shutter), duration = 5000).release().perform()
    driver.find_element(By.ID, buttonSendDirect).click()
    
    try:
        WebDriverWait(driver, 60).until(EC.invisibility_of_element_located((By.ID, iconMengirim)))
        time.sleep(3)
        driver.close_app()
    except TimeoutException:
        raise Exception("video tidak terkirim :(")
    
@pytest.mark.zoomFoto
def test_zoom_foto():
    driver.implicitly_wait(10)

    buttonDm = 'com.instagram.android:id/action_bar_inbox_button' #ID
    searchbar = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.view.ViewGroup/android.widget.FrameLayout/android.widget.TextView' #XPATH
    searchbar2 = 'com.instagram.android:id/search_bar_real_field'
    akun = '//android.widget.TextView[@content-desc="Maul"]' #XPATH
    buttonCamera = 'com.instagram.android:id/row_thread_composer_button_camera' #id
    gambar1 = '(//android.view.View[@content-desc="Photo thumbnail"])[2]' #xpath
    previewGambar = 'com.instagram.android:id/focus_view' #id
    buttonSendDirect = 'com.instagram.android:id/direct_reply_avatar_button_toggle_container' #id
    iconMengirim = 'com.instagram.android:id/action_icon' #ID
    
    driver.find_element(By.ID, buttonDm).click()
    driver.find_element(By.XPATH, searchbar).click()
    driver.find_element(By.ID, searchbar2).send_keys("maul")

    if driver.find_element(By.XPATH, akun).text == "Maul":
        driver.find_element(By.XPATH, akun).click()
    else:
        raise Exception("Akun tidak ditemukan !!!")

    driver.find_element(By.ID, buttonCamera).click()
    time.sleep(3)

    driver.swipe(715, 2100, 715, 1300, 500)
    #TouchAction(driver).long_press(None, 715, 2100).move_to(None, 715, 1300).release().perform()
    
    driver.find_element(By.XPATH, gambar1).click()
    time.sleep(3)

    # Penggunaan MultiAction untuk melakukan zoom in
    a1 = TouchAction(driver).long_press(driver.find_element(By.ID, previewGambar), 715, 1300).move_to(driver.find_element(By.ID, previewGambar), 715, 1000).release()
    a2 = TouchAction(driver).long_press(driver.find_element(By.ID, previewGambar), 715, 1300).move_to(driver.find_element(By.ID, previewGambar), 715, 1600).release()

    #MultiAction(driver).add(touch1, touch2).
    #MultiAction(driver).add(touch1.perform(), touch2.release())

    zoom = MultiAction(driver)
    zoom.add(a1)
    zoom.add(a2)
    zoom.perform()

    time.sleep(3) 

    driver.find_element(By.ID, buttonSendDirect).click()
    
    try:
        WebDriverWait(driver, 60).until(EC.invisibility_of_element_located((By.ID, iconMengirim)))
        time.sleep(2)
        driver.close_app()
    except TimeoutException:
        raise Exception("gambar tidak terkirim :(")

    driver.quit()



    









