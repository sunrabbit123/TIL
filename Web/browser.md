# 브라우저에 관하여

여기서 언급하는 브라우저는 우리가 흔히 알고있는

`Chrome`, `Firefox`, `Edge`, `Safari`, `Opera`, `Brave`, ~~Internet Explorer~~등을 얘기한다.

이러한 브라우저들은 사용자가 `WWW`, 즉 월드 와이드 웹을 사용하는데에 있어 가장 필수적인 소프트웨어이다.

과거 최초의 웹 브라우저인 [Erwise](https://ko.wikipedia.org/wiki/Erwise)로부터 시작된 이 소프트웨어는 사용자들에게 인터넷의 자료를 재구성해 읽기 쉽게 제공한다는 기능을 축으로 삼아 크게 변한 것 없이,
지금까지도 여러 갈래로 나뉘며, 업데이트되고 발전해왔다.

그 중 대중적인 `Chrome`, `FireFox`, `Safari`에 대해 얘기를 할 것이며, 서로 어떤 변화가 있었는지, 브라우저 내에서 어떤일이 벌어지는지에 대해 할 것이다.

## 주요 기능
현대 브라우저는 다양한 기능을 제공하지만, 중심이 되는 기능은 **사용자가 원하는 것을 서버에 요청하고, 그것을 해석하여 브라우저에 표시하는 것**이다.

자원은 대부분 `HTML`문서지만 제공하는 기능에 따라 `PDF`, `Image` 또는 다른 형태의 파일일수도 있다.
이런 자원의 주소를 `URI`**(Uniform Resource Identifier)**에 의해 정해진다.

브라우저는 `HTML`, `CSS`에 지정된 명세에 따라 자원 파일(`HTML`)을 해석해서 표시하는데
이는 웹 표준화 기구인 [W3C](https://www.w3.org/)**(World Wide Web Consortium)**에서 정한다.

`w3c`에서 운영중인 사이트인 [w3cSchool](https://www.w3schools.com/)에서는 최신 웹 기능과 예제들을 사용해 볼 수 있다.
우리 곁에서 쉽게 볼 수 있는 브라우저인 `Chrome`, `FireFox`등의 최신 소프트웨어들은 이 표준 명세들을 따른다.
> 물론 각 브라우저마다 다르게 작동하는 점도 있다.

브라우저의 `UI`, 그니까 `User Interface`는 서로 닮은 모습인것을 볼 수 있는데, 보통 다음과 같은 요소들이 보편적으로 포함되어 있다.

    1. URL을 입력할 수 있는 주소 표시 줄
    2. 이전 페이지, 다음 페이지 버튼
    3. 북마크(즐겨찾기)
    4. 새로고침 버튼과 현재 문서의 로드를 중도정지할 수 있는 버튼
    5. 홈 버튼

비록 브라우저의 UI에 있어서, 표준 명세가 없음에도 불구하고 서로 경쟁하고 서로의 기능을 모방하며 비슷한 모습을 갖추게 되었다.

그럼에도 각자 브라우저만의 장단점과 최대의 퍼포먼스를 낼 수 있는 환경이 다르기에, 여러 브라우저들이 현재까지도 자신들만의 팬층을 유지한 채 이어져오고 있다.

## 브라우저의 기본 구조
브라우저의 기본적인 구성 요소는 이렇다.
    1. UI :
        요청한 페이지를 보여주는 창을 제외한 모든 부분으로 주소 표시줄, 북마크 메뉴 등이 이에 해당한다.
    2. 브라우저 엔진 :
        사용자 인터페이스와 렌더링 엔진 사이의 동작을 제어한다.
    3. 렌더링 엔진 :
        요청한 컨텐츠를 표시한다. 만약 HTML일 경우 해석 후 화면에 표시한다.
    4. 통신 : 
        HTTP요청과 같은 네트워크 호출에 사용된다. 이것은 플랫폼의 독립적인 기능이며, 각 플랫폼의 하부에서 실행된다.
    5. UI 백엔드 :
        콤보박스나 글 입력 폼 등의 기본적인 장치를 그린다. 플랫폼에서 명시하지 않은 인터페이스로 OS 사용자 인터페이스 체계를 사용한다.
    6. 자바스크립트 해석기 :
        자바스크립트 코드를 해석하고 실행한다.
    7. 자료 저장소 :
        자료를 저장하는 계층으로 쿠키나 로컬 스토리지등의 자료가 저장되는 저장소이다. 이는 하드디스크에 저장되며 HTML명세 등도 이곳에 저장된다.
    
![브라우저1](image/브라우저1.png)

### 렌더링 엔진에 대해
렌더링 엔진의 역할은 사용자로부터 요청 받은 내용을 브라우저 화면에 표시하는 일이다.
`HTML`, `XML`, `image` 등을 표시할 수 있다.

여기서는 렌더링 엔진의 기본적인 동작과정과 `Safari`와 `Chrome`의 렌더링 엔진인 [`Webkit`과 `FireFox`](#Webkit과-Gecko의-차이점)의 렌더링 엔진인 **Gecko**의 차이점에 대해 얘기할 것이다.

렌더링 엔진의 동작 과정은 다음과 같다.

![렌더링 엔진 과정](https://media.vlpt.us/images/glm777/post/55dd3ea5-8830-4fbc-9a0b-b0d8e1c211b1/2.png)

- [HTML 파싱](#HTML-파싱) :
    렌더링 엔진은 먼저 HTML 문서를 [파싱](#파싱)하고 콘텐츠 트리 내부에서 태그를 DOM노드로 [변환](#변환)한다. 그 다음 외부 [CSS 파일에 포함된 스타일 요소도 파싱](#CSS-파싱)한다. 그 후 스타일 정보와 HTML 표시 규칙은 렌더 트리라고 불리는 또 다른 트리를 구축한다.
- [렌더 트리 구축](#렌더-트리-구축) :
    렌더 트리는 색상 또는 면적과 같이 시각적 속성이 있는 사각형을 포함하고 있는데 이를 정해진 순서대로 화면에 표시하는 역할을 한다.
- 렌더 트리 배치 :
    렌더 트리 구축이 끝나면 실제 배치를 시작한다.
    이는 각 DOM 노드가 정해진 위치에 표시하는것을 의미한다.
- 렌더 트리 그리기 :
    UI 백엔드에서 실행되며 렌더 트리의 각 노드를 거치면서 형상을 만드는 과정이다.

이런 일련의 과정이 진행되는 것이 렌더링 엔진이다.

최신 렌더링 엔진들은 조금 더 빠르고 쾌적한 사용자 경험을 위해 가능한 빨리 내용을 표시하는데 모든 HTML을 파싱할때까지 기다리는 것이 아닌, 배치와 그리기 과정부터 시작한다.

그런 후 네트워크로부터 나머지 내용을 전송받는대로 화면에 표시한다.

이런 방법을 통해 사용자는 빈 화면을 보며 기다리지 않고
화면이 그려지는 것부터 볼 수 있게 된 것이다.

#### Webkit과 Gecko의 차이점

![Webkit](https://media.vlpt.us/images/glm777/post/9705a7c4-0a81-444d-a8c2-f1028d319998/3.png)

> Webkit

![Gecko](https://media.vlpt.us/images/glm777/post/fc68bdc1-c1fe-448c-b712-814c3c789df1/4.png)

> Gecko

Webkit은 렌더 객체로 구성되어 있는 렌더 트리를 이용하며, 요소를 배치하여 `배치(layout)`라는 용어를 사용한다.

Gecko는 렌더 트리를 `형상 트리(frame tree)`라고 부르며 각 요소를 `형상(frame)`이라고 부른다. 요소를 배치하는데는 리플로(reflow)라는 용어를 사용한다.

|렌더링 엔진|렌더 객체들의 모임|각 요소의 이름|요소를 배치하는 용어|
|:-:|:-:|:-:|:-:|
|Webkit|렌더 트리(render tree)|요소|배치(layout)|
|Gecko|형상 트리(frame tree)|형상(frame)|리플로(reflow)|

두 렌더링 엔진은 대동소이 할 뿐이다.
다만 다른부분은 용어나, 과정이 약간씩 다른 것이다.

### HTML 파싱

#### 파싱
DOM 트리를 구축하기 위해서는 먼저 파싱 과정을 거쳐야 한다.
이는 브라우저가 코드를 이해할 수 있는 구조로 변환하는 과정을 의미한다.
파싱결과는 보통 문서 구조를 나타내는 `노드 트리`이며, 이를 `파싱 트리` 또는 `문법 트리라`고 부른다.

파싱은 어휘 분석과 구문 분석으로 분류할 수 있다.

![파싱과정](https://media.vlpt.us/images/glm777/post/e64d4fbc-2137-4306-a370-a961ace306f5/5.png)

- 문서 :
    렌더링 엔진에 전송되는 HTML 파일
- 어휘 분석 :
    자료를 토큰으로 분석하는 과정
    토큰은 용어집이라고 할 수 있다.
    이 과정에서 공백과 줄바꿈과 같은 의미없는 문자들을 제거한다.
- 구문 분석 :
    언어의 구문 규칙을 적용하는 과정이다.
    
파싱의 마지막 단계에 위치한 `파서`는 구문 분석으로 얻은 정보를 토대로 문서 구조를 분석해 `파싱 트리`를 생성한다. 이 과정은 반복되며 어휘 분석단계로부터 토큰을 받아 구문 분석에서 제공한 규칙 정보와 일치하는지 검사한다.
값이 참이면 해당 노드가 파싱 트리에 추가되고 파서는 또 다른 토큰을 요청한다.

만약 규칙이 맞지 않으면 파서는 토큰을 내부적으로 저장하고 이에 일치하는 규칙이 발견될때까지 계속해서 구문 분석을 요청한다.
맞는 규칙이 없을 경우 예외처리되는데 이는 문서가 유효하지 않고 구문 오류를 포함하고 있다는 의미이다.

#### 변환
파싱의 다음단계로, 파싱 트리가 생성된 이후 이를 다른 양식으로 변환하는데, `컴파일`정도로 생각하면 된다.
소스코드를 기계어로 변환하는 `컴파일러`는 파싱 트리 생성 후 이를 브라우저 소프트웨어가 이해할 수 있도록 기계 코드로 변환시킨다.

![변환단계](https://media.vlpt.us/images/glm777/post/67743551-3ebb-49f1-970d-35ae4efb7658/6.png)

#### DOM 트리 구축
위 과정을 통해 생성된 파싱 트리는 DOM(문서 객체 모델, Document Object Model)요소로 변환 될 수 있는데, 이러한 DOM은 마크업과 1대 1 관계를 맺는다.

ex:
```html
<html>
  <body>
    <p>Hello World</p>
    <div><img src="example.png" /></div>
  </body>
</html>
```
위의 코드는 아래와 같이 변환될 수 있다.

![DOM트리1](https://media.vlpt.us/images/glm777/post/8634478f-0ce1-48f3-9648-7fe1eaa60ebe/7.png)

HTML과 마찬가지로 DOM에도 w3c에 의해 [일종의 명세](https://www.w3.org/DOM/DOMTR)가 정해져있다.
이는 문서에 대한 일반적인 명세이다. 물론 [HTML 요소](https://www.w3.org/TR/2003/REC-DOM-Level-2-HTML-20030109/idl-definitions.html)를 설명하는 부분도 포함되어 있다.

이와 같은 과정을 거쳐 구축된 DOM트리는 렌더트리에 대응되어 우리가 흔히 아는 HTML 문서로 변환된다.

트리가 DOM노드를 포함한다고 하는 것은 ODM의 하나를 실행하는 요소를 구성한다는 의미이다.

브라우저에서는 내부 속성들을 사용해 이 작업을 실행한다.

#### CSS 파싱
CSS는 HTML과는 다르게 문맥이 자유로운 문법이고 파서를 이용해서 파싱이 가능하고 [CSS명세(CSS 어휘와 문법을 정의한 내용)](https://www.w3.org/TR/CSS2/grammar.html)를 따른다.

한가지의 예시를 보면, 다음은 정규표현식을 정의된 어휘 문법이다.

```
omment   \/*[^]*+([^/][^]*+)\/
num        [0-9]+|[0-9]"."[0-9]+
nonascii    [\200-\377]
nmstart    [_a-z]|{nonascii}|{escape}
nmchar    [_a-z0-9-]|{nonascii}|{escape}
name        {nmchar}+
ident        {nmstart}{nmchar}
```

크롬의 렌더링 엔진인 [웹킷](#Webkit과-Gecko의-차이점)은 위에서 서술한 CSS 문법 파일로부터 파서를 생성하기 위한 `플렉스`와 `바이슨 파서 생성기`를 사용한다.

바이슨은 상향식 이동 감소 파서를 생성하며, 이 파서는 CSS파일을 스타일 시트 객체로 파싱시키며 각 객체는 CSS 규칙을 포함한다.
해당 CSS 규칙 객체는 선택자와 선언 객체, 그리고 CSS 문법과 일치하는 다른 객체를 포함한다.

![바이슨](https://media.vlpt.us/images/glm777/post/6fcc4a2b-fdcb-445f-a751-37cff72c36c5/8.png)

#### 스크립트와 스타일 시트의 진행 순서

![스크립트 진행 순서](https://media.vlpt.us/images/glm777/post/6c9d98b4-cd26-4ea9-8f95-08f22ba76442/9.png)

웹은 파싱과 실행이 동시에 수행되는 동기화(synchronous)모델이다.
스크립트가 실행되는동안 문서의 파싱은 중단되며 만약 스크립트가 서버 내부가 아닌 외부에 있는 경우, 네트워크로부터 자원을 가져오게 되는데 이 또한 실시간으로 처리되며 자원을 전부 전송받을때까지 문서의 파싱은 중단된다.
> 한줄요약 : 스크립트가 실행되고, 자원을 가져오기까지 파싱은 중단된다.

스타일 시트의 경우 일반적으로 DOM 트리를 변경하지 않기 때문에 문서 파싱을 기다릴 필요가 없다. 그러나 **스크립트가 문서를 파싱하는동안 스타일 정보를 요청하는 경우**에는 문제가 된다.
스타일이 파싱되지 않은 상태라면 스크립트는 잘못된 결과값을 내놓기 때문에 많은 문제를 유발한다.
이런 상황이 흔치 않을지도 모른다고 생각할 수 있지만 의외로 많이 발생하는 이슈이다.
이런 상황이 발생하면 렌더링 엔진들간의 차이점이 나타나는데 [Webkit](#Webkit과-Gecko의-차이점)의 경우 로드되지 않은 스타일 시트 중 문제가 될만한 속성이 있을때만 스크립트를 중단하지만 [Gecko](#Webkit과-Gecko의-차이점)의 경우 로드 대기중이거나 파싱중인 스타일 시트가 있더라도 모든 스크립트를 중지한다.

#### 렌더 트리 구축
렌더링 엔진이 [DOM 트리](#DOM-트리-구축)를 구축되는동안 브라우저 엔진은 렌더 트리를 구축한다.

렌더 트리란 문서를 시각적인 구성 요소로 변환시켜주는 역할을 하며 이 과정에 있어서 스타일의 경우 브라우저에서 제공하는 기본 스타일 시트를 따라가게 된다.

이때 DOM 트리와 렌더 트리가 완전히 1대 1로 대응되어 변환되지는 않으며 `dispaly:none, hidden` 등은 렌더트리에 포함되지 않는다.

![렌더 트리 구축](https://media.vlpt.us/images/glm777/post/5fd5d4e5-37d1-45f8-9ca3-379be8a5e9fa/10.png)

#### 웹 페이지에 배치하기

렌더 트리가 생성되고 나면 웹 페이지에 배치하기 시작하는데 이 과정을 `리플로(Reflow)`라고 부른다.
브라우저 좌표 `0, 0`부터 시작하여 각 영역에 해당되는 `Viewport`만큼의 면적을 가지며 배치된다.
이 과정에서 일부 영역에 변경이 발생할 경우 [전역 배치](#전역-배치)와 [점증 배치](#점증-배치)가 발생한다.

브라우저에서는 렌더 트리를 활용해 실제로 화면에 우리가 보는 도형과 텍스트를 그리기 시작하는데, 이대 더티 렌더러의 Paint 메서드를 호출함과 동시에 UI Backend 요소를 이용해 그린다.

각각의 요소는 블럭 렌더러의 순서에 따라 그려지며 그 순서는 아래와 같다.

    1. 배경
    2. 배경 이미지
    3. 테두리
    4. 자식 엘리먼트
    5. 아웃라인

해당 과정이 끝나고 모든 요소가 그려지고 난 뒤에 브라우저에서 변경이 발생할 경우 [리플로(Reflow)](#리플로우)와 [리페인트(Repaint)](#리페인트)가 실행된다. 리페인트는 변경된 스타일을 다시 적용하는 기능을 하며 만약 크기와 위치도 변경되었을 경우 리플로도 실행된다.

이 모든 과정이 끝나고 나면 우리가 평소에 사용하는 웹사이트의 모습을 볼 수 있게 된다.

#### 단어장
##### 점증 배치
[더티 렌더러](#더티-렌더러)가 배치되는 경우 비동기적으로 발생한다.

##### 더티 렌더러
변경 요소를 브라우저가 특수히 지정하여 해당 요소만 변경하는것을 의미한다.

##### 전역 배치
렌더링 전체에 영향을 주는 전역 스타일의 변경 사항이 있을 경우 발생한다.


##### 리페인트
이는 레이아웃에 영향을 주지 않지만, 가시성에는 영향을 주는 엘리먼트가 변경되면 발생한다.

> ex : opacity, background-color, visibility, outline

오페라에 따르면, "브라우저가 DOM 트리에 있는 다른 모든 노드의 가시성을 확인해야 하므로 리페인트는 비용이 많이 든다."라고 하였다.

##### 리플로우
이는 모든 엘리먼트의 위치와 길이 등을 다시 계산하는 것으로 문서의 일부 혹은 전체를 다시 렌더링한다.

단일 엘리먼트 하나를 변경해도, 하위 엘리먼트나 상위 엘리먼트 등에 영향을 미칠 수 있다.
