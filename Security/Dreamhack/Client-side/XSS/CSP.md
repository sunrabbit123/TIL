# CSP(Content Security Policy)

[예시](#예시)
이는 응답 헤더나, meta태그를 통해 아래와 같이 선언해서 사용하며,
각각의 지시어를 적용하여 사이트에서 로드하는 리소스들의 출처를 제한할 수 있습니다.
```json
    { Content-Security-Policy : <지시어>; ... }
```

-----

예를 들면

    defautl-src 'self' *.dreamhack.io*
이와 같이 설정된 CSP는 모든 리소스의 출처가
현재 도메인이거나,`*.dreamhack.io`도메인이
출처일 경우만 허용한다.
또한 `script-src`를 선언해 자바스크립트 코드의
출처를 제한할 수 있으며,
공격자가 외부에 업로드된 JS파일을 호출하거나
직접 JS코드를 작성하는 등의 행동을 
막을 수 있다.
**하지만 신뢰받는 CDN서버가 해킹당하면 무력화된다는 단점이 있다.**

-----

이 외에도 많은 리소스의 출처를 제한할 수 있는
지시어들이 존재하며,
`script-src 'nonce-noncevalue13b739d8ea12'`와 같이
script-src를 이용해 랜덤값을 설정하고, JS를 실행 할 경우
서버에서 생성된 이 랜덤값을 알아야만 실행가능토록 가능하다.
**이는 XSS를 당하더라도 랜덤값을 유추 불가능하다면**
**JS실행이 불가능하도록 한다.**

-----

또한 `script-src 'sha256-hashvalue_base64'`와 같은 형태로
JS나 스타일시트의 해쉬를 구해 CSP를 설정하면,
미리 구한 해쉬와 다를 경우
실행 불가능하도록 만들 수 있다.

## 예시

```html
<!doctype html>
<html>
    <head>
        <meta http-equiv="Content-Security-Policy" content="script-src 'sha256-5jFwrAK0UV47oFbVg/iCCBbxD8X1w+QvoOUepu4C2YA='">
    </head>
    <body>
    <script>alert(1);</script>
    </body>
</html>
```
이 코드는 script 태그 안의 JS코드의 해쉬를
미리 구해 **CSP**를 설정해
alert(1)을 호출한 예시입니다.

작성한 CSP지시어를 확인하려면
[http://csp-evaluator.withgoogle.com](http://csp-evaluator.withgoogle.com)에서
확인이 가능합니다.

[Home](https://github.com/sunrabbit123/Learn_Web_Security) / [Back](./README.md)->