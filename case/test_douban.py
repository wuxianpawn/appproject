# 0.导包
import time
from pageAction.login_action import Login


def test_login(getdriver):
    # todo 想办法搞一个driver出来
    # 方法一：导自己写的模块，前提是derive已经封装好，setup里引用，teardown退出driver； 方法二：fixture函数进行引用
    # driver就是getdriver的返回值
    driver = getdriver
    login = Login(driver)
    # 成功登录
    login.login_success()
    time.sleep(1)
    # 点击我的
    login.after_login_click_me()
    time.sleep(5)
    assert 'pawn' in driver.page_source

