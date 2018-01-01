# coding=utf-8
"""
    根据URL获取网站上的信息
"""
import urllib.request


class GetWebData:

    def check_urls(self, url):
        if url is not str:
            return False

    def header(self):
        headers = {"User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:36.0) Gecko/20100101 Firefox/36.0",
                   "Referer": "http://xxx.yyy.com/test0",
                   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                   "Accept-Language": "en-US,en;q=0.5",
                   "Accept-Encoding": "gzip, deflate",
                   "Connection": "keep-alive",
                   # "Cookie":"QSession=",
                   "Content-Type": "application/x-www-form-urlencoded",
                   }
        return headers


class GetBaikeData(GetWebData):

    def get_baike_data(self, url):
        if (self.check_urls(url)):
            print('链接不对')
        else:
            response = urllib.request.urlopen(url)
            if ( response.getcode() != 200):
                if ( response.getcode == 404):
                    print('页面不存在')
                elif ( response.getcode == 503):
                    print('访问时出错')
                else:
                    print('我特么也不知道什么错')
                return ''
            else:
                ls = response.read().decode('utf-8')
                return ls

