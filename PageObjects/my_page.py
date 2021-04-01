from PageLocators.myPage_locators import MyPageLocator as loc
from Common.basePage import BasePage
import time

class MyPage(BasePage):
    def check_page(self):
        doc = ''
        try:
            self.wait_eleVisible(loc.see_all_order, doc=doc)
            # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.is_express_news))
            return True
        except:
            return False