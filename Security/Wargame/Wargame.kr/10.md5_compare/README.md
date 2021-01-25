# md5_compare in php

1. 소스코드를 확인한다.
2. 첫번째 인자값은 문자열이며, 두번째 인자값은 숫자로 들어간다.
3. 만약 문자열 equal 숫자 로 표현하면 우리는 flag값을 얻을 수 있다.
4. md5 compare를 검색하고 md5 equal 코드를 찾자

[They are both float number format strings (numerical strings), and if you use == in php, when compare a number with a string or the comparison involves numerical strings, then each string is converted to a number and the comparison performed numerically.

Both of the strings are converted to 0 when compared with ==, if you want to compare them as string, remember to use ===(strict comparison) instead.] with stack overflow

->
> php에서 '=='를 사용하여 문자열과 숫자 문자열을
> 비교할 때 각 문자열을 숫자로 비교한다.
> 그러므로 '=='로 비교시 두 문자열 모두 0으로 반환이 된다.

그러므로
첫번째 인자값은 QNKCDZO
두번째 인자값은 240610708
을 넣어주면 된다.
