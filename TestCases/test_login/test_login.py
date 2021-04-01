from PageObjects.index_page import IndexPage
from TestDatas.test_login import login_datas as LD
import pytest


# @pytest.mark.demo
@pytest.mark.usefixtures("access_web")
# @pytest.mark.usefixtures("refresh_page")
class TestLogin:

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", LD.failed_data)
    def test_login_0_failed(self, data, access_web):  # 直接输入conftest里面用到的函数名，传参过来，根据角标调用
        access_web[1].error_login(data['user'], data['passwd'])
        assert access_web[1].check_toast(data['check'])

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", LD.success_data)
    def test_login_1_sucess(self, data, access_web): # 直接输入conftest里面用到的函数名，传参过来，根据角标调用
        access_web[1].password_login(data['user'], data['passwd'])
        assert IndexPage(access_web[0]).isExist_logout_ele()

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", LD.register_phone)
    def test_register_success(self, data, access_web):
        access_web[1].register(data['user'])
        assert IndexPage(access_web[0]).isExist_logout_ele()

