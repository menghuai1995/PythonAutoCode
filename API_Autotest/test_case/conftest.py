from common.log import GetLogger
#pytest框架无法让日志记录器生效,需要导入日志类
log = GetLogger().get_logger()

def pytest_collection_modifyitems(items):
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")