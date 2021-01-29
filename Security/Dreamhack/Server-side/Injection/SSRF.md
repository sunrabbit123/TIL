# SSRF
### Server - Side Request Forgery

웹 어플리케이션에서 사용자가 입력한 URL에
요청을 보내는 기능이 구현되어야 하는 경우도 있습니다.

예를 들어 URL을 통해 사용자가 입력한 사진을
업로드하는 기능을 구현하면
사용자가 입력한 URL을 웹 어플리케이션에서 접근해야합니다.

"Client-side Basic"에서 다루는 `Cross-site Request Forgery(CSRF)`과
차이점은 변조된 요청을 보내는 대상의 차이입니다.

**CSRF**는 변조된 요청이 웹 클라이언트가 보내며
**SSRF**는 웹 어플리케이션에서 보내지게 됩니다.

웹 어플리케이션에서 요청을 보내기 때문에
웹 어플리케이션에서 작동하고 있는
서버 내부의 포트, 서버와 연결된 내부망에 요청을 보낼 수 있고
Server-side에서 **변조된 요청 / 의도치 않은 서버로 요청**을
보내는 공격이 `SSRF`입니다.

> 웹 서비스 인프라를 구성 할 때
> 외부망 / 내부망을 나누어 설계하고
> "내부망에서는 인증된 서버 사용자만이 요청을 보낼 수 있다"라고
> 가정해 별도의 인증 없이 기능을 구현하는 경우가 많다.
</br>

> 클라우드 플랫폼들에서도 내부망에서
> 작동하는 기능들이 있어
> SSRF 공격이 발생하면
> 인프라를 공격하는 취약점이 될 수 있습니다.


### 예방법

SSRF 취약점을 방지하기 위해서는
사용자가 입력한 URL의 Host를 
미리 화이트리스트방식으로
검증하는 방법이 있습니다.

미리 신뢰할 수 있는 Domain Name, IP Address를
화이트리스트에 등록하고 사용자가 입력한
URL에서 Host부분을 파싱해 화이트리스트에
있는지 확인합니다.

### - URL Host 화이트리스트 방식 필터링

``` python
rom urllib.parse import urlparse
WHITELIST_URL = [
    'i.imgur.com',
    'img.dreamhack.io',
    ...
]
SCHEME = ['http', 'https']
def is_safehost(url):
    urlp = urlparse(url)
    if not urlp.scheme in SCHEME:
        return False
    hostname = urlp.hostname.lower()
    if hostname in WHITELIST_URL:
        return True
    return False
print(is_safehost('https://127.0.0.1/'))
print(is_safehost('https://i.imgur.com/Bsz7RJN.png'))
```
> 블랙 리스트 방식으로 검증할 경우
> http://127.0.0.4/
> http://0x7f000001/
> 과 같이 다양한 루프백 주소를 사용하거나
> Host에 Domain Name을 넣어 
> DNS Rebinding 공격 등으로 우회할 수 있습니다.

그 외에도 사용자의 URL을 처리하는 서버를
독립적으로 망 분리를 하여
SSRF 취약점이 발생하여도 다른 취약점과 
연계를 하지 못하도록 방지하는 방법이 있습니다.
