# 登录用例数据

# 正常登录场景
# success_data = {'user': '15765560218', 'passwd': 'qi123456'}
success_data = [
    {'user': '16626272282', 'passwd': 'qi123456'}
]


# 异常用例
phone_data = [
    {'user': '16626272282151', 'passwd': 'qi123456', 'check': '用户不存在'}
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