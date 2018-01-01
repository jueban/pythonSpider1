from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
html = urlopen("https://www.mafengwo.cn")

bsObj = bs(html.read())
print(bsObj)