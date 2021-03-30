from PageObjects.index_page import IndexPage
from TestDatas import login_datas as LD
import pytest


# @pytest.mark.demo
@pytest.mark.usefixtures("access_web")
# @pytest.mark.usefixtures("refresh_page")
class TestLogin:

    # @classmethod
    # def setUpClass(cls):
    #     # 通过Excel读取本功能当中需要的所有测试数据
    #     # 一个测试类执行一次
    #     mobileEmulation = {'deviceName': 'iPhone X'}
    #     options = webdriver.ChromeOptions()
    #     options.add_experimental_option('mobileEmulation', mobileEmulation)
    #     cls.driver = webdriver.Chrome(chrome_options=options)
    #     # self.driver = webdriver.Chrome()
    #     cls.driver.get(CD.web_login_url)
    #     cls.lg = LoginPage(cls.driver)
    #
    # @classmethod
    # def tearDownClass(cls):
    #     # 一个测试类执行一次 比如打开关闭浏览器，当多个测试用例不需要关闭浏览器继续执行时使用
    #     cls.driver.quit()

    # def setUp(self):
    #     # 每个用例执行一遍
    #     mobileEmulation = {'deviceName': 'iPhone X'}
    #     options = webdriver.ChromeOptions()
    #     options.add_experimental_option('mobileEmulation', mobileEmulation)
    #     self.driver = webdriver.Chrome(chrome_options=options)
    #     # self.driver = webdriver.Chrome()
    #     self.driver.get(CD.web_login_url)
    #     self.lg = LoginPage(self.driver)
    #
    # def tearDown(self):
    #     self.driver.quit()


    # # @ddt.data(*LD.phone_data)
    # @pytest.mark.parametrize("data", LD.phone_data)
    # def test_login_0_fail(self, data, access_web):
    #     access_web[1].login(data['user'], data['passwd'])
    #     assert access_web[1].get_errorMsg_from_loginArea() == data['check']
    #     # self.assertEqual(self.lg.get_errorMsg_from_loginArea(), data['check'])

    @pytest.mark.parametrize("data", LD.phone_data)
    def test_login_0_fail(self, data, access_web):
        access_web[1].login(data['user'], data['passwd'])
        assert access_web[1].get_errorMsg_from_loginArea() == data['check']

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", LD.success_data)
    def test_login_1_sucess(self, data, access_web): # 直接输入conftest里面用到的函数名，传参过来，根据角标调用
        access_web[1].login(data['user'], data['passwd'])
        assert IndexPage(access_web[0]).isExist_logout_ele()

