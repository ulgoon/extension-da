import requests
from bs4 import BeautifulSoup as btfs


def scrape():
    url = "https://www.naver.com"
    response = requests.get(url).text
    soup = btfs(response, "html.parser")
    ul_tag = soup.find('ul', attrs={"class":"ah_l"})
    all_li = ul_tag.find_all('li')
    for li in all_li:
        rank = li.find('span', attrs={"class":"ah_r"}).text
        keyword = li.find('span', attrs={"class":"ah_k"}).text
        print(rank, keyword)
scrape()
