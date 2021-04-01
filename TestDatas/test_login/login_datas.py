# 登录用例数据
# -*- coding: utf-8 -*-
import random

def create_phone():
    # 第二位数字
    second = [3, 4, 5, 7, 8][random.randint(0, 4)]
    # 第三位数字
    third = {
        3: random.randint(0, 9),
        4: [5, 7, 9][random.randint(0, 2)],
        5: [i for i in range(10) if i != 4][random.randint(0, 8)],
        7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
        8: random.randint(0, 9),
    }[second]
    # 最后八位数字
    suffix = random.randint(9999999,100000000)
    # 拼接手机号
    return "1{}{}{}".format(second, third, suffix)
if __name__ == '__main__':
    # 生成手机号
    phone = create_phone()
    print(phone)

# 正常登录场景
success_data = [
    {'user': '16626272282', 'passwd': 'qi123456'}
]
register_phone = [
    {'user': create_phone()}
]
failed_data = [
    {'user': '123', 'passwd': 'gree123456', 'check': '手机号码格式不正确！'},
    {'user': '15266666692', 'passwd': '123456', 'check': '请输入正确的密码'},
    {'user': '16626270000', 'passwd': 'gree123456', 'check': '该号码尚未注册，请用验证码登录'}
]


# 异常用例
phone_data = [
    {'user': '16626272282151', 'passwd': 'qi123456', 'check': '用户不存在'},
]
# phone_data = [
#     {'user': '15765560218151', 'passwd': 'qi123456', 'check': '用户不存在'},
#     {'user': '', 'passwd': 'qi123456', 'check': '请填写手机号'},
#     {'user': '15765560000', 'passwd': 'qi123456', 'check': '用户不存在'},
#     {'user': '15765560218', 'passwd': 'qi123456789', 'check': '用户名或密码不正确'}
#
# ]

# # 正常登录场景
# success_data = {'user': '16626272282', 'passwd': '100201346'}
#
# # 异常用例
# phone_data = [
#     {'user': '16626272282123', 'passwd': '100201346', 'check': '用户不存在'},
#     {'user': '', 'passwd': '100201346', 'check': '请填写手机号'},
#     {'user': '16626270000', 'passwd': '100201346', 'check': '用户不存在'},
#     {'user': '16626272282', 'passwd': '100201346789', 'check': '用户名或密码不正确'}
#
# ]