from appium import webdriver
import time
caps = {}
caps["appPackage"] = "com.kmxs.reader"
caps["appActivity"] = "com.kmxs.reader.home.ui.HomeActivity"
caps["platformName"] = "Android"
caps["platformVersion"] = '9'
caps["deviceName"] = '3HX0217115011233'
caps["unicodeKeyboard"] = True
caps["autoAcceptAlerts"] = True #对权限弹窗进行授权
caps["resetKeyboard"] = True
caps["noReset"] = True
caps["newCommandTimeout"]=6000

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

#获取手机大小 {'width': 720, 'height': 1280}
size = driver.get_window_size()
print(size)

print(driver.is_app_installed("com.kmxs.reader"))

me = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout[5]/android.view.ViewGroup/android.widget.ImageView")
me.click()
time.sleep(1)

# 点击登录按钮
driver.find_element_by_id("com.kmxs.reader:id/tourist_login").click()

driver.find_element_by_id("com.kmxs.reader:id/login_msg_phone_et").click()
driver.find_element_by_id("com.kmxs.reader:id/login_msg_phone_et").send_keys("18712345678")
time.sleep(1)

driver.find_element_by_id("com.kmxs.reader:id/tb_navi_back").click()

book = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.ImageView")
book.click()
time.sleep(2)

driver.find_element_by_id("com.kmxs.reader:id/tv_banner_text").click()
time.sleep(1)

driver.find_element_by_id("com.kmxs.reader:id/search_text_hint").send_keys("流浪地球")
driver.find_element_by_id("com.kmxs.reader:id/search_tv").click()

#关闭app
driver.close_app()


