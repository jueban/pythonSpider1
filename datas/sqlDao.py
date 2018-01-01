"""
    SQL集合:
    返回数据处理结果
"""
from conf import db

class Dao:

    def __init__(self):
        self.dbDao = db.db()

    def get_city_name(self):
        sql = "select id cityId,citynameC city_name from db_geography.chinacity order by id"
        result = self.dbDao.select_result_by_sql(sql)
        return result

    def insert_city_info(self, cityId1, data):
        if (cityId1 is None) or (data is None):
            print("不可执行插入操作,因为数据原是空的- -!")
            return False
        try:
            cityId = int(cityId1)

        except (AttributeError, TypeError) as reason:
            print("强转类型失败", reason)
            return False
        else:
            sql = 'INSERT INTO db_geography.cityIntroduce (countryId,cityId,introduce) VALUES( "44","%d","%s") ' % (cityId, data)
            result = self.dbDao.insert_db_by_sql(sql)
            # print(result)
            if(result):
                return True
            else:
                return False