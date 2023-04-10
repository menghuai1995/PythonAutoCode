a=[1,2,3,'你好']
b=[4,5,6]
c=[]
c.append(a)
c.append(b)
print(tuple(c))
from common.log import GetLogger
log=GetLogger().get_logger()

log.info("1111")