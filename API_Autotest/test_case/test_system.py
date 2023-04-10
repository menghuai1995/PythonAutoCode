import pytest
from common.readExcel import RwExcel
from common.baseRequest import BaseRequest
from rdconfig.get_path_info import GetPathInfo
import os
import json
from common.log import GetLogger
import allure
from rdconfig.connect_Mysql import connctDB
from common.paramsPreparation import ParamsPre
log=GetLogger().get_logger()

params,ids = ParamsPre("IMS.xlsx").getParametrize("Sheet1","case_id","url","title","data","expected")

class TestClass:
    # fileName = GetPathInfo().getFileName("IMS.xlsx")
    # # ("url,data,expected",([url,data,expcted],[],[]))
    # res1 = RwExcel(fileName, "Sheet1")
    #
    # dict1 = res1.read()[0]
    # data_list = []
    # ids = []
    # for i in range(len(res1.read())):
    #     list = []
    #
    #     row = res1.read()[i]["case_id"]+1
    #     url = res1.read()[i]["url"]
    #     title = res1.read()[i]["title"]
    #
    #     data = res1.read()[i]["data"]#data为JSON字符串格式
    #     #print("+++++:"+data)
    #
    #
    #
    #     expected = res1.read()[i]["expected"]
    #     a = json.loads(expected)["code"]
    #     list.append(row)
    #     list.append(url)
    #     list.append(data)
    #     list.append(a)
    #     data_list.append(list)
    #     ids.append(title)
    #
    # params=tuple(data_list)

    #@allure.title()
    @allure.feature("新增接口")
    @pytest.mark.parametrize("row,url,data,expected",params,ids=ids)
    def test_1(self,row,url,data,expected):
        headers = {
            "content-type": "application/json",
            "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VySWQiOiIiLCJhcHBJZCI6IiIsInVzZXJOYW1lIjoienQyMzA4OCIsImlhdCI6MTY4MDIyNjQ4NiwiZXhwIjoxNjgwMjMzNjg2fQ.LI2dt0MTokwhlFJuX5p_JPIHx3g1tD8yi2FuyStBehYc89Q9sSovZJT4ZrrLWwZ95GHlG1q5m3MmTW4_yv8ofg"
        }
        code = None

        res = BaseRequest().post(url=url, data=data, headers=headers)
        code = res.json()["code"]
        #print(res.text)
        assert code == expected
        path = GetPathInfo().getPeojectPath()
        filePath = os.path.join(path, "datas")
        fileName = os.path.join(filePath, "IMS.xlsx")
        # ("url,data,expected",([url,data,expcted],[],[]))
        res1 = RwExcel(fileName, "Sheet1")
        #测试结果写入Excel文件
        if code == expected:
            res1.write(row, "pass")
        else:
            res1.write(row, "false")
    def teardown_class(self):
        #清除垃圾数据
        connctDB().runSql("DELETE FROM ims_data.ims_derivative_config where derivative_zh_name ='自动化6' ")




# if __name__ == '__main__':
#     pytest.main(['test_system.py','-s','--alluredir=../allure-report','--clean-alluredir'])
#     # 执行命令 allure generate ./temp -o ./report --clean ，生成测试报告
#     os.system('allure serve ../allure-report')
