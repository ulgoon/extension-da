# Fastcampus Data Science Extension SCHOOL
## Web Scraping - with API

---
<!--
page_number: true
$size: A4
footer : fastcampus 데이터 사이언스 Extension 스쿨, Wooyoung Choi, 2018
-->

## Index
- review
- What is API?
- How to use API?
- How to get API response?

---
## API
> Application Program Interface
- 응용프로그램에서 사용할 수 있도록 운영체제나 프로그래밍 언어가 제공하는 기능을 제어할 수 있게 만든 인터페이스
- [Windows API](https://msdn.microsoft.com/en-us/library/windows/desktop/ff818516(v=vs.85).aspx)
- [python/C API](https://docs.python.org/3.6/c-api/index.html)

---
## Web API
> 웹서버 혹은 웹브라우저를 위한 API


---
## REST API
`RE`presentational `S`tate `T`ransfer 
`A`pplication `P`rogramming `I`nterface

`Resource` - URI
`Verb` - HTTP method
`Representations` - 표현

---
## So, REST is
> HTTP URI + HTTP method

[Yahoo Finance](https://finance.yahoo.com/)
[json api](http://jsonapi.org/)

---
## [Roy Fielding](http://roy.gbiv.com/)
![](http://farm2.static.flickr.com/1035/1403382259_e85df3c1b4.jpg)
- 2000년 UC Irvine의 박사 학위 논문 "Architectural Styles and the Design of Network-based Software Architectures" 발표

---
## Characteristics of REST
- 범용성(HTTP가 가능하면 OK)
- 리소스 중심 API 명세(URI를 읽는 것으로 이해 가능)
- Stateless(클라이언트의 상태를 신경쓰지 않음)

---
## pros and cons of REST
pros: 
- 스펙없이 기존의 HTTP를 이용해 요청을 처리할 수 있다.

cons: 
- 사용할 수 있는 메소드가 4개다
- 표준이 없다

---
### Before REST
![](https://dab1nmslvvntp.cloudfront.net/wp-content/uploads/2017/05/1494257477001-TraditionalWebserver.png)


---
![](https://dab1nmslvvntp.cloudfront.net/wp-content/uploads/2017/05/1494257479002-RestfulServer.png)


---
## CRUD

### Create
### Read
### Update
### Delete

---
## HTTP Response code

200, 201 - Success
400, 404 - Not found
500 - Server error

[more info..](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html)

---
![](https://www.troyhunt.com/content/images/2016/02/41694168readImage2.png)



---
## How to get data from API

---
## [inspect] -> [Network]

### XHR
- XML HTTP Request

---
## test postman before requests.get()

---
## postman으로 테스트 하는 이유
- API에 독립으로 접근이 가능한지 알아보기 위해
- API에 독립으로 접근했을 때 필요로 하는 헤더값들을 알아보기 위해

---
## https://www.getpostman.com/

---
## learn postman with jsonplaceholder
https://jsonplaceholder.typicode.com/

---
## get lecture list from edx.org

---
## get real estate data from ??


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