# HTTPOnly 사용

해당 플래그는 서버 측에서 응답 헤더에
Set-Cookie 헤더를 전송해 쿠키를 생성할 때
옵션으로 설정 가능하며, 이는 JS에서
해당 쿠키에 접근 하는 것을 금지하기때문이다.

이를 활용하면 XSS취약점이 발생하더라도,
공격자가 알아낼 수 없는 쿠키값이기에
세션쿠키를 설정할 때, HTTPOnly 플래그를 설정하는 것 이다.

```json
    {Set-Cookie: session = sbdh1vjwvq;} HttpOnly
```



[Home](https://github.com/sunrabbit123/Learn_Web_Security) / [Back](./README.md)->
