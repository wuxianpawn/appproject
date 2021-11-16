from appium import webdriver


class BaseDriver():
    @staticmethod
    def start_driver(appPackage, appActivity):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        # 写不写都可以，但是写就必须写对
        desired_caps['platformVersion'] = '7'
        desired_caps['deviceName'] = '127.0.0.1:21503'
        desired_caps['appPackage'] = appPackage
        desired_caps['appActivity'] = appActivity
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        # 连接远程appium服务
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        driver.implicitly_wait(10)
        return driver


if __name__ == '__main__':
    driver = BaseDriver().start_driver(appPackage='com.douban.frodo', appActivity='com.douban.frodo.activity.SplashActivity')
    driver.find_element_by_id().click()
    driver.find_element_by_android_uiautomator()