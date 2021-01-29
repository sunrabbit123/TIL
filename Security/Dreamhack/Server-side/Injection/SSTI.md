# Server Side Template Injection
### SSTI

웹 어플리케이션에서 동적인 내용을 
HTML로 출력할 때 미리 정의한
Template에 동적인 값을 넣어
출력하는 Template Engine을 넣어
사용하기도 합니다.

예를 들어 내 정보를 출력해주는
페이지가 있으면 아래처럼 Template을 만들어놓고 변수를 넣어 동적으로 HTML을 만들 수 있습니다.
</br>

- Python에서 Template Engine(jinja2)를 사용해 Render하는 코드
```python
from flask import ...
...
@app.route('/user_info')
def user_info():
    ...		
    template = '''<html>
    <head>
        <style>
        div{background-color : black}
        h3{color : white}
        </style>
    </head>
    <body>
        <h3>유저 아이디: {{user.uid}}</h3>
        <h3>유저 레벨: {{user.level}}</h3>
    </body>
</html>'''
    return render_template_string(template, user=user)
```
</br>

- 위 코드를 guest유저가 접근하여 실행된 출력 화면
<html>
    <head>
        <style>div{background-color : black}
        h3{color : white}
        </style>
    </head>
    <body>
        <div>
            <h3>유저 아이디 : guest </h3>
            <h3>유저 레벨 : user </h3>
        </div>
    </body>
</html>

만약 Template 내부에서 사용되는 context가 아닌
Template source에 사용자 입력이 들어간다면
악의적인 입력을 통해
개발자가 의도하지 않은
임의의 Template 기능을 실행할 수 있습니다.

즉, 사용자의 입력 데이터가
Template에 직접 사용될 경우 template Engine이 해석하여 실행하는
문법을 사용할 수 있기때문에
SSTI취약점이 발생하게됩니다.

SSTI취약점을 막기 위해서는
사용자의 입력 데이터를
Template source에 삽입되지 않도록 해야합니다.
사용자의 입력 데이터를 Template에서 출력하기 위해서
Template context에 값을 넣어 출력해야합니다.

## 예시

```python
...
class Secret(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
secret = Secret('admin', secret_password)
...
@app.route('/board')
def board():
    title = request.form['title']
    content = request.form['content']
    template = '''<html>
    <body>
        <h3 id="title">{{title}}</h3>
        <h3 id="content">%s</h3>
    </body>
</html>''' % content
    return render_template_string(template, title=title, secret=secret)
```

이때 입력을 title과 content를 받는다면
content에 {{secret.password}}를 넣는다면 secret_password가 출력 될 것이다.

```
소스코드의 render_template_string함수 실행 시 template로
사용되는 데이터가 사용자의 입력 데이터에 의해 변조될 수 있으며,
SSTI가 발생합니다.
template Engine이 해석하는 {{ Data }} 형태를
이용하여 공격에 사용할 수 있습니다.
secret 변수 객체에 password를 가져오기 위해 Data 에
secret.password 를 넣어 해결할 수 있습니다.

content={{ secret.password }}
```