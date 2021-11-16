import time

from appium.webdriver.common.touch_action import TouchAction

from base.baseDriver import BaseDriver


class Swipe(object):
    def __init__(self, driver):
        self.driver = driver

    def siwpe_page(self, dir='up', duration=3000):
        """
        向下滑动 x 不变 top-bottom 大
        向上滑动 x 不变 bottom-top 小
        向左滑动 y 不变 right-left 变小
        向右滑动 y 不变 left-right 变大
        duration决定惯性 时间越大（速度越慢） 惯性越小 时间越小（速度越快） 惯性越大
        :param dir: up 向上划
        :param duration:
        :return:
        """
        # 获取屏幕的分辨率{width：，height}
        screen = self.driver.get_window_size()
        screen_width = screen['width']
        screen_height = screen['height']
        # 固定不变的x和y轴的值
        x = screen_width*0.5
        y = screen_height*0.5
        # 距离顶部的y轴
        top_y = screen_height*0.2
        # 距离底部的y轴
        buttom_y = screen_height*0.75
        # 距离左边的x轴
        lefg_x = screen_width*0.25
        # 距离右边的x轴
        right_x = screen_width*0.75

        if dir == 'up':
            self.driver.swipe(x, buttom_y, x, top_y, duration)
        elif dir == 'down':
            self.driver.swipe(x, top_y, x, buttom_y, duration)
        elif dir == 'left':
            self.driver.swipe(right_x, y, lefg_x, y, duration)
        elif dir == 'right':
            self.driver.swipe(lefg_x, y, right_x, y, duration)
        else:
            raise Exception('请输入正确的滑动方向，比如up/down/left/right')

    def swipe_and_find_element(self, loc, dir='up'):
        """
        思路：
        如果找不到就一直滑动---滑动次数（没有办法确定范围）---while True  ----退出条件
        正确找到元素的退出条件：能找到元素就不会报错（try.....except.....）
        没有找到元素的退出条件:except:证明没有找到元素，屏幕的高度是固定的（滑倒底部该退出）
        判断滑到底部，old_page_source == now_page_source 证明滑倒了底部
        loc:定位元素的方式
        :return: 找到的元素
        """
        while True:
            try:
                # 查找元素
                return self.driver.find_element(*loc)
            except:
                # 没有找到元素 要记录滑动之前的页面
                old_page_source = self.driver.page_source
                # 继续滑动
                self.siwpe_page(dir)
                # 判断一下是否滑倒了底部
                if old_page_source == self.driver.page_source:
                    # 证明滑到了底部
                    raise Exception('滑倒了底部，请检查传入的元素的定位方式')

    def el_swipe(self, el, n, dir):
        """
        单元素的滑动   location - size  获取滑动点的x，y值
        :param el: 对哪个元素进行操作
        :param n:  目标-当前的值=n次
        :param dir: 方向
        :return:
        """
        # 1、获取元素的宽高
        el_size = el.size
        el_width = el_size['width']
        el_height = el_size['height']
        # 2、获取元素的x、y轴的坐标
        el_location = el.location
        el_x = el_location['x']
        el_y = el_location['y']
        # 3、找到滑动点(可以写死指针坐标/动态获取）
        swipe_x = int(el_x+el_width*0.5)
        swipe_y_up_top = int(el_y*0.7)
        swipe_y_up_buttom = int(el_y+el_height*0.9)
        # 向下滑动的x，y轴
        swipe_y_down_top = int(el_y+el_height*0.6)
        swipe_y_down_buttom = int(el_y+el_height+el_height*0.8)
        if dir == 'up':
            print('向上滑动，y值在变小')
            for i in range(n):
                # 只滑动一次 duration时间长，惯性越小，就越稳定
                self.driver.swipe(swipe_x, swipe_y_up_buttom, swipe_x, swipe_y_up_top, 10000)
                # 循环里面 --滑动一次稍微停一下
                time.sleep(2)
        elif dir == 'down':
            print('向下滑动，y值在变大')
            for i in range(n):
                # 只滑动一次 duration时间长，惯性越小，就越稳定
                self.driver.swipe(swipe_x, swipe_y_down_top, swipe_x, swipe_y_down_buttom, 10000)
                # 循环里面 --滑动一次稍微停一下
                time.sleep(2)
        else:
            raise Exception


if __name__ == '__main__':
    # com.android.settings /.Settings
    # 选择锁屏的图案的包名和界面名：com.android.settings/.ChooseLockPattern
    driver = BaseDriver().start_driver(appPackage='com.android.settings', appActivity='.Settings')
    # # Swipe(driver).siwpe_page(dir='up')
    # loc = By.XPATH, '//*[@text="关于平板电脑"]'
    # el = Swipe(driver).swipe_and_find_element(loc)
    # el.click()
    # # tap 敲 tap（元素/坐标）  优势是后面能跟着坐标  特殊情况用：如click无效了，用tap
    # tap_x = int((108+270)*0.5)
    # tap_y = int((1194+1231)*0.5)
    # # 第一种tap写法
    # # TouchAction(driver).tap(el, tap_x, tap_y).perform()
    # # 第二种tap写法
    # TouchAction(driver).tap(x=tap_x, y=tap_y).perform()
    # bounds 属性指的是左上角和右下角的坐标
    # TouchAction执行的操作，需要perform一下才能生效，代码比较底层，需要的步骤多一点
    # 对元素压住
    TouchAction(driver).press(x=359, y=490).wait(10).move_to(x=354, y=647).move_to(x=354, y=803).move_to(x=513, y=203).release().perform()
