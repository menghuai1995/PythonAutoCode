# -*- coding: utf-8 -*-
import pytest
import os

#执行test_case目录下所有的用例文件
pytest.main(['test_case','-s','--alluredir=./allure-report','--clean-alluredir'])
#生成在线报告
#os.system('allure serve ./allure-report')
#生成本地报告
os.system('allure generate ./allure-report -o ./report --clean')