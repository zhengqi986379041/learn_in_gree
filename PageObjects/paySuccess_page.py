from PageLocators.paySuccessPage_locators import PaySuccessPageLocator as loc
from Common.basePage import BasePage


class PaySuccessPage(BasePage):

    def isPay_success(self):
        doc = "支付成功页_等待支付成功操作"
        try:
            self.wait_eleVisible(loc.success_text, doc=doc)
            return True
        except:
            return False

    # 返回首页
    def return_index(self):
        doc = "支付成功页_返回首页操作"
        self.wait_eleVisible(loc.return_index, doc=doc)
        self.click_element(loc.return_index, doc)

    # 返回订单
    def return_order(self):
        doc = "支付成功页_返回订单操作"
        self.wait_eleVisible(loc.return_order, doc=doc)
        self.click_element(loc.return_order, doc)
