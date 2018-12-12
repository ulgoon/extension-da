# Fastcampus Data Science Extension SCHOOL
## Web Scraping - Dynamic Pages

---
<!--
page_number: true
$size: A4
footer : fastcampus 데이터 사이언스 Extension 스쿨, Wooyoung Choi, 2018
-->

## Index
- review
- install selenium
- dynamic web pages
- scrape with selenium


---
## Requirements
- `$ pip install selenium`
- ChromeDriver: https://sites.google.com/a/chromium.org/chromedriver/downloads

---

## Review

---
## requests && BeautifulSoup
- 정적인 페이지를 수집할 때
- requests: HTTP 요청 -> HTML 응답
- BeautifulSoup: HTML 응답 -> 분석 후 요소 접근

---
## But..
- BeautifulSoup은 AJAX나 javaScript로 그려지는(렌더링) 요소나 행동은 접근할 수 없음

---
## Selenium!
- Web Application User test tool
- `$ pip install selenium`

---
## Dynamic Contents

---
### Static Web site - 1
<div id="dynamic-btn1" style="width:200px; height:200px; background:red;"></div>

---
### Static Web site - 2
<div id="dynamic-btn2" style="width:200px; height:200px; background:green;"></div>

---
### Static Web site - 3
<div id="dynamic-btn3" style="width:200px; height:200px; background:blue;"></div>


---
### Dynamic Web site
<div id="dynamic-btn" style="width:200px; height:200px; background:black;"></div>
<button type="button" onclick="document.getElementById('dynamic-btn').style.background='red'" style="font-size:20px;">Red</button>
<button type="button" onclick="document.getElementById('dynamic-btn').style.background='green'" style="font-size:20px;">Green</button>
<button type="button" onclick="document.getElementById('dynamic-btn').style.background='blue'" style="font-size:20px;">Blue</button>

---
## Pros & Cons
### Pros
- 동적 페이지 제어 가능
- 사용자처럼 행동 가능
- iframe 제어 가능

### Cons
- 느림
- BS4에 비해 신경써야 할 것이 많음

---
## Route is important while using Selenium
- BeautifulSoup : 수집할 요소 선택 -> url 정보 수집 -> 스크래핑 수행
- Selenium: 수집할 요소 선택 -> 요소까지의 경로 선정 -> 스크래핑 수행

---
## Web Scraping with Selenium

---
## naver cafe
- login
- execute script
- iframe - switch frame

---
## Quora
- scroll


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