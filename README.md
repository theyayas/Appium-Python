# Appium-Python
Contains projects that were made for learning how to operate mobile automation testing using Appium Python

# How to Configure
1. Install Python at https://www.python.org/downloads/
2. Install Android Studio at https://developer.android.com/studio
3. Open android studio, go to more actions > SDK Manager > SDK Tool > check these packages, then click Apply. This will automatically install these packages:
   - Android SDK Build-Tools 34
   - Android SDK Command-line Tool (latest)
   - Android Emulator
   - Android Emulator hypervisor driver (installer)
   - Android SDK Platform-Tools
   - Google USB Tools
4. In the same menu, go to SDK Platforms tab, check the Android Version Packages you desire, then click Apply. This will also automatically install the packages
5. Copy the Android SDK Location, then add it to The System Environment Variables in your PC (this is crucial for the Appium Server)
   To make sure that the Android SDK has been added to the System Environment Variables, open Command Prompt, type "adb", then hit Enter
   This will show ADB version, then you're good to go
6. Test the connection of your Android Phone with your PC via USB (don't forget to allow USB debugging) by typing "adb devices" in Command Prompt
   This will show the list of devices attached, and again you're good to go
7. To install the app you can do it using Command Prompt by typing "adb install 'path of the apk in your pc'" (optional)
8. Install JDK at https://www.oracle.com/id/java/technologies/downloads/
9. Install Appium at https://github.com/appium/appium-desktop/releases/
10. Install Appium Inspector https://github.com/appium/appium-inspector/releases
11. Open Command Prompt, type "pip install appium", then hit Enter

--- To test the app on your mobile you should do the following ---
1. Connect your mobile via USB
2. Open the app
3. Open Command Prompt, type "adb shell dumpsys window windows", then hit Enter
4. Copy the App Package dan App Activity
5. Open Command Prompt, type "adb devices", then hit Enter
6. Copy the serial number that pops up
7. Open Appium, then Start Server
8. Go to Appium Inspector then fill the JSON Representation with this
   {
     "appium:appPackage": "*copied App Package*",
     "appium:appActivity": "*copied App Activity*",
     "appium:platformName": "Android",
     "appium:deviceName": "*your device name*",
     "appium:udid": "*copied Serial Number*",
     "appium:noReset": true,
     "appium:autoGrantPermissions": true,
     "appium:forceAppLaunch": true
   }

--- if you have problems while trying to start a session ---
1. Go to Appium Server GUI -> Advanced, then set:
   - Server address: localhost
   - Port: 4723
   - Allow CORP: yes
2. Start Appium Server
3. Go to Appium Inspector, then set:
   - Remote host: localhost
   - Port: 4723
   - Path: /wd/hub
   - Allow Unauthorized Certificates
   - Select your capabilities
4. Start Appium Inspector Server
   
or

Stop the appium server and execute this:
   - adb uninstall io.appium.uiautomator2.server
   - adb uninstall io.appium.uiautomator2.server.test

