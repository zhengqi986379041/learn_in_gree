from selenium.webdriver.common.by import By


class ProductDetailsPageLocator:
    "商品详情页"
    # 立即购买按钮
    buy_now = (By.XPATH, '/html/body/div[1]/div[1]/footer/div[2]/a[2]')

    # 浮窗"购买数量"文案
    buy_number = (By.XPATH, '/html/body/div[1]/div[1]/footer/div[4]/div[2]/div[3]/div[1]')

    # 浮窗"立即购买"按钮
    buy_now_2 = (By.XPATH, '/html/body/div/div[1]/footer/div[4]/div[3]/button[2]')

    # 已选配送地址
    delivery_address = (By.XPATH, '/html/body/div/div[1]/div/div[2]/div[3]/table/tr[1]/td[2]/div/span')

    # 不支持配送地区文案：(本店不支持该区域配送，如需购买请联系客服)
    not_support_address = (By.XPATH, '/html/body/div/div[1]/div/div[2]/div[3]/table/tr[2]/td/div/span')

    # 选择默认地址
    default_address = (By.XPATH, '/html/body/div/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div[3]/div[1]/div[2]/span[1]')