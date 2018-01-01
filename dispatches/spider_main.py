from datas import sqlDao
from urls import getUrlByKeyWords
from datas import getWebData
from parse import dataParser

class dispatch:

    def __init__(self):
        self.dao = sqlDao.Dao()
        self.url = getUrlByKeyWords.Get_url()
        self.webData = getWebData.GetBaikeData()
        self.parser = dataParser.Parser()


    def get_needed_data(self):
        cities = self.dao.get_city_name()

        # city = cities[0][1]
        # link = self.url.get_url_by_key_words(city)
        # htmlData = self.webData.get_baike_data(link)
        # data = self.parser.soupObj(htmlData)
        # result = self.dao.insert_city_info(cities[0][0], data)
        # print(result)

        i = 1
        for city in cities:
            link = self.url.get_url_by_key_words(city[1])
            htmlData = self.webData.get_baike_data(link)
            data = self.parser.soupObj(htmlData)
            result = self.dao.insert_city_info(city[0], data)
            if(result):
                print('ok', i)
                i += 1
                continue
            else:
                print('error', link)
                break

        self.dao.dbDao.close_conn()



