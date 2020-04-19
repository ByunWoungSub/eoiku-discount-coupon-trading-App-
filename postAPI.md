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
    id: Int,
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

게시글 수정
-
```
PUT /post/{Post.id}
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

게시글 삭제
-
```
DELETE /post/{Post.id}
```
- Request
```
{
    
}
```
- Response
```


```
```


```
