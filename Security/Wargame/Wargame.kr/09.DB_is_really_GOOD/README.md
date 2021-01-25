# DB_is_really_Good, rellationship of DB and web

1. "/"를 입력하게 된다면 오류가 뜨면서 각종 path들이 보일 것 이다.
> then response "Fatal error: Uncaught exception 'Exception' with message 'Unable to open database: unable to open database file' in /
> var/www/html/db_is_really_good/sqlite3.php:7 Stack trace: #0 /var/www/html/db_is_really_good/sqlite3.php(7): SQLite3->open('./db/> 
> wkrm_admin...') #1 /var/www/html/db_is_really_good/memo.php(14): MyDB->__construct('./db/wkrm_admin...') #2 {main} thrown in /var/www/
> html/db_is_really_good/sqlite3.php on line 7"

2. DB파일을 찾는 path는 db_is_really_good/db/wkrm_[this]가 된다.
3. 우리는 admin의 파일을 원하기때문에 [this] 부분에 admin.db를 입력하게 된다면
admin으로 연결할 수가 있다.

4. 그렇게 얻어낸 DB파일을 열어서 확인하면 되지만, 만약 열 파일이 없다면 임의로 [txt파일](./wkrm_admin.txt)로 열면된다.
5. 그렇다면 ./dhkdndlswmdzltng.php 라는 링크를 얻게되는데 [이에 들어가게 된다면](http://wargame.kr:8080/db_is_really_good/dhkdndlswmdzltng.php) flag값을 얻을 수 있게 된다.
