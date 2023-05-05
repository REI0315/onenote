# import pytest
# import requests
#
# # 测试用例数据
# testdata = [
#     ('/login', {'username': 'admin', 'password': '123456'}, 200),  # 登录成功
#     ('/login', {'username': 'admin', 'password': '123'}, 401),  # 密码错误
#     ('/user/1', None, 200),  # 获取用户信息
#     ('/user/100', None, 404),  # 用户不存在
#     ('/product', {'name': 'test', 'price': 100}, 201),  # 创建产品
# ]
#
# # ERP系统的接口地址
# BASE_URL = 'http://example.com/api'
#
# # 测试用例
# @pytest.mark.parametrize('path, data, expected', testdata)
# def test_erp_api(path, data, expected):
#     url = BASE_URL + path
#     response = requests.post(url, json=data)
#     assert response.status_code == expected
#     if expected == 200:
#         assert 'token' in response.json()
#     elif expected == 201:
#         assert 'id' in response.json()
#     elif expected == 404:
#         assert 'message' in response.json() and response.json()['message'] == 'User not found'


import asyncio
import os

import edge_tts

TEXT = "你好哟，我是智能语音助手，小伊"
VOICE = "zh-CN-XiaoyiNeural"
OUTPUT_FILE = os.path.join('E:/documents/onenote')


async def _main() -> None:
    communicate = edge_tts.Communicate(TEXT, VOICE)
    await communicate.save(OUTPUT_FILE)


if __name__ == "__main__":
    asyncio.run(_main())
