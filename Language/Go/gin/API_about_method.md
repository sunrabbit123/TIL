# API 작성하기

```Golang
func main() {
    router := gin.Default()
    기본적인 미들웨어를 생성합니다.
    로거 및 복구(무중단) 미들웨어입니다.

    router.GET("/someGet", getting)
    router.POST("/somePost", posting)
    .
    .
    .
    router.OPTIONS("/someOptions", options)

    router.RUN()
    
}
```

기본적으로 작동되는 포트는 8080포트이며, 다음과 같은 경우에 다른 포트에서 작동합니다.
1. 포트 환경변수가 설정되었을 경우
2. `router.Run(":3000")`처럼 변수가 들어갔을 경우


