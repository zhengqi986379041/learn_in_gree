from Common.basePage import BasePage
from PageLocators.classificationDetailsPage_locators import ClassficationDetailsPageLocator as loc

class ClassificationDetailsPage(BasePage):
    '''
    分类详情页-类目下具体的商品列表
    '''

    # 立即购买
    def buy_now(self):
        doc = "分类详情页_立即购买操作"
        self.wait_eleVisible(loc.buy_now, doc=doc)
        self.click_element(loc.buy_now, doc)
