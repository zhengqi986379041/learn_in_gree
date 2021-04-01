import sys, os
sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))
from selenium import webdriver
from TestDatas import Common_Datas as CD
import pytest
from PageObjects.login_page import LoginPage
from PageObjects.index_page import IndexPage
driver = None
# 声明它是一个fixture
@pytest.fixture(scope="class")
def access_web():
    # 前置操作
    global driver
    mobileEmulation = {'deviceName': 'iPhone X'}
    options = webdriver.ChromeOptions()
    options.add_experimental_option('mobileEmulation', mobileEmulation)
    # 以下两行：关闭显示“chrome正受到自动测试软件的控制”
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    driver = webdriver.Chrome(executable_path = 'D:\path\chromedriver.exe',chrome_options=options)
    driver.get(CD.web_password_login_url)
    lg = LoginPage(driver)
    yield (driver, lg) # 可以将这两个参数传出去，类似于return
    # 后置操作
    driver.quit()

@pytest.fixture(scope="class")
def access_to_order():
    global driver
    mobileEmulation = {'deviceName': 'iPhone X'}
    options = webdriver.ChromeOptions()
    options.add_experimental_option('mobileEmulation', mobileEmulation)
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(CD.web_index_url)
    index = IndexPage(driver)
    yield (driver, index)
    driver.quit()

def refresh_page():
    global driver
    # 前置条件
    yield
    # 后置操作
