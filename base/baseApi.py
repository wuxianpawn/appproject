"""
logger 正常的描述 一般是logger.info（）
异常处理  logger.error()
"""
from tools.inihelper import IniHelper
from tools.logger import GetLogger
logger = GetLogger().get_logger()


class Base(object):
    def __init__(self, driver):
        # driver引用
        self.driver = driver
        self.source = IniHelper

    def base_find_element(self, loc):
        """
        loc = xpath=>//android.widget.TextView[@text='我的'],是一个字符串类型
        :param loc:
        :return: 定位到的元素
        """
        element = ''
        # 对loc的字符串进行切割
        ele_type = loc.split('=>')[0]
        value = loc.split('=>')[1]
        # 做下判断
        if ele_type == '' or ele_type == '':
            logger.error('grammatical error,eg:"id=>name"')
            raise NameError('grammatical error,eg:"id=>name"')
        if ele_type == 'id':
            try:
                element = self.driver.find_element_by_id(value)
                logger.info('had find element{},by{},value{}'.format(element.text, ele_type, value))
            except Exception as e:
                logger.error('定位方式有误：%s' % e)
        elif ele_type == 'name':
            try:
                element = self.driver.find_element_by_name(value)
                logger.info('had find element{},by{},value{}'.format(element.text, ele_type, value))
            except Exception as e:
                logger.error('定位方式有误：%s' % e)
        elif ele_type == 'xpath':
            try:
                element = self.driver.find_element_by_xpath(value)
                logger.info('had find element{},by{},value{}'.format(element.text, ele_type, value))
            except Exception as e:
                logger.error('定位方式有误：%s' % e)
        elif ele_type == 'link':
            try:
                element = self.driver.find_element_by_link_text(value)
                logger.info('had find element{},by{},value{}'.format(element.text, ele_type, value))
            except Exception as e:
                logger.error('定位方式有误：%s' % e)
        elif ele_type == 'class':
            try:
                element = self.driver.find_element_by_class_name(value)
                logger.info('had find element{},by{},value{}'.format(element.text, ele_type, value))
            except Exception as e:
                logger.error('定位方式有误：%s' % e)
        elif ele_type == 'p_link':
            try:
                element = self.driver.find_element_by_partial_link_text(value)
                logger.info('had find element{},by{},value{}'.format(element.text, ele_type, value))
            except Exception as e:
                logger.error('定位方式有误：%s' % e)
        elif ele_type == 'android_uiautomator':
            try:
                element = self.driver.find_element_by_android_uiautomator(value)
                logger.info('had find element{},by{},value{}'.format(element.text, ele_type, value))
            except Exception as e:
                logger.error('定位方式有误：%s' % e)
        else:
            logger.error('NoSuchElementTypeException:%s' % ele_type)
            raise NameError('please enter correct type:id,name,xpath,link_text,class,link_text,android_uiautomator')
        return element

    def base_click(self, loc):
        """
        点击
        :param loc:
        :return:
        """
        el = self.base_find_element(loc)
        el.click()

    def base_input(self, loc, value):
        """
        输入
        :param loc:
        :param value:
        :return:
        """
        el = self.base_find_element(loc)
        el.clear()
        el.send_keys(value)

    @property
    def base_paage_source(self):
        return self.driver.page_source()


if __name__ == '__main__':
    pass
