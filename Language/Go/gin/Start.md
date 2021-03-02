# Gin을 시작하자

## installation
- download
```shell
go get -u github.com/gin-gonic/gin
```

- import
```golang
import "github.com/gin-gonic/gin
```

### Optional
- for `http.StatusOK`
```golang
import "net/http"
```


## Quick Start
```golang
package main

import "github.com/gin-gonic/gin"
func main() {
    r:= gin.Default()
    r.GET("/ping", func(c *gin.Context){
        c.JSON(200, gin.H{
            "message" : "pong",
        })
    })
    r.Run()
}
```
위 코드는 0.0.0.0:8080/ping, localhost:8080/ping으로 브라우저를 이용하여 접속이 가능합니다.

