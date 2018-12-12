# Fastcampus Data Science Extension SCHOOL
## Web Scraping - Static Pages with BeautifulSoup

---
<!--
page_number: true
$size: A4
footer : fastcampus 데이터 사이언스 Extension 스쿨, Wooyoung Choi, 2018
-->

## Index
- git
	- continuous pull
- Web Scraping
- requests
- beautifulsoup

---
## continuous pulled

---
## continuous pull

`$ git remote add upstream https://github.com/anotheruser/original-repo.git`

`$ git fetch upstream`
`$ git merge upstream/master`


## Get static page content from web

---
## Crawling, Scraping, Parsing

---
### Crawling
Crawling: 조직적 자동화된 방법으로 월드 와이드 웹을 탐색하는 것

![](https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/WebCrawlerArchitecture.svg/500px-WebCrawlerArchitecture.svg.png)


---
### Scraping
Scraping: 데이터를 수집하는 행위

![](http://webdata-scraping.com/media/2013/11/web-scraping-services.png)

---
### Parsing
Parsing: 문장 혹은 문서를 구성 성분으로 분해하고 위계관계를 분석하여 문장의 구조를 결정하는 것

![](http://www.booooooom.com/wp-content/uploads/2013/11/michelgondry-tallhappy.jpg)

---
## Caution!!
저작권 침해 위반 소지
- 웹사이트 운영자의 크롤링 금지 룰을 어길경우 
- 월권하여 데이터베이스에 접근
- 타인의 경제적 이익을 침해할 경우
- 개인정보를 수집할 경우(전화번호, 주소, ..)

---
## Requirements
- requests
- beautifulsoup4

---
## How to request??
`$ pip install requests`

`requests.get(url)`

---
## How to parse from response data??
```python
>>> url="https://www.google.com/"
>>> response = requests.get(url)
>>> response
>>> response.status_code
>>> response.encoding
>>> response.text
>>> response.json()
>>> response.headers
```

---
## get li data

```html
<ul>
<li></li>
<li></li>
<li></li>
</ul>
```

---
## with beautifulsoup
`$ pip install beautifulsoup4`
`$ pip install lxml`
```python
import requests
from bs4 import BeautifulSoup
import lxml


html = request.get().text
soup = BeautifulSoup(html, 'lxml')
lis = soup.find('li')
for li in lis:
    print(li.get_text())
```

---
## find headline news from the guardian
https://www.theguardian.com/uk/technology

---
## get table data

```html
<table>
<tbody>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
```

---
## Top Box Office data from rotten tomatoes
https://www.rottentomatoes.com

---
## editorials in rotten tomatoes
https://editorial.rottentomatoes.com/publications/

---
## get article title and contents

```html
<article>
<h1>Title</h1>
<p></p>
<p></p>
<p></p>
</article>
```

---
```python
article_section = soup.find('article')
title = article_section.a.get_text()
contents = article_section.find_all('p')
text = ""
for p in contents:
	text += p.string
print(title, text)
```

---
## get article title and contents from the guardian


<link href="https://fonts.googleapis.com/css?family=Nanum+Gothic:400,800" rel="stylesheet">
<link rel='stylesheet' href='//cdn.jsdelivr.net/npm/hack-font@3.3.0/build/web/hack-subset.css'>

<style>
h1,h2,h3,h4,h5,h6,
p,li, dd {
font-family: 'Nanum Gothic', Gothic;
}
span, pre {
font-family: Hack, monospace;
}
</style>
