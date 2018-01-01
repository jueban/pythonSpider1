"""
    通过keywords来返回需要爬取的URL
"""
from urls import urlManager
from urllib import parse

class Get_url:

    def __init__(self):
        self.orgUrl = urlManager.UrlManager()

    def get_url_by_key_words(self, keyWords):

        keyWord = parse.quote(keyWords)

        link_url = parse.urljoin(self.orgUrl.baike_city_url(), keyWord)
        return link_url

