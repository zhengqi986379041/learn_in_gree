from PageObjects.isOrder_page import IsOrderPage
from PageObjects.login_page import LoginPage
from PageObjects.paySuccess_page import PaySuccessPage
from TestDatas import login_datas as LD
from PageObjects.productDetails_page import ProductDetailsPage
import time
import sys, os
# 运行命令
# pytest --reruns 2 --reruns-delay 5 -s --junitxml=Outputs/Reports/report.xml --html=Outputs/Reports/html_report.html


class TestShopkeeperRecommened:
    sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))


    # 店主推荐成功下单
    # @pytest.mark.smoke
    def test_shopkeeper_recommened_success(self, access_to_order):
        # print(CD.loc_isOrder.commodity_price.text)
        # 步骤
        # 关闭首页弹窗
        access_to_order[1].close_index_Popup()
        # 首页去登录
        access_to_order[1].index_to_login()
        # 登录页输入账号密码
        LoginPage(access_to_order[0]).login(LD.success_data[0]['user'], LD.success_data[0]['passwd'])
        # 店主推荐下单
        time.sleep(2)
        access_to_order[1].Shopkeeper_recommended_order()
        # 检查配送地址
        ProductDetailsPage(access_to_order[0]).check_delivery_address()
        # 商品详情页立即购买
        ProductDetailsPage(access_to_order[0]).buy_now()
        # 确认订单页使用积分
        IsOrderPage(access_to_order[0]).use_intergral()
        # 去支付
        IsOrderPage(access_to_order[0]).go_pay()
        # 获取收货地址数量
        try:
            number = IsOrderPage(access_to_order[0]).get_area_number()
            # 循环选择地址去支付
            for times in range(1, number + 1):
                # 当提交订单有toast提示时
                if IsOrderPage(access_to_order[0]).check_area_fail() == False:
                    # 选择第几个地址
                    IsOrderPage(access_to_order[0]).choose_area(times=times)
                    # 使用积分
                    IsOrderPage(access_to_order[0]).use_intergral()
                    # 去支付
                    IsOrderPage(access_to_order[0]).go_pay()
                    time.sleep(2)
                    try:
                        # 再一次去支付，假如上一次支付成功了，这里异常内消就行
                        IsOrderPage(access_to_order[0]).go_pay()
                    except:
                        pass
                else:
                    break
        except:
            pass
        # 断言
        assert PaySuccessPage(access_to_order[0]).isPay_success()