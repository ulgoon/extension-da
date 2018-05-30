import requests
import time
from bs4 import BeautifulSoup as btfs
from pymongo import MongoClient


def scrape():
    results = {}
    url = "https://www.naver.com"
    response = requests.get(url).text
    # get execution time
    exec_time = time.ctime()
    results["exec_time"] = exec_time

    soup = btfs(response, "html.parser")
    ul_tag = soup.find('ul', attrs={"class":"ah_l"})
    all_li = ul_tag.find_all('li')
    for li in all_li:
        rank = li.find('span', attrs={"class":"ah_r"}).text
        keyword = li.find('span', attrs={"class":"ah_k"}).text
        results[rank] =  keyword
    return results

if __name__ == "__main__":
    results_dict = scrape()
    try:
        mongo_url = "mongodb://strongadmin:12341234@ds123500.mlab.com:23500/collections"
        client = MongoClient(mongo_url)
        db = client.collections
        nv_query_collection = db.realtimekeyword
        nv_query_collection.insert(results_dict)
        print("success")
    except:
        print("failed. try again")









