"""
    使用BeautifulSoup分析网页
"""
from bs4 import BeautifulSoup


class Parser:

    def soupObj(self, data):
        if data is None:
            print('传入数据不能为空')
            return False

        soup = BeautifulSoup(data, 'html.parser')
        content = self.parse(soup)
        if content is None:
            print('传入数据为空')
            return False
        else:
            return content

    def parse(self, soup):

        datas = soup.findAll('div', class_='para')
        result = ''

        for data in datas:

            result += (data.getText().replace('"', '\''))

        # print(result)
        return result