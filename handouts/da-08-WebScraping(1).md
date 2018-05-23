# Fastcampus Data Science Extension SCHOOL
## Web Scraping with BeautifulSoup

---
<!--
page_number: true
$size: A4
footer : fastcampus 데이터 사이언스 Extension 스쿨, Wooyoung Choi, 2018
-->

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

---
## How to parse from response data??

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