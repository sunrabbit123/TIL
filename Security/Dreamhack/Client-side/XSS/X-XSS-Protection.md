# X-XSS-Protection Header

이는 Response Header에 아래와 같이 선언 및 사용합니다.
```Response Header
X-XSS-Protection: <Value>
```
해당 정책은 웹 브라우저에 내장된
XSS Filter를 활성화할 것인지를 설정한다.

이는 XSS라 판단되는 경우, 유저에게 알리고
의심되는 코드를 차단합니다.
이는 Reflected XSS 공격에 대해
효과적이고 적합한 방법이며,
다른 유형의 XSS공격을 방어할 수 없습니다.

```Response Header
X-XSS-Protection: 0
X-XSS-Protection: 1
X-XSS-Protection: 1; mode=block
X-XSS-Protection: 1; report=<reporting-uri>
```
위 처럼 4가지의 방법이 있으며,
기본값은 1이며,

1. 0일 경우 비사용
2. 1일 경우 XSS공격이 감지된 부분만 제거
3. mode = block이면 렌더링 전체 중단
4. report면 미리 설정된 주소에 신고

## 경고
XSS Filter는 XSS공격에 대한
강력한 방어수단이었지만,
최신브라우저에서 삭제되는 추세이다.
> **실 서비스의 보안을 위해서 이 헤더를 신뢰하지 않는것을 권장합니다.**



[Home](https://github.com/sunrabbit123/Learn_Web_Security) / [Back](./README.md)->