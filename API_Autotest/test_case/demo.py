from common.log import GetLogger
from common.readExcel import RwExcel
from common.baseRequest import BaseRequest
from rdconfig.get_path_info import GetPathInfo
import os
import json




path = GetPathInfo().getPeojectPath()
filePath = os.path.join(path,"datas")
fileName = os.path.join(filePath,"IMS.xlsx")
# ("url,data,expected",([url,data,expcted],[],[]))
res1=RwExcel(fileName,"Sheet1")
dict1 = res1.read()[0]

data_list =[]
for i in range(len(res1.read())):
    list = []
    url = res1.read()[i]["url"]
    row = res1.read()[i]["case_id"]
    data = res1.read()[i]["data"]
    #data = json.dumps(data)

    expected = res1.read()[i]["expected"]
    a = json.loads(expected)["code"]
    list.append(url)
    list.append(data)
    list.append(a)
    data_list.append(list)


data = dict1["data"]
#data = json.dumps(data)

print(type(data))
url = dict1["url"]
row = dict1["case_id"]
expected = dict1["expected"]
a = json.loads(expected)["code"]
#print(a)

#data  = json.loads(data)
#print(url)
headers = {
  "content-type": "application/json",
  "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VySWQiOiIiLCJhcHBJZCI6IiIsInVzZXJOYW1lIjoienQyMzA4OCIsImlhdCI6MTY1NzU5MTIxNCwiZXhwIjoxNjU3NTk4NDE0fQ.1SKMWbzVX_mcScUCoRxgV5vSAC3hbqOAhijVvWzQ8haTielcpH6Pf2coILUj22qRc68W0Rco2y9lrPeyefl6eg"
 }
code = None
print(json.dumps(data))
try:
    res = BaseRequest().post(url=url,data=data,headers=headers)
    code = res.json()["code"]
    #print(code)

except Exception as e:
    print(e)

if code == a:
    res1.write(row,"pass")
else:
    res1.write(row,"false")
