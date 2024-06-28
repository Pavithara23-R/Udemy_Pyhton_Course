from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find(name="a", class_="storylink")
article_text = []
article_link = []
for article_tag in articles:
    text = article_tag.getText()
    article_text.append(text)

    link = article_tag.get("href")
    article_link.append(link)

article_upvotes = [score.getText() for score in soup.find_all(name="span", class_="score")]

# print(article_text)
# print(article_link)
# print(article_upvotes)
print(article_upvotes[0])


# with open("./website.html", encoding="utf-8") as file:
#     contents = file.read()
#
#
# soup = BeautifulSoup(contents, "html.parser")
# #print(soup.title)
# # print(soup.title.name)
#
# #print(soup.p)
#
#
# all_anchor_tag = soup.find_all(name="a")
# #print(all_anchor_tag)