from common.log import GetLogger
#pytest����޷�����־��¼����Ч,��Ҫ������־��
log = GetLogger().get_logger()

def pytest_collection_modifyitems(items):
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")