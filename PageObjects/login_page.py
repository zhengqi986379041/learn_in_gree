from PageLocators.loginPage_locators import LoginPageLocator as loc
from Common.basePage import BasePage
import time
from Common.do_mysql import DoMysql as SQL


class LoginPage(BasePage):
    """
    登录页面
    """
    def error_login(self, username, passwd):
        doc = '登录页面_登录功能_异常登录'
        try:
            self.wait_eleVisible(loc.password_login_button, wait_times = 3, doc=doc)
            time.sleep(1)
            self.click_element(loc.password_login_button, doc=doc)
            time.sleep(1)
        except:
            pass
        self.clear_text(loc.user_name, doc=doc)
        self.clear_text(loc.pass_word, doc=doc)
        self.input_text(loc.user_name, username, doc=doc)
        self.input_text(loc.pass_word, passwd, doc=doc)
        self.click_element(loc.login_button, doc=doc)
    def check_toast(self,check):
        doc = '登录页面_登录功能_异常登录_check'
        self.wait_eleVisible(loc.error_login_toast, doc=doc)
        try:
            if self.get_text(loc.error_login_toast, doc=doc) == check:
                return True
        except:
            return False


    def password_login(self, username, passwd):
        """
        登录操作
        :param username: 用户名
        :param passwd: 密码
        :return: None
        """
        doc = '登录页面_登录功能_正确登录'
        self.wait_eleVisible(loc.password_login_button, doc=doc)
        time.sleep(1)
        self.click_element(loc.password_login_button, doc=doc)
        self.input_text(loc.user_name, username, doc=doc)
        self.input_text(loc.pass_word, passwd, doc=doc)
        self.click_element(loc.login_button, doc=doc)

    def register(self,username):
        '''
        注册登录
        :param username: 手机号
        :return:
        '''
        doc = '登录页面_注册功能_验证码注册'
        self.wait_eleVisible(loc.phone_name,doc=doc)
        self.input_text(loc.phone_name,username,doc=doc)
        self.click_element(loc.code_login_button,doc=doc)
        self.wait_eleVisible(loc.yi,doc=doc)
        number = {'1':loc.yi,
                  '2':loc.er,
                  '3':loc.san,
                  '4':loc.si,
                  '5':loc.wu,
                  '6':loc.liu,
                  '7':loc.qi,
                  '8':loc.ba,
                  '9':loc.jiu,
                  '0':loc.ling
                  }
        sql = 'SELECT * FROM basecenter.base_send_message where address = "{0}" order by id desc limit 1;'.format(username)
        code_list = list(SQL.query(sql))
        time.sleep(5)
        for number_code in code_list:
            self.click_element(number[number_code])