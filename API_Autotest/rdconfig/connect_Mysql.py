# -*- coding: utf-8 -*-
import pymysql

class connctDB():
    def __init__(self):
        self.__host = '10.100.1.151'
        self.__port = 63307
        self.__user = 'ztaduser'
        self.__password = 'jYpzw1DqF4yEsIXo'
        self.__database = 'ims_data'
        self.__db = pymysql.connect(host=self.__host,
                     port=self.__port,
                     user=self.__user,
                     password=self.__password,
                     database=self.__database)

    def runSql(self,sql):
        """
        #执行SQL方法
        :return:
        """
        cursor = self.__db.cursor()
        try:
            cursor.execute(sql)
            self.__db.commit()
        except:
            self.__db.rollback()
        self.__db.close()


#cursor.execute("SELECT * FROM ims_data.ims_derivative_config")

# if __name__ == '__main__':
#     res = connctDB().runSql("DELETE FROM ims_data.ims_derivative_config where derivative_zh_name ='自动化6' ")
#     print(res)

