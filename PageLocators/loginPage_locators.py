from selenium.webdriver.common.by import By


class LoginPageLocator:
    """
    登录页面
    """
    password_login_button = (By.XPATH, '/html/body/div/div[1]/div/div[5]/div[2]/div')# 切换密码登录按钮
    user_name = (By.XPATH, '/html/body/div/div[1]/div/div[2]/div[1]/div[2]/div/input')# 密码登录的用户名
    pass_word = (By.XPATH, '/html/body/div/div[1]/div/div[2]/div[2]/div[2]/div/input')# 密码登录的密码
    login_button = (By.XPATH, '/html/body/div/div[1]/div/div[3]/button')# 密码登录的登录按钮
    phone_name = (By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div/div[2]/div/input')# 验证码登录的手机号
    code_login_button = (By.XPATH, '/html/body/div[1]/div[1]/div/div[3]/button')# 验证码登录获取验证码登录按钮
    # 验证码登录的验证码数字按钮
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
    error_login_toast = (By.XPATH, '/html/body/div[2]/div')# 异常登录的toast提示

