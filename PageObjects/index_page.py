from PageLocators.indexPage_locators import IndexPageLocator as loc
from PageLocators.myPage_locators import MyPageLocator
from Common.basePage import BasePage

import time


class IndexPage(BasePage):
    """
    首页
    """
    def isExist_logout_ele(self):
        doc = "首页_等待加载完成操作"
        # 如果存在就返回true，如果不存在就返回false
        try:
            self.wait_eleVisible(loc.index_button, doc=doc)
            # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.is_express_news))
            return True
        except:
            return False

    # 店主推荐下单
    def Shopkeeper_recommended_order(self):

        doc = "首页_店主推荐下单操作"
        self.scroll_to_see(loc.floor_location, doc)
        self.wait_eleVisible(loc.is_shopkeeper_recommended, doc=doc)
        self.click_element(loc.rush_purchase_now_1, doc)

    # 楼层下单
    def Floor_purchase(self):
        doc = '首页_楼层下单'
        # self.scroll_to_see(loc.floor_purchase, doc)
        self.scroll_to_bottom(doc=doc)
        self.wait_eleVisible(loc.floor_purchase, doc=doc)
        time.sleep(3)
        self.click_element(loc.floor_purchase, doc)

    # 关闭首页弹窗
    def close_index_Popup(self):
        doc = "首页_关闭弹窗操作"
        self.wait_eleVisible(loc.index_Popup, doc=doc)
        self.click_element(loc.index_Popup, doc)

    # 首页去登录
    def index_to_login(self):
        doc = "首页_去登录操作"
        self.wait_eleVisible(loc.bottom_me, doc=doc)
        self.click_element(loc.bottom_me, doc)
        try:
            self.wait_eleVisible(MyPageLocator.click_login, doc= doc)
        except:
            self.click_element(loc.bottom_me, doc)
        self.wait_eleVisible(MyPageLocator.click_login, doc= doc)
        self.click_element(MyPageLocator.click_login, doc)

