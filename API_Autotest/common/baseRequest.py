import requests
from common.log import GetLogger

log = GetLogger().get_logger()

class BaseRequest():
    def __init__(self):
        pass

    def get(self,url,params=None,**kwargs):
        try:
            response=requests.get(url,params=params,**kwargs)
            log.info("==========接口API请求开始===========")
            log.info("请求URL：{}/n请求参数：{}".format(url,params))
            log.info("接口请求成功！返回参数:{}".format(response.text))
            log.info("===========结束===========")
        except Exception as e:
            log.error("接口请求异常！{0}".format(e))

    def post(self,url,data=None,json=None,headers=None,**kwargs):

        try:
            respose = requests.post(url=url,data=data.encode("utf-8"),json=json,headers=headers,**kwargs)
            log.info("===========接口API请求开始===========")
            log.info("请求URL：{}".format(url))
            log.info("请求参数：{}".format(data,json))
            log.info("响应参数：{}".format(respose.text))
            log.info("响应时间：{}ms".format(respose.elapsed.total_seconds()*1000))
            log.info("===========结束===========")
            return respose
        except Exception as e:
            log.error("接口请求异常！{0}".format(e))



# if __name__ == '__main__':
#     Headers = {
#         "content-type": "application/json"
#         }
#     a=BaseRequest()
#     a.get("http://192.168.122.105:9900/basic-user/web/business/system/list")
#     data={
# 	"businessSystemCode": "DAC",
# 	"businessSystemId": 0,
# 	"businessSystemKey": "DAC",
# 	"businessSystemName": "基础配置中心"
# }
#     a.post("http://192.168.122.105:9900/basic-user/web/business/system/save",data=data,headers=Headers)

