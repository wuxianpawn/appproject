from pageObject.page_cover import PageCover
from pageObject.page_index import PageIndex
from pageObject.page_login import PageLogin


class ActionManager(object):
    def __init__(self, driver):
        self.pagecover = PageCover(driver)
        self.pagelogin = PageLogin(driver)
        self.pageindex = PageIndex(driver)