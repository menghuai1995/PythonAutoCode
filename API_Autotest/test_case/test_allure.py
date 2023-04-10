# -*- coding: utf-8 -*-
import os
import allure
import pytest
@allure.feature("测试流程")
class TestAllure():

    @allure.title("case1")
    def test_1(self):
        print("用例1")
    @allure.title("case2")
    def test_2(self):
        print("用例2")
#
# if __name__ == '__main__':
#     pytest.main(['test_allure.py', '-s', '--alluredir=./allure-report'])
#     # 执行命令 allure generate ./temp -o ./report --clean ，生成测试报告
#     os.system('allure serve --alluredir=./allure-report')