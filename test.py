from appium import webdriver
from Util.GetDesiredcaps import getDesiredcaps
from Action.PageAction import *
from Util.ObjectMap import *


open_app()

xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout[5]/android.view.ViewGroup/android.widget.ImageView"
click("xpath", xpath)

click("id","com.kmxs.reader:id/tourist_login")

click("id", "com.kmxs.reader:id/login_msg_phone_et")
input_string("id", "com.kmxs.reader:id/login_msg_phone_et", "18712345678")

sleep(2)
click("id", "com.kmxs.reader:id/tb_navi_back")

click("xpath", "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.ImageView")
sleep(1)
click("id", "com.kmxs.reader:id/tv_banner_text")

input_string("id", "com.kmxs.reader:id/search_text_hint", "凡人修仙传")
sleep(1)
click("id", "com.kmxs.reader:id/search_tv")