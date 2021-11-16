import time

import pytest

from base.baseDriver import BaseDriver


@pytest.fixture(scope='function')
def getdriver():
    """
    目的是为了引入driver
    :return:
    """
    driver = BaseDriver.start_driver(appPackage='com.douban.frodo', appActivity='.activity.SplashActivity',)
    yield driver
    time.sleep(3)
    driver.quit()
