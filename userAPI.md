회원
=
회원가입
-
```
POST /account/sign-up
```
- Request
```
{
    id: String,
    pw: String,
    nickname: String,
    email: String,
    phonenum: String
}
```
- Response
```
SUCCESS {"message": "Success"},status=200
```
```
FAIL {"message":"FAIL"},status=404
FAIL {"message": "User is already exists"},status=401

```
로그인
-
```
POST /account/sign-in
```
 - Request
```
{
    id: String,
    pw: String,
}
```
- Response
```
SUCCESS {
     id: String,
     pw: String,
     nickname: String,
     email: String,
     phonenum: String,
     token: String,
    },status=200
```
```
FAIL {"message":"FAIL"},status=400
FAIL {"message":"FAIL"},status=401
FAIL {"message":"FAIL"},status=404
```
로그아웃
-
```
POST/logout
```
 - Request
```


```
- Response
```


```
```


```