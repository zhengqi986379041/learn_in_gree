from selenium.webdriver.common.by import By


class IsOrderPageLocator:
    # 选择积分
    choose_integral = (By.XPATH, '//*[@id="price"]/div[2]/div[2]/span')
    # 积分输入框
    intergral_text = (By.XPATH, '//*[@id="price"]/div[10]/div[2]/div/div[2]/div/input')
    # 积分确认按钮
    intergral_confirm_button = (By.XPATH, '//*[@id="price"]/div[10]/button')
    # 去支付按钮
    go_pay_button = (By.XPATH, '//*[@id="write_order"]/footer/div')
    # 商品总价 //*[@id="write_order"]/section/ul/li/div/div[2]/div[2]/p[3]/span[1]
    #'//*[@id="price"]/div[11]/span[1]/span'  /html/body/div/div[1]/div[1]/section/div[4]/div[9]/span[1]/span
    commodity_price = (By.XPATH, '/html/body/div/div[1]/div[1]/section/div[4]/div[9]/span[1]/span')
    # 收货地址栏_选择收货地址
    choose_shipping_address = (By.XPATH, "/html/body/div[1]/div[1]/div[1]/section/div[2]/div/div/div")

    # 收货地址列表eles
    delivery_address_list = (By.XPATH, "/html/body/div[1]/div[1]/section/div/div[{0}]/div[1]/div[1]/span[1]")
    delivery_address_lists = (By.XPATH, "/html/body/div[1]/div[1]/section/div/div")
    # 超出配送区域toast提示
    toast_over_area = (By.XPATH, "/html/body/div[2]/div")
