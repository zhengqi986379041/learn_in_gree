from selenium.webdriver.common.by import By


class IndexPageLocator:
    """
    首页
    """
    # 店主推荐模块展示
    is_shopkeeper_recommended = (By.XPATH, '/html/body/div/div[1]/div[1]/div[3]/div[3]/div[4]/div[1]/div[1]/span[2]')
    # 立即抢购第一个商品
    rush_purchase_now_1 = (By.XPATH, '/html/body/div/div[1]/div[1]/div[3]/div[3]/div[4]/div[2]/div/div[1]/span')
    # 立即抢购按钮
    rush_purchase_now = (By.XPATH, '/html/body/div/div[1]/div[1]/div[3]/div[3]/div[4]/div[1]/div[2]')
    # 快报模块展示
    is_express_news = (By.XPATH, '/html/body/div/div[1]/div[1]/div[3]/div[2]/div[1]/div[2]')
    # 导航栏-我的
    bottom_me = (By.XPATH, '/html/body/div/div[1]/div[2]/div/div[5]/div[2]/span')
    # 首页弹窗
    index_Popup = (By.XPATH, '/html/body/div/div[1]/div[2]/div/div')
    # 楼层商品
    floor_purchase = (By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[3]/div[3]/div[5]/div/div/div[2]/div/div/div/div/div/div[1]/div[1]/p[1]')
    # 楼层名位置
    floor_location = (By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[3]/div[3]/div[5]/div/div/div[1]/div/div/div/div[1]')