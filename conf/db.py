"""
    db对象,默认执行数据库连接
"""
import pymysql

class db:

    __host = '127.0.0.1'
    __account = 'root'
    __pwd = '**********'

    conn = pymysql.connect(
        host=__host,
        user=__account,
        passwd=__pwd,
        charset='utf8'
    )

    cursor = conn.cursor()


    # 从数据库获取数据,返回列表
    def select_result_by_sql(self, sql):
        L = []
        self.cursor.execute(sql)
        r2 = self.cursor.fetchall()
        for index in r2:
            L.append(index)
        # self.close_conn()
        return L

    # 执行给定插入SQL
    def insert_db_by_sql(self, sql):
        # print(sql)
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print("插入异常: ", e)
            print(sql)
        finally:
            # print('ok')
            # self.close_conn()

            return self.conn.affected_rows()



    def close_conn(self):
        self.cursor.close()
        self.conn.close()
