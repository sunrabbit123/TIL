# XSS를 유발하는 태그 검증

## 사용자의 입력이 HTML형태를 지원할필요가 없다면
    
    1. 꺽쇠( <, > )
    2. 따옴표 (", ')

이러한 특수문자를 **HTML Entity Encoding**을
이용해 태그로써 인식이 안되도록 설정이 가능하다.

```python
    # HTML Entity Encoding 예시
    from jinja2 import utils
    @app.route('/board/', methods=['GET', 'POST'])
    def write():
        ...
        if request.method == 'POST':
            title = utils.escape(request.form.get('title'))
            content = utils.escape(request.form.get('content'))
            query = '...' % (...)
            ...
            return result
    # 화이트리스트 필터링 예시
    import bleach # https://github.com/mozilla/bleach
    @app.route('/board/', methods=['GET', 'POST'])
    def write():
        ...
        if request.method == 'POST':
            ALLOW_TAGS = ['a', 'p', 'h1', 'h2', 'h3']
            ALLOW_ATTRS = ['href']
            title = bleach.clean(request.form.get('title'), ALLOW_TAGS, ALLOW_ATTRS)
            content = bleach.clean(request.form.get('content'), ALLOW_TAGS, ALLOW_ATTRS)
            query = '...' % (...)
            ...
            return result
            
```

## 만약 사용자에게 HTML형태를 지원해야한다면
**화이트리스트 필터링**을 해야 한다.

```txt
화이트리스트 필터링이란

허용해도 안전한 값들을 제외한 모든값을
필터링 하는 것을 의미한다.
```

게시글을 운영하는데
**img**, **video**, **a**태그만 필요하다면
위 세개의 태그를 제외한 모든 태그를
필터링하는 방안이다.

### 사용자 입력을 필터링 할때 유의점
URI Query값, POST Body값만 필터링이 아닌,
User-Agent, Referer과 같은 헤더도
모두 포함하여 **사용자의 인풋 모두 적용해야한다.**

필터링을 구현하게 된다면,
[Mozilla에서 제작한 Bleach도 괜찮다.](https://github.com/mozilla/bleach)

이 외로도 사용자가 로그인할 때 세션에 로그인한 IP주소를 함께 저장하고,
사용자가 접속할 때마다 IP주소를 계속 비교하는 방법이 있지만,
이는 현재에 Mobile유저가 늘어나고,
WiFi가 변경 될 경우에 IP주소가 지속적으로 변한다는 점에 의하여
국가로 탐지하는 형태로 변형되었습니다.


[Home](https://github.com/sunrabbit123/Learn_Web_Security) / [Back](./README.md)->