from selenium.webdriver.common.by import By


class PaySuccessPageLocator:
    # 支付成功
    success_text = (By.XPATH, '//*[@id="app"]/div[1]/header/h1')
    # 返回首页
    return_index = (By.XPATH, '/html/body/div[1]/div[1]/section/div[1]/div[2]/button[1]/div')
    # 返回订单
    return_order = (By.XPATH, '/html/body/div[1]/div[1]/section/div[1]/div[2]/button[2]/div')
