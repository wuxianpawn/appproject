from base.baseApi import Base


class PageIndex(Base):
    # 点击我的按钮
    def click_mybutton(self):
        self.base_click(self.source.get_value('doubanLogin.ini', 'Button', '我的'))
