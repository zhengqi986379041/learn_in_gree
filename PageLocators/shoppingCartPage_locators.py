from selenium.webdriver.common.by import By
class ShoppingCartPageLocator:
    pass
    guan_li = (By.XPATH, '/html/body/div[1]/div[1]/div[1]/p/span')
    quan_xuan = (By.XPATH, '/html/body/div[1]/div[1]/div[3]/div[1]/div/i')
    jie_suan = (By.XPATH, '/html/body/div[1]/div[1]/div[3]/div[2]/button')
#/html/body/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/div/div[2]/div[1]/div/button[2]
#/html/body/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/div/div[2]/div[1]/div/button[1]
    goods_name = (By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/div[{0}]/div[2]/div/div/div[2]/div/div[1]/div/div/div[1]/div[1]'.format('1'))
    add_goods_num = (By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/div[{0}]/div[2]/div/div/div[2]/div/div[1]/div/div/div[2]/div[1]/div/button[2]'.format('1'))
    cut_goods_num = (By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/div[{0}]/div[2]/div/div/div[2]/div/div[1]/div/div/div[2]/div[1]/div/button[1]'.format('1'))
    shopping_table = (By.XPATH, '/html/body/div/div[1]/div[6]/div/div[3]')



