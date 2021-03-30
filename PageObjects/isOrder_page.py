from PageLocators.isOrderPage_locators import IsOrderPageLocator as loc
import time
from Common.basePage import BasePage


class IsOrderPage(BasePage):
    """
    确认订单页
    """
    def use_intergral(self):
        doc = "确认订单页_使用积分0元支付"
        self.wait_eleVisible(loc.choose_integral, doc=doc)
        self.wait_eleVisible(loc.commodity_price, doc=doc)
        price = int(float(self.get_text(loc.commodity_price))) * 100
        self.click_element(loc.choose_integral, doc)
        self.wait_eleVisible(loc.intergral_text, doc=doc)
        self.input_text(loc.intergral_text, price, doc)
        self.wait_eleVisible(loc.intergral_confirm_button, doc=doc)
        self.click_element(loc.intergral_confirm_button, doc)

    def go_pay(self):
        doc = "确认订单页_去支付按钮"
        self.wait_eleVisible(loc.go_pay_button, doc=doc)
        self.click_element(loc.go_pay_button, doc)

    def get_area_number(self):
        doc = "确认订单页_获取我的收货地址数量"
        self.wait_eleVisible(loc.choose_shipping_address, doc=doc)
        self.click_element(loc.choose_shipping_address, doc)
        self.wait_eleVisible(loc.delivery_address_lists, doc=doc)
        eles = self.number_of_list_elements(loc.delivery_address_lists, doc)
        self.b_back()
        return eles

    def choose_area(self, times = 1):
        doc = "确认订单页_根据位置选择第几个地址"
        self.wait_eleVisible(loc.choose_shipping_address, doc=doc)
        self.click_element(loc.choose_shipping_address, doc)
        time.sleep(2)
        try:
            self.click_element((loc.delivery_address_list[0], loc.delivery_address_list[1].format(times)), doc)
        except:
            self.scroll_to_see((loc.delivery_address_list[0], loc.delivery_address_list[1].format(times)), doc)
            self.wait_eleVisible((loc.delivery_address_list[0], loc.delivery_address_list[1].format(times)), doc=doc)
            self.click_element((loc.delivery_address_list[0], loc.delivery_address_list[1].format(times)), doc)

    def check_area_fail(self):
        doc = "确认订单页_检查收货地址"
        try:
            self.wait_eleVisible(loc.toast_over_area, doc=doc)
            return False
        except:
            return True









