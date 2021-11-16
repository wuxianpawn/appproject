from pageAction.actionManager import ActionManager


class Login(ActionManager):
    # 成功登录的业务---作为其他业务的依赖
    def login_success(self):
        self.pagecover.click_passworld_login()
        self.pagelogin.input_username('15920179959')
        self.pagelogin.input_password('abc7757526@')
        # 点击登录
        self.pagelogin.click_login_button()

    # 登录业务---主要测试登录的功能
    def login_business(self, username, password):
        self.pagecover.click_passworld_login()
        self.pagelogin.input_username(username)
        self.pagelogin.input_password(password)
        # 点击登录按钮
        self.pagelogin.click_login_button()

    # 断言 点击我的 判断昵称是否在页面源码里面
    def after_login_click_me(self):
        """
        主要为做断言
        :return:
        """
        self.pageindex.click_mybutton()
