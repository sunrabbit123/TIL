# Injection

`Injection`공격은 사용자의 입력 데이터가
어플리케이션의 처리 과정에서
구조나 문법적인 데이터로
해석되어 발생하는 취약점을 의미합니다.

변조된 입력을 주입해 의도한 행위를
변질시켜 의도하지 않은 행위를 발생시킵니다.

## 목차

1. [SQL Injection](./SQL_Injection.md)</br>
SQL 요청을 사용할 때 공격자의 입력 값이
정상적인 요청에 영향을 주는 취약점이다.

2. [Command Injection](./Command_Injection.md)</br>
OS Command를 사용 시 사용자의
입력 데이터에 의해 실행되는
Command를 변조할 수 있는 취약점이다.

3. [Server Side Template Injection](./SSTI.md)</br>
템플릿 변환 도중 사용자의 입력 데이터가
템플릿으로 사용돼
발생하는 취약점이다.

4. [Path Traversal](./Path_Traversal.md)</br>
URL / File Path를 사용 시
사용자의 입력 데이터에 의해
임의의 경로에 접근하는 취약점입니다.

5. [server Side Request Forgery(SSRF)](./SSRF.md)</br>
공격자가 서버에서 변조된 요청을 보낼 수 있는 취약점입니다.


