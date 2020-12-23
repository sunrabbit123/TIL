# QnA (error based SQLI)

근데 사실 `error based` 말고도 `Time based`방식으로 풀 수 있지만
저는 결과가 빨리 나오는걸 선호하기에 `error based`방식으로 풀 예정입니다.

1. 오른쪽에 보니 to JSMaster가 있는데
    이를 통해 DB를 거쳐 관리자에게 도착하는 것 같네요, QnA목록을 쌓아놓을면 저장소가 필요할테니 말이죠

2. 메세지를 적고 send를 보내니 `cont`, `mail`, `type` 세개의 인자값이 날라가는걸 인터셉트 할 수 있습니다.
세개 다 실행해본 결과 type에 취약점이 있음을 알 수 있었다.

3. 그래서 스크립트를 짜보았습니다.

    1. "select count(table_name) from information_schema.tables"
    2. "select table_name from information_schema.tables limit 70,1"
    3. "select column_name from information_schema.columns where table_name=0b01100001011101010111010001101000011010110110010101111001 limit 0,1"
    4. "select authkey from authkey"

근데 난 아직도 무슨 원리로 필터링이 되는지는 모르겠다.

3-3에서는 authkey를 필터링하더니 3-4에선 안하는거처럼 말이다
조건절에서만 필터링을 하는것인가