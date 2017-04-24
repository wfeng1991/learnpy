import urllib.request as request
from bs4 import BeautifulSoup



url = "https://www.zhihu.com/people/zhao-yu-jia-74/answers"

html = request.urlopen(url).read()

# print(html)

soup = BeautifulSoup(html, 'lxml')



news_titles = soup.select("div.List-item h2.ContentItem-title a")

# 对返回的列表进行遍历
for n in news_titles:
    # 提取出标题和链接信息
    title = n.get_text()
    link = n.get("href")
    data = {
        '标题':title,
        '链接':link
    }
    print(data)
