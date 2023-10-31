from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import pytest
import time
import csv

desire_caps = {}

desire_caps['appPackage'] = "com.spotify.music"
desire_caps['appActivity'] = "com.spotify.music.MainActivity"
desire_caps['platformName'] = "Android"
desire_caps['udid'] = "emulator-5554"
desire_caps['noReset'] = True
desire_caps['autoGrantpermissions'] = True
desire_caps['forceAppLaunch'] = True

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_caps)

@pytest.mark.playlistUru
def test_playlist_uru():
    driver.implicitly_wait(10)

    shortcutUru = '//android.widget.TextView[@content-desc="Shortcut uru"]' #xpath
    soreo = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.GridView/android.view.ViewGroup[1]/android.widget.TextView[1]' #xpath
    playingBarContainer = 'com.spotify.music:id/now_playing_bar_container' #id
    playSoreo = '//androidx.recyclerview.widget.RecyclerView[@content-desc="Currently playing track"]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.TextView' #xpath
    # それを愛と呼ぶなら - From THE FIRST TAKE

    driver.find_element(By.XPATH, shortcutUru).click()
    driver.find_element(By.XPATH, soreo).click()

    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, playingBarContainer)))
        assert driver.find_element(By.XPATH, playSoreo).text == "それを愛と呼ぶなら - From THE FIRST TAKE"
    except TimeoutException:
        raise Exception("SALAH LAGU")
    
    time.sleep(20)
    driver.close_app()

@pytest.mark.cariLagu
def test_cari_lagu():
    driver.implicitly_wait(10)

    searchTab = 'com.spotify.music:id/search_tab' #id
    tombolInput = 'com.spotify.music:id/find_search_field_text' #id
    searchInput = 'com.spotify.music:id/query' #id
    thisIsBMTH = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.GridView/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.TextView' #xpath
    #swipe
    throne = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.GridView/android.view.ViewGroup[3]/android.widget.TextView[1]' #xpath
    playingBarContainer = 'com.spotify.music:id/now_playing_bar_container' #id
    song = '//androidx.recyclerview.widget.RecyclerView[@content-desc="Currently playing track"]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.TextView' #xpath
    
    driver.find_element(By.ID, searchTab).click()
    driver.find_element(By.ID, tombolInput).click()
    driver.find_element(By.ID, searchInput).send_keys("bring me the horizon")

    if driver.find_element(By.XPATH, thisIsBMTH).text == "This Is Bring Me The Horizon":
        driver.back()
        driver.find_element(By.XPATH, thisIsBMTH).click()
    else:
        raise Exception("Playlist tidak ditemukan")
    
    driver.swipe(720, 1960, 720, 1000, 500)

    if driver.find_element(By.XPATH, throne).text == "Throne":
        driver.find_element(By.XPATH, throne).click()
    else:
        raise Exception("Lagu tidak ditemukan")
    
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, playingBarContainer)))
        assert driver.find_element(By.XPATH, song).text == "Throne"
    except TimeoutException:
        raise Exception("SALAH LAGU")
    
    time.sleep(60)
    #driver.close_app()



