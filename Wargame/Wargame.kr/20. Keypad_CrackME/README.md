# Keypad_CrackMe

It is second simple Reverse engineering at wargame.kr

1. download the CrackME2st.exe
2. open the CrackME2st.exe at dbg tool
3. you can look a assembler language code in dbg tool
4. It's a good judgment to look for strings
5. you can find the succes string at 4

```c
v3 = (const wchar_t **)((char *)v1 + 116);
v5 = _wtoi(*v3); //사용자가 입력한 값
v6 = Tm.tm mon + 1; //현재 달 정보

if( -201527 * v6 + v5 == 195,934,910){
AfxMessageBox(L"congratulations!",0,0);}
```
etc...