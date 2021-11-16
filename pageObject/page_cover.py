"""
文件是封面
"""
from base.baseApi import Base


class PageCover(Base):
    # 点击账号密码登录
    def click_passworld_login(self):
        self.base_click(self.source.get_value('doubanLogin.ini', 'Button', '帐号密码登录'))
