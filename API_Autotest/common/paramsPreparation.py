# -*- coding: utf-8 -*-
"""
结合测试框架pytest.mark.parametrize参数化定制参数
"""
from common.readExcel import RwExcel
from common.log import GetLogger
from rdconfig.get_path_info import GetPathInfo
import json


class ParamsPre():
    """
    定制化参数准备
    """
    def __init__(self,file):
        self.__file = file
        self.fileName = GetPathInfo().getFileName(self.__file)



    def getParametrize(self,sheet,*args,**kwargs):
        #fileName = GetPathInfo().getFileName("IMS.xlsx")
        # ("url,data,expected",([url,data,expcted],[],[]))
        res1 = RwExcel(self.fileName,sheet)
        #dict1 = res1.read()[0]
        data_list = []
        ids = []
        for i in range(len(res1.read())):
            list = []
            row = res1.read()[i][args[0]] + 1
            url = res1.read()[i][args[1]]
            title = res1.read()[i][args[2]]
            data = res1.read()[i][args[3]]  # data为JSON字符串格式
            # print("+++++:"+data)
            expected = res1.read()[i][args[4]]
            a = json.loads(expected)["code"]
            list.append(row)
            list.append(url)
            list.append(data)
            list.append(a)
            data_list.append(list)
            ids.append(title)
        return tuple(data_list),ids



# if __name__ == '__main__':
#     params,ids = ParamsPre("IMS.xlsx").getParametrize("Sheet1","case_id","url","title","data","expected")
#     print(params,ids)
