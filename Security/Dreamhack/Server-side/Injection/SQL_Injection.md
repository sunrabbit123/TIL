# SQL Injection

## 목차

1. [개요](#개요)
2. [SQL이란](#SQL이란)
3. [SQL Injection](#SQL_Injection)

## 개요

SQL은 관계형 데이터베이스(RDBMS)의
데이터를 정의하고, 질의, 수정을 하기 위해
고안된 언어입니다.

DB에 의존하는 상당수의 웹 응용은 SQL를 사용해
데이터베이스와 상호작용합니다.

웹 응용에서 로그인/검색과 같이
입력 데이터를 기반으로 DBMS에 저장된 정보를
조회하는 기능을 구현하기 위해
SQL쿼리문에 입력 데이터를 추가해
DBMS에 요청합니다.

이 과정에 사용자의 입력이 SQL쿼리에 삽입돼,
SQL구문으로 해석되어,
개발자의 의도 외의 사태가 벌어질 수 있습니다.

즉 `SQL Injection`은 SQL 쿼리에
사용자의 입력 데이터가 삽입되어
사용자가 원하는 쿼리를 실행시키는
취약점입니다.

이 취약점이 발생하게 된다면,
쿼리를 실행하는 `DBMS의 계정`으로
공격이 가능하며,
DB에서 자료를 추출, 삭제, 추가 등의
행위가 가능합니다.

-----

## SQL이란
`SQL(Structured Query Language)`

이는 말 그대로 구조화된 형태를 가지는 언어이다.
올바른 구조로 요청해야만
DB가 이해하고 요청한 데이터를 수행하게 된다.

SQL은 사용 목적과 행우에 따라
다양한 구조가 존재하며
대표적으로 아래의 세가지가 존재합니다.

- [DDL](#DDL)(Data Definition language)
데이터를 정의하기 위한 언어이다.
데이터를 저장하기 위한 스키마,
데이터베이스의 **생성/수정/삭제** 등의
행위를 수행합니다.
</br>

- [DML](#DML)(Data Manipulation language)
데이터를 조작하기 위한 언어입니다.
실제 DB 내의 데이터에 대해
**조회/저장/수정/삭제**등의 행동을 수행합니다.
</br>

- DCL(Data control language)
DB의 접근 권한 등의 설정을 하기 위한 언어이다.
데이터베이스내에 사용자의 사용권한을
부여하기 위한 `GRANT`와 박탈하는 `REVOKE`
이 둘이 대표적인 DCL이다.

-----

### DDL
`DDL`(Data definition language)

대표적인 예시는 다음과 같다.

- CREATE</br>
새로운 데이터베이스 또는 테이블을 생성합니다.

```SQL
CREATE TABLE Board(
	idx INT AUTO_INCREMENT,
	boardTitle VARCHAR(100) NOT NULL,
	boardContent VARCHAR(2000) NOT NULL,
	PRIMARY KEY(idx)
)
```
위 명령어를 통해 원하는 컬럼을 가진
`Board`테이블을 생성 할 수 있습니다.
|idx|boardTitle|boardContent|
|:--|:---------|:-----------|
| | |

----- 
- ALTER</br>
데이터베이스 또는 테이블의 속성을 변경한다.

```SQL
ALTER TABLE Board ADD createdDate date;
```
위 명령어를 통해 테이블에 새로운 컬럼을 추가할 수 있습니다.(ex : createdDate)
|idx|boardTitle|boardContent|createdDate|
|:--|:---------|:-----------|:---|
| | | |
-----

- DROP</br>
데이터베이스 또는 테이블을 삭제합니다.
```SQL
DROP TABLE Board;
```


### DML
`DML` (Data manipulation language)

- INSERT</br>
테이블에 새로운 데이터를 추가합니다.
```SQL
INSERT INTO 
  Board(boardTitle, boardContent, createdDate) 
Values(
  'Hello', 
  'World !',
  Now()
);
```
이 명령어를 통해
테이블에 새로운 데이터를 추가할 수 있습니다.

|idx|boardTitle|boardContent|createdDate|
|:--|:---------|:-----------|:---|
|1|Hello|World!|20yy-MM-dd HH:mm:ss|

-----

- UPDATE</br>
테이블에 존재하는 데이터를 수정합니다.
```SQL
UPDATE Board SET
boardContent='DreamHack!' 
Where idx=1;
```
위 명령어를 통해 테이블에 존재하는
데이터를 수정할 수 있습니다.

|idx|boardTitle|boardContent|createdDate|
|:--|:---------|:-----------|:---|
|1|Hello|__DreamHack!__|20yy-MM-dd HH:mm:ss|

-----

- SELECT</br>
테이블에 존재하는 데이터를 조회합니다.
```SQL
SELECT 
  boardTitle, boardContent
FROM
  Board
Where
  idx=1;
```
위 명령어를 데이터베이스에 요청하여
아래와 같은 데이터를 얻을 수 있습니다.
```txt
    Hello, DreamHack!
```

-----

- DELETE</br>
테이블에 존재하는 데이터를 삭제합니다.
```SQL
DELETE From 
  Board
Where 
  idx=1;
```
위 명령어를 통해 테이블에 존재하는
데이터를 삭제할 수 있습니다.
|idx|boardTitle|boardContent|createdDate|
|:--|:---------|:-----------|:---|
|||||

## SQL_Injection

### 목차
-----
1. [개요](#개요)
2. [예시](#예시)
3. [해결방안](#해결방안)

### 개요
사용자의 입력 데이터가 SQL 쿼리에 들어가는
대표적인 예시로는 로그인 기능이다.
사용자가 아이디와 패스워드를
입력 및 서버에 전송하면

서버는 해당 데이터가 데이터베이스에
존재하는지 확인하고 로그인을 
성공시킬지 실패시킬지
판단할 수 있습니다.

`MySQL`에서의 로그인을 처리하는
가장 간단한 형태의 쿼리는 다음과 같다.
```SQL
select * from user_table
where ui='{uid}' and upw = '{upw}';
```

사용자가 값을 전송하면
`{uid}`와 `{upw}`에 
값이 대체되어 들어가고, DBMS에서 실행됩니다.

SQL에서는 `'`를 기준으로 문자열을 구분한다.
만약 입력에 `'`를 포함시켜 문자열을 탈출하고
새로운 쿼리를 작성하여 전달하면
DBMS에서 사용자가 입력한 쿼리를 실행시킬 수 있다.

### 예시
|idx|uid|upw|
|----|---|---|
|1|guest|guest|
|2|admin|********|

이런 테이블 구조를 가질 때,
`uid = guest`, `upw = guest`를 입력 시
guest정보를 출력하여 로그인이 됩니다.

admin의 upw를 알고 있지 않을 때
SQL Injection을 통해 논리적으로 참이 되는
구조를 만들어 admin으로 로그인이 가능합니다.

`or`연산은 양 측의 조건 중 하나만 만족하면 결과는 참이 됩니다.

이를 통해 `upw = 1'or '1`과 같은 
공격 페이로드를 통해 admin으로
로그인이 가능합니다.

### 해결방안
-----
이를 막기 위해서는
사용자의 입력 데이터가 SQL쿼리로
해석되지 않아야 한다.

`'`나 `"`과 같은 문자열 구분자를 
필터링하는 방법이 있지만,
이는 권장되지않는 방법이며

권장되는 방법으로는
`ORM`과 같이 검증된
SQL라이브러리를 사용하는 방법입니다.

이를 통해 개발자가 직접 쿼리를 작성하는
Raw 쿼리를 사용하지 않아도
기능구현이 가능하며,
SQL Injection으로부터 상대적으로 안전합니다.

이 `ORM`은 Object Relational Mapper의 약자로써
SQL의 쿼리 작성을 편리하게 돕기 위한 라이브러리입니다.
이는 생산성을 위해서도 사용되지만
사용자의 입력 값을 라이브러리 단계에서
알아서 escape하고 쿼리에 매핑하기에,
안전하게 SQL 쿼리를 사용가능합니다.

#### 예문
```python
from flask_sqlalchemy import SQLAlchemy
...
db = SQLAlchemy(...)
...
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(...)
    upw = db.Column(...)
    ...
User.query.filter(User.uid == uid, User.upw == upw).all()
```

> **주의사항**
> ORM을 사용하더라도
> 입력데이터의 타입 검증이 없다면
> 잠재적인 위협이 될 수 있으니,
> 입력 데이터의 타입 검증이 필요하다.

[Home](../../README.md) / [Back](./README.md)