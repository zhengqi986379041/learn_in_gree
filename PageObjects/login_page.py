from PageLocators.loginPage_locators import LoginPageLocator as loc
from Common.basePage import BasePage
import time


class LoginPage(BasePage):
    """
    登录页面
    """
    def login(self, username, passwd):
        """
        登录操作
        :param username: 用户名
        :param passwd: 密码
        :return: None
        """
        doc = "登录页面_登录功能_登录操作"
        self.wait_eleVisible(loc.passwd_login_style, doc=doc)
        time.sleep(1)
        try:
            self.get_element(loc.remember_passwd, doc=doc)
            self.clear_text(loc.name_text, doc=doc)
            self.input_text(loc.name_text, username, doc=doc)
            self.clear_text(loc.passwd_text, doc=doc)
            self.input_text(loc.passwd_text, passwd, doc=doc)
            self.click_element(loc.login_button, doc=doc)

        except:
            self.click_element(loc.passwd_login_style, doc=doc)
            self.clear_text(loc.name_text, doc=doc)
            self.input_text(loc.name_text, username, doc=doc)
            self.clear_text(loc.passwd_text, doc=doc)
            self.input_text(loc.passwd_text, passwd, doc=doc)
            self.click_element(loc.login_button, doc=doc)

    # 注册入口
    def register(self):
        doc = "登录页面_注册入口"
        self.wait_eleVisible(loc.register_enter, doc=doc)
        self.click_element(loc.register_enter, doc)

    # 异常提示
    def get_errorMsg_from_loginArea(self):
        doc = "登录页面_登录功能_异常登录"
        self.wait_eleVisible(loc.errorMsg_from_loginArea, doc=doc)
        return self.get_text(loc.errorMsg_from_loginArea, doc)