#coding:utf-8
import sys
def get_max_int():
    return sys.maxsize

# class A(object):
#     def __setitem__(self, key, value):
#         print "開始設置"
#         self.key=value
#     def __getitem__(self, item):
#         print("開始獲取")
#         return self[item]
#     def __setattr__(self, key, value):
#         print "開始設置Attr"
#         self.key = value
#     def __getattr__(self, item):
#         print("開始獲取Attr")
#         return self[item]
# if __name__ == '__main__':
#     a=A()
#     a["c"]=6
#     print("over")

from appium import webdriver

descrip={}
descrip["deviceName"]="Android"
descrip["platformVersion"]="4.1.1"
descrip["platformName"]="Android"
descrip["udid"]="91QEBP74ZDHH"
descrip['appPackage'] = 'com.meizu.flyme.calculator'
descrip['appActivity'] = '.Calculator'
# descrip["app"]="E:\\Code\\ython3\\HeadFirstPython\\charpt01\\a.apk"
#远程电脑设置ip为本机实际ip,
driver = webdriver.Remote('http://192.168.3.229:4723/wd/hub', descrip)
driver.find_element_by_id("digit7").click()

driver.find_element_by_id("digit5").click()

driver.find_element_by_id("digit9").click()


driver.find_element_by_id("digit5").click()
# com.meizu.flyme.calculator:id/plus
driver.find_element_by_id("plus").click()

driver.find_element_by_id("digit5").click()

driver.find_element_by_id("eq").click()

driver.quit()

