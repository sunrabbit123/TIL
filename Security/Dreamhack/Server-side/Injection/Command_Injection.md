# Command Injection

## 목차
1. [개요](#개요)
2. [특수문자](#특수문자)

## 개요
웹 앱에서 OS Command를 사용하기 위해
> PHP(System)
> NodeJS(child_process)
> Python(os.system)
이 셋과 같이 OS Command를 실행하는 함수가
구현되어있습니다.

OS Command란
1. `linux(ls, pwd, ping, zip)`
2. `windows(dir, pwd, ping)`
이 처럼 OS에서 사용되는 Command입니다.

일반적으로 웹 어플리케이션에서 OS Command를 사용하는 이유는 이미 기능을 구현한
OS 실행파일이 존재할 때
코드 상에서 다시 구현하지 않고
`OS Commnad`로 실행하면 더 편리하기 때문이다.

`OS Commnad`는 내부적으로
쉘을 이용해 실행하는데,
쉘에는 한 줄에 여러 명령어를 실행하는 등의
쉘 사용자 편의성을 위해 제공하는
특수 문자들이 존재합니다.

`OS Command`를 사용할 때
만약 사용자의 입력이 검증되지 않고,
그대로 `OS Command` 함수에 들어가게된다면
오른쪽 탭의 특수 문자를 이용해
사용자가 원하는 명령어를 함께 실행하게 될 수도 있습니다.

## 특수문자

### `&&`
**명령어 연속 실행**
한 줄에 여러 명령어를
사용하고 싶을 때 사용합니다.
앞 명령어에서 에러가 발생하지 않아야
뒷 명령어를 실행합니다.(Logical And)

> $ echo hello &&
> echo theori
> hello
> theori
-----
### `||`
**명령어 연속 실행**
한 줄에 여러 명령어를
사용하고 싶을 때 사용합니다.
앞 명령어에서 에러가 발생해야
뒷 명령어를 실행합니다.

> 1 : $ cat / || echo theori
> 2 : cat: /: Is a directory
> 3 : theori
-----
### `;`
**명령어 구분자**
한 줄에 여러 명령어를
사용하고 싶을 떄 사용합니다.
`;`은 단순히 명령어를
구분하기 위해 사용하며,
앞 명령어의 에러 유무와 관계 없이
뒷 명령어를 실행합니다.

> 1 $ echo hello;
> echo theori
> hello
> theori
-----
### `|`
**파이프**
앞 명령어의 결과가
뒷 명령어의 입력으로 들어갑니다.

> $ echo id | \bin\sh
> uid=1001(theori)
> gid=1001(theori)
> groups=1001(theori)
-----
### ``
**명령어 치환**
``안에 들어있는 명령어를 실행한 결과로
치환됩니다.

> echo \`echo theori\` theori
-----
### `$()`
명령어 치환
`$()`안에 들어있는 명령어를
실행한 결과로 치환됩니다.
이 문자는 ``와 다르게 중복 사용이 가능합니다.

> \$ echo $(echo
> theori)
> theori

## Command_Injection
`Command Injection` 취약점을 막기 위해서는
사용자의 입력 데이터가
Command 인자가 아닌 다른 값으로
해석되는 것을 막아야 합니다.

가장 좋은 방법은 웹 어플리케이션에서
`OS Command`를 사용하지 않는 것입니다.
웹 어플리케이션에서 필요한 `OS Command`가
라이브러리 형태로 구현되어 있으면
해당 라이브러리를 사용하고,
아니면 직접 짜는 것이 좋습니다.

> OS Command는 사용할 경우,
> 다른 취약점이 발생하는 등의 잠재적인
> 위협이 될 수 있습니다.

만약 OS Command에 사용자의 입력 데이터를
넣어 사용해야할 경우
필터링을 통해 방지해야합니다.

**화이트/블랙 리스트** 방식의 필터링으로
나눌 수 있습니다.

### - 정규식을 통한 화이트리스트방식 필터링
e.g. ping을 보내는 페이지의 경우
사용자가 입력한 ip address가 정상적인
ip address형식인지
정규식으로 검증 후 사용할 수 있습니다.

``` python
import re, os, ...
...
chk_ip = re.compile('^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')
if bool(chk_ip.match(ip)):
    return run_system(f'ping -c 3 {ip}')
else:
    return 'ip format error'
```

### - OS Command에서 Meta 문자로 사용되는 값을 필터링하고 따옴표로 감싸기

ping을 보내는 페이지의 경우
사용자가 입력한 ip adress를 따옴표로 감싸서 사용할 수 있습니다.

```python
if '\'' in ip:
    return 'not allowed character'
return run_system(f'ping -c 3 \'{ip}\'')
```
> Double Quotes(")를 사용할 경우
> **dollarsign($)** -> **backquote(`)**
> 이렇게 해석돼, 모든 입력을
> 문자열로 처리하는
> **Single Quotes(')**를 사용해야합니다.

### -execve args 인자로 사용
shell meta 문자로
해석되지 않게 입력 값을 넣습니다.
```Shell
subprocess.Popen(['ping', '-c', '3', ip]) # B
```

### - 기능에 해당하는 라이브러리 사용
사용하고자하는 기능을 OS커맨드가 아닌
구현된 라이브러리로 대체 가능합니다.
`ping3`는 소켓프로그래밍을 통해
ping기능을 구현한 라이브러리입니다.
```python
#! pip install ping3 
# https://github.com/kyan001/ping3/blob/master/ping3.py
import ping3
ping3.ping(ip)
```
> 라이브러리의 보안성 및 안전성 등을
> 검토한 후 사용하여야 합니다.