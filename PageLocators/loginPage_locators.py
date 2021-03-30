from selenium.webdriver.common.by import By


class LoginPageLocator:
    """
    登录页面
    """
    # 切换账号密码登录
    passwd_login_style = (By.XPATH, '/html/body/div/div[1]/div/div[1]/div[2]/div[2]')
    # 账号输入框
    name_text = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div[3]/div/div[1]/div/input')
    # 密码输入框
    passwd_text = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div[3]/div/div[2]/div/input')
    # 登录按钮
    login_button = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div[3]/div/p[1]')
    # 错误提示
    errorMsg_from_loginArea = (By.XPATH, '//div[@class="van-toast__text"]')
    # 注册入口
    register_enter = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div[3]/div/a')
    # 记住密码
    remember_passwd = (By.XPATH, '/html/body/div/div[1]/div/div[1]/div[3]/div/div[3]/label')



    # # 切换账号密码登录
    # passwd_login_style = (By.XPATH, '/html/body/div[1]/div/div[3]/span/a[1]')
    # # 账号输入框
    # name_text = (By.XPATH, '/html/body/div[1]/div[3]/div/div[1]/form/ul/li[2]/input')
    # # 密码输入框
    # passwd_text = (By.XPATH, '/html/body/div[1]/div[3]/div/div[1]/form/ul/li[3]/input')
    # # 登录按钮
    # login_button = (By.XPATH, '/html/body/div[1]/div[3]/div/div[1]/form/ul/li[5]/button')
    # # 错误提示
    # errorMsg_from_loginArea = (By.XPATH, '//div[@class="van-toast__text"]')
    # # 注册入口
    # register_enter = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div[3]/div/a')
