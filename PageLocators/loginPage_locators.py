from selenium.webdriver.common.by import By


class LoginPageLocator:
    """
    登录页面
    """
    # # 切换账号密码登录
    # passwd_login_style = (By.XPATH, '/html/body/div/div[1]/div/div[1]/div[2]/div[2]')
    # # 账号输入框
    # name_text = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div[3]/div/div[1]/div/input')
    # # 密码输入框
    # passwd_text = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div[3]/div/div[2]/div/input')
    # # 登录按钮
    # login_button = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div[3]/div/p[1]')
    # # 错误提示
    # errorMsg_from_loginArea = (By.XPATH, '//div[@class="van-toast__text"]')
    # # 注册入口
    # register_enter = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div[3]/div/a')
    # # 记住密码
    # remember_passwd = (By.XPATH, '/html/body/div/div[1]/div/div[1]/div[3]/div/div[3]/label')
    password_login_button = (By.XPATH, '/html/body/div/div[1]/div/div[5]/div[2]/div')
    user_name = (By.XPATH, '/html/body/div/div[1]/div/div[2]/div[1]/div[2]/div/input')
    pass_word = (By.XPATH, '/html/body/div/div[1]/div/div[2]/div[2]/div[2]/div/input')
    login_button = (By.XPATH, '/html/body/div/div[1]/div/div[3]/button')
    phone_name = (By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div/div[2]/div/input')
    code_login_button = (By.XPATH, '/html/body/div[1]/div[1]/div/div[3]/button')
    yi = (By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div/div/div[1]/div')
    er = (By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div/div/div[2]/div')
    san = (By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div/div/div[3]/div')
    si = (By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div/div/div[4]/div')
    wu = (By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div/div/div[5]/div')
    liu = (By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div/div/div[6]/div')
    qi = (By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div/div/div[7]/div')
    ba = (By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div/div/div[8]/div')
    jiu = (By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div/div/div[9]/div')
    ling = (By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div/div/div[11]/div')
