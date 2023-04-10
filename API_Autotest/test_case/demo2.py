import requests
import json
from common.baseRequest import BaseRequest




data ={"approvalWhether":0,"countCaliber":"计算口径1","derivativeDescribe":"描述","derivativeEnName":"auto1","derivativeZhName":"自动化1"}
print(type(data))
headers = {
            "content-type": "application/json",
            "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VySWQiOiIiLCJhcHBJZCI6IiIsInVzZXJOYW1lIjoienQyMzA4OCIsImlhdCI6MTY1NzU5MTIxNCwiZXhwIjoxNjU3NTk4NDE0fQ.1SKMWbzVX_mcScUCoRxgV5vSAC3hbqOAhijVvWzQ8haTielcpH6Pf2coILUj22qRc68W0Rco2y9lrPeyefl6eg"
        }

res = BaseRequest().post(url="http://uat-dmsc-api.eminxing.com/ims/web/derivative/save",data=json.dumps(data),headers=headers)
