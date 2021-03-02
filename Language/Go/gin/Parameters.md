# 인자 값 전달에 대하여
1. [Parameters in path](#Parameters-in-path)
2. [Querystring parameters](#Querystring-parameters)
3. [return json](#return-json)

## Parameters in path

```golang
func main(){
    router := gin.Default()
    // 기본 라우터 생성

    router.GET("/user/:name", func(c *gin.Context){
        name := c.Param("name")
        c.String(http.StatusOK, "Hello %s ", name)
    })
    // :name 을 통해 name이라는 인자값을 얻을 수 있습니다.



    router.GET("/user/:name/*action", func(c *gin.Context){
        name := c.Param("name")
        action := c.Param("action")
        message := name + " is " + action
        c.String(http.StatusOK, message)
    })


    일치하는 각 요청마다, Path들은 정의를 유지합니다.
    router.POST("/user/:name/*action", func(c *gin.Context){
        c.FullPath() == "/user/:name/*action" // true

    })

    router.Run(":8080")
}
```

## Querystring parameters
```golang
func main() {
    router := gin.Default()
    
    // /welcom?firsname=Jane&lastname=Doe
    router.GET("/welcome", func(c *gin.Context){
        firstname := c.DefaultQuery("firstname", "Guest")
        lastname := c.Query("lastname")

        c.String(http.StatusOK, "Hello %s %s", firstname, lastname)
    })
    router.Run(":8080")
}
```

## return Json
```golang
func main(){
    router := gin.Default()

    router.POST("/form_post", func(c *gin.Context){
        message := c.PostForm("message")
        nick := c.DefaultPostForm("nick", "anonymous")

        c.JSON(200, gin.H{
            "status": "posted",
            "message": message,
            "nick" : nick,
        })
    })
    router.Run(":8080")
}
```
