from PageLocators.ProductDetailsPage_locators import ProductDetailsPageLocator as loc
from Common.basePage import BasePage
import time

class ProductDetailsPage(BasePage):
    def check_delivery_address(self):
        doc = '商品详情页_检查配送地址/选择默认地址'
        self.wait_eleVisible(loc.delivery_address, doc=doc)
        try:
            self.wait_eleVisible(loc.not_support_address, doc=doc) # 等待不支持配送
            self.click_element(loc.delivery_address, doc=doc) # 点击已选地址
            self.wait_eleVisible(loc.default_address, doc=doc) # 等待默认地址标识
            self.click_element(loc.default_address, doc=doc) # 点击默认地址标识
            time.sleep(2)
        except:
            pass

    def buy_now(self):
        doc = '商品详情页_立即购买'
        self.wait_eleVisible(loc.buy_now, doc=doc)
        self.click_element(loc.buy_now, doc)
        time.sleep(2)
        self.wait_eleVisible(loc.buy_number, doc=doc)
        self.click_element(loc.buy_now_2, doc)