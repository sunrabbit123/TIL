# Path Traversal
Path가 사용되는 대푲거인 로직으로는
URL/File이 있습니다.

URL/File의 Path에는 Parent Directory를 의미하는 구분자 `..`가 있습니다.
예를 들어 `/tmp/test/../a` 경로가 해석되면
`/tmp/test/`의 상위 폴더인
`/tmp/`폴더의 하위에 있는 `a` 즉 `/tmp/a`를 나타낸다.

사용자의 입력 데이터가 검증 없이
URL/File Path에 직접적으로 사용되면
설계 및 개발 당시에 의도치않은
임의의 경로에 접근할 수 있는
해당 취약점이 발생합니다. 

예를 들어 내부 API가 path variable로 입력 데이터를 받는 형식으로
구현되어 있어 입력 데이터가
url path로 들어가는 경우도 있습니다.
즉 dream유저의 정보를 가져오기 위해
`http://internal.dreamhack.io/api/user/dream`과 같이
내부 api에 요청을 위해 url에 들어가기도 합니다.

사용자의 입력 데이터가 url path에서 사용될 경우
URL구분 문자를 사용하지 못하도록 하는
필터링 또는 인코딩 없이 사용하게 된다면 `../`과 같은
문자를 통해 의도한 경로가 아닌
상위 경로에 접근해 다른 api를 호출 할 수 있습니다.

> File Path에서 발생하는 Path Traversal은
> File Vulnerability에서 자세히 다룹니다.

이처럼 사용자의 입력 데이터가 경로로 사용되는 경우에는
URL Encoding과 같은 Encoding을 사용해
사용자의 입력 데이터에 포함된
구분 문자가 인식되지 않도록 할 수 있습니다.
이를 통해 Path Traversal 취약점을 방지할 수 있습니다.

## URL에서 해석되는 구분 문자

| 문자 | 의미 | 번역 |
|:--|:--|:--|
|/|**Path identifier**|경로 구분자|
|..|**Parent directory**|부모 폴더|
|?|**Query identifier**|쿼리 시작자|
|#|**Fragment identifier**|# 뒤부터는 전달이 안됨(comment)|
|&|**Parameter separator**|인자값 연결자|

