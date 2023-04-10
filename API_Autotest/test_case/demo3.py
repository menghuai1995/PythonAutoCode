# -*- coding: utf-8 -*-

from common.log import GetLogger


# def islogin(fun):
#      def inner():
#          print("已登录")
#          fun()
#      return inner
#
# @islogin
# def findone():
#     print("查询一条")



# def isLogin(auth):
#     def inner(fun):
#         def innerIN(*args,**kwargs):
#             if auth ==1:
#                 print("已登录")
#                 return fun(*args,**kwargs)
#             else:
#                 print("未登录,请先登录")
#         return innerIN
#     return inner
# @isLogin(2)
# def findone(a,b):
#      print("查询一条",a,b)
#
#
# findone(3,4)

#引入日志装饰器
def logOut(info):
    def log(fun):
        def warp(*args,**kwargs):
            try:
                return fun(*args,**kwargs)
            except Exception as e:
                GetLogger.get_logger().info(e)
                return info
        return warp
    return log

@logOut("参数错误")
def add(a,b):
    return a/b

#print(add(1,0))
