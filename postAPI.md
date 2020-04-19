게시글
=
게시글 조회
-
```
GET /post
```
- Request
```
{
    
}
```
- Response
```
{
    Post.Objects.all()
}
```
```


```
게시글 작성
-
```
POST /post
```
 - Request
```
{
    title: String,
    author: User.id,
    created: DateTime,
    content: Text,
    image: Image,
    category: String,
    period: Date,
    price: Int,
    state: Boolean
}
```
- Response
```

```
```

```
게시글 세부 조회
-
```
GET /post/{Post.id}/
```
 - Request
```


```
- Response
```
{
    title: String,
    author: User.id,
    created: DateTime,
    content: Text,
    image: Image,
    category: String,
    period: Date,
    price: Int,
    state: Boolean
}
```
```


```
