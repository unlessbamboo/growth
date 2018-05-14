## 1 使用说明

### 1 参数

必选项：所有参数类型后面有!的表示该参数是必选的。

## 2 服务配置

### 2.1 主站和测试

主站：https://app.ilifdiary.com

测试:  https://test.app.ilifediary.com

### 2.2 图片服务

使用node.js服务，所有/media都转向该服务器，进行图片的上传操作

## 3 图片

### 3.1 图片上传

```js
// 图片表单
GET http://app.ilifediary.com/image/

// 图片upload
POST http://app.ilifediary.com/image/upload
```

### 3.2 图片尺寸

```json
// 默认
http://app.ilifediary.com/media/origin/image-name.jpg

// 大、中、小
http://app.ilifediary.com/media/large/image-name.jpg
http://app.ilifediary.com/media/medium/image-name.jpg
http://app.ilifediary.com/media/small/image-name.jpg
```



## 4 用户账号

### 4.1 Register

#### 4.1.1 步骤

* 通过手机号获取验证码，对于测试，则验证码默认为123456
* 验证手机号和验证码
* 检查手机号是否被注册
* 检查username是否被注册
* register and create

```css
/* 发送手机号和创建用户一起执行 */
mutation {
	sendPhoneMessage(data: {phone: "15210000001", purpose: "register", test: true}){
 		sent
 	}
    createUser(data: {username: "story1", phone: "15210000001", code: "123456", password: "12345678"}){
        user {
            username
            userType
            id
        }
    }
    login(data: {account: "story1", password: "12345678"}){
        user{
            id
            username
            phone
        }
    }
}
```



#### 4.1.1 Send Message

```Css
/* 
	测试验证码，默认不调用手机服务
	Input: 
		phone, purse: 必选
	output: success or failed
*/
mutation {
	sendPhoneMessage(data: {phone: "158571924025", purpose: "register", test: true}){
 		sent
 	}
}

/* 正式环境 */
mutation {
	sendPhoneMessage(data: {phone: "158571924025", purpose: "register"}){
 		sent
 	}
}
```

#### 4.1.2 Check Code

```Css
/* 
	确保数据库中有该条件的记录，并且未过期（没有使用、没有删除），配合上面的send_phone_message使用。
	output: 直接返回true/false 
*/
query {
 checkCode(phone: "158571924025", code: "123456", purpose: "register")
}
```

#### 4.1.3 Check Register

> 验证手机号、验证用户名

```Css
/* 验证用户名 */
query{
 checkRegister(username: "bifeng")
}
```

#### 4.1.4 create user

```Css
/*
	Input: 
		username, phone, code, password都是必选
		device目前有:web, phone
	output: UserNode
*/
mutation {
 createUser(data: {username: "bifeng", phone: "15210000001", code: "123456", password: "12345678"}){
   user {
     username
     userType
     id
   }
 }
}
```

#### 4.1.5 Reset Password

```css
/*
	Input:
		required: phone, code, password
	Output:
		success or failed
*/
mutation {
  resetPassword(data: {phone: "158571924025", code: "123456", password:"xxxxx"}){
    success
  }
}
```



### 4.2 login and logout

#### 4.2.1 Login User

> 为了测试方便，login和logout可以不使用Graph api来进行，具体见4.1.3.3说明
>
> 移动设备使用token来登录，每次登录都会刷新token；
>
> 允许web和phone同时登录，所以在登录时最好传递device以便后端区别对待

##### 4.2.1.1 Login User

```Css
/*
	Input: account(可以为username、email、phone，目前username为空)
	Output: 
*/
mutation{
 login(data: {account: "bifeng", password: "ab123456"}){
   user{
     id
     username
     phone
   }
 }
}

/* Token */
mutation{
 login(data: {token: "6449197d04485e3d964dd6e28bd2768e71e1fab8"}){
   user{
     id
     username
     phone
   }
 }
}
```

##### 4.2.1.2 Login Admin

```css

/* 管理员登录：目前有三个管理员（ilifediary, yinjie, zhangxiaoxiao）具体密码见密码记录*/
mutation{
 login(data: {account: "ilifediary", token: "046242160fcc6fb73ae9574900b16b4b97d19c63"}){
   user{
     id
     city
     username
     userType
   }
 }
}
```

##### 4.2.1.3 login Url

* login: https://app.ilifediary.com/origin/login/
* Logout: https://app.ilifediary.com/origin/logout/

#### 4.2.2 Logout User

```Css
/* 对于手机端，登出之后立刻将token设置为过期 */
query {
 logout
}
```

### 4.3 Update

#### 4.3.1 Change Password

```css
/*
	Input: oldPassword-required, password-required
	output: UserNode
*/
mutation{
	updateUser(data: {oldPassword: "123", password: "234"}){
    user{
      id
      username
      userType
      articles{
        id
        author
        tags
      }
      socials{
        id
        uid
        accessToken
      }
    }
  }
}
```

#### 4.3.2 Update User info

```css
/*
	Input: avatar, tagline
*/j
mutation{
	updateUser(data: {
      avatar: "https://app.ilifediary.com/media/origin/teLXqc-1501753784402.jpeg"
    }
  ){
    user{
      id
      username
      userType
      articles{
        id
        author
        tags
      }
      socials{
        id
        uid
        accessToken
      }
    }
  }
}
```

### 4.4 Token

#### 4.4.1 Fresh Token

```css
/*
	Input: 无，默认为当前登录用户的token
	Output: tokenType
*/
mutation{
  refreshToken{
    token{
      key
      device
      expired
    }
  }
}
```

#### 4.4.2 Defer Token

增加token的使用日期。

```css
/*
	Input: 无
	Output: TokenType
*/
mutation{
  deferToken{
    token{
      key
      device
      expired
    }
  }
}
```



### 4.5 Query

#### 4.5.1 Query a User

##### 4.5.1.1 Common

```Css
/* 已登录用户 */
{
 me{
   id
   username
   userType
   token{
     key
     device
     expired
   }	
 }
}

/* 某一个用户, 不能获取敏感信息否则报错,例如token, access_token */
{
  user(id: "679b78d8d141c8"){
    nickname
    token
    socials{
      accessToken
      email
    }
  }
}


```

##### 4.5.1.2 Pagination

```css
/* 使用分页获取用户基本信息, 其中articles也会进行分页 */
{
  users {
    totalCount  /* 总数量 */
    edges {
      node {    /* 节点数据 */
        id
        articles {
          edges {
            node {
              id
            }
          }
        }
      }
      cursor    /* 每一个节点的cursor值 */
    }
  }
}
```



#### 4.5.2 Query some users

```css

/* 管理员 */
query{
 users(userType: "xinshu"){
    id
    username
    userType
    token{
      key
      device
    }
  }
}

/* 管理员--查询某一个昵称的用户 */
query {
  users(nickname: "张小") {
    id
    username
    userType
    token{
      key
      device
    }
  }
}
```

#### 4.5.3 Query Token

```Css
/* Input：key, Output: TokenType */
query{
 token(key: "66c7d584200e2d4a56f880187c689292108511cd"){
   key
   device
   expired
 }
}
```

### 4.6 Sync

#### 4.6.1 流程

用户在ilifdiary.com进入"原创内容时"，需要调用该接口（相当于正常情况下的login）。

传入参数：：传入ilifediary.com的uid, token信息。

管理后台操作：从ilifedairy.com同步user, social_user信息，如果app.ilifediary.com不存在则创建新用户并自动login

输出：返回在app.ilifediary.com登录成功后的用户信息

#### 4.6.2 例子

```css
/*
	
	output: success
*/
mutation{
  syncUser(uid: "2a4395646b", key: "b07074650f103ccd72abb6a3d969bf44cf085534", device: "web") {
    user{
      id
      username
      token{
        key
      }
    }
  }
}
```



## 5 书籍

### 5.1 Book Mutation

#### 5.1.1 Create Book

```Css
/* Input: 文章标题, output: book */
mutation{
  createBook(data: {title: "我的前半生"}){
    book{
      title
      author
      cover
      user{
        username
        id
      }
      articles{
        user{
          id
          username
        }
        content
      }
    }
  }
}
```
#### 5.1.2 Update Book

```css
/* 
	input: 
		bid, title, author, cover, article_order 
	output: 
		BookNode

	其中article_order用于更改文章在chapter中的顺序，可能的值有：
      {
          "move": 需要操作的aid，
          "bifore": 插入位置
          "after": 插入位置
          "newOrder、new_order": 新的顺序
      }
*/
mutation{
  updateBook(data: {bid: "da4d7f30c0b2", title: "我的后半生", author: "狂想"}){
    book{
      title
      author
      cover
      user{
        username
        id
      }
      articles{
        user{
          id
          username
        }
        content
      }
    }
  }
}
```



#### 5.1.3 Delete Book

```css
/*
	Input: bid
	Output: success
*/
mutation{
  deleteBook(bid: "6f6cf37f40e0"){
    success
  }
}
```



#### 5.1.4 Recover Book

```css
/*
	Input: bid
	Output: success
	
	对应Delete Book EndPoint
*/
mutation{
  recoverBook(bid: "6f6cf37f40e0"){
    success
  }
}
```



#### 5.1.5 batch delete books

```css
/*
	Input: bids(list)
	Output: success
*/
mutation{
  deleteBooks(bids: ["6f6cf37f40e0"]){
    success
  }
}
```

#### 5.1.6 Batch Recover Books

```css
/*
	Input: bids(list)
	Output: success
*/
mutation{
  recoverBooks(bids: ["6f6cf37f40e0"]){
    success
  }
}
```



### 5.2 Book Query

#### 5.2.1 query a book

##### 5.2.1.1 Common

```css
/* input: id, output: BookNode */
query{
  book(id: "6f6cf37f40e0") {
    id
    user{
      id
      username
      userType
    }
    pageNum
  }
}

/* 
	获取详细的书籍信息，逐层到获取layout排版信息 
	deleted: 获取未删除书籍
	empty: 默认不返回空书籍，如果为true，则返回所有空的书籍
*/
query{
  book(id: "85a869ff80bc"){
    id
    title
    pageNum
    current{
      id
      uid
      title
      current{
        id
        title
        layout{
          id
          pages
          pageCount
        }
      }
    }
  }
}
```

##### 5.2.1.2 Pagination

```css
/* 获取所有书籍 */
{
  books(whole:true) {
    totalCount
    edges {
      node {
        id
      }
      cursor
    }
  }
}

{
  books(whole:true, first: 10, after: "YXJyYXljb25uZWN0aW9uOjk=") {
    totalCount
    edges {
      node {
        id
        title
      }
      cursor
    }
    pageInfo {
      hasNextPage
      endCursor
    }
  }
}
```



#### 5.2.2 query some books

```css
/*
	Input: uid(or current login user), deleted
	Output: BookNode
*/
query {
  books(uid: "3b1c5b78ceb370"){
    id,uid, sid, sourceSite, public, status
    chapters
    author
    cover
    title
    pageNum
  }
}

/* 多本书 */
query{
  books(deleted: false, empty: false){
    id
    title
    pageNum
    current{
      id
      uid
      title
      current{
        id
        title
        layout{
          id
          pages
          pageCount
        }
      }
    }
  }
}
```

#### 5.2.3 Sync Book

```css
/* 
	用于ilifediary.com请求app.ilifediarya.com，同步欲定稿书籍信息
*/
syncBook(id: "41575befa596", uid: "71ab0fad6c41b1"){
  id
  title
  pageNum
  current{
    id
    title
  }
}
```

### 5.3 Book Typeset

```css
/* 触发排版 */
mutation{
  typesetBook(bid: "971ebdd046d5"){
    success
  }
}
```



## 6 文章

### 6.1 Article Mutation

#### 6.1.1 Create Article

##### 6.1.1.1 Create Simple Article

```css
/* input: bid, title, output: ArticleNode */
mutation{
  createArticle(data: {bid: "6f6cf37f40e0", title: "我的12岁生涯"}){
    article{
      id
      title
      content
      user{
        id
        username
        userType
        avatar
      }
    }
  }
}
```

##### 6.1.1.2 Create Article with multiple Paragraphs

```css
mutation{
  createArticle(data: {
    title: "Test1", 
    cover: {
      cover: "http://ilife.xinshu.me/upload/media/SU1HXzI4NTUuSlBHPzE1MDMyODUxNzgxNjM3MmY1ZDIzODE3ZjhkMQ==",
      width: 2000,
      height: 3000,
    },
    paragraphs: [
      {
      	elements: [
        	{
          		tag: "img", 
          		src: "http://image.nationalgeographic.com.cn/2017/0726/20170726030039849.jpg",
				w: 990,
          		h: 620
        	}
        ]
      },
    ]
  }){
    article{
      id
      title
      content
      user{
        id
        username
        avatar
      }
      bid
    }
  }
}
```



#### 6.1.2 Update Article

```css
/* Input: 
	aid: required
	title, author, 
	paragraphOrder:
		move: operate paragraph id
		before: the paragraph's pid where you want to add paragraph before
		after: the paragraph's pid where you want to add paragraph after 
*/
/* Output: ArticlenNode */
mutation{
  updateArticle(data: {aid: "7ac0d1bad0c7a8", author: "伟大的10岁的郑碧峰"}){
    article{
      id
      title
      author
      user{
        id
        username
        userType
        avatar
      }
    }
  }
}

/* 更改paragraph顺序 */
mutation{
  updateArticle(data: {
    aid: "e63522bb05f6f5", 
    paragraphOrder: {
      move: "3d49e2",
      after: "44e871"
    }
  }){
    article{
      id
      title
      author
      content
      user{
        id
        username
        userType
        avatar
      }
    }
  }
}
```

#### 6.1.3 Update Article Content

```css
/*
	更新文章内容
*/
/* 所有paragraphs都为新的内容 */
mutation{
  updateArticle(data: {
    aid: "1dd0a7dedcf1e0",
    title: "文章标题1"
    content: {
      paragraphs: [
        {
      	 		elements: [
                {tag:"p", id:"e7bf72", text:"狂想写作本"},
                {tag:"img", src:"http://image.nationalgeographic.com.cn/2017/0726/20170726030039849.jpg",h:620,w:990}
            ]
        },
        {
      	    elements: [
                {tag:"p", id:"e7bf72", text:"狂想写作本2"},
                {tag:"img", src:"http://image.nationalgeographic.com.cn/2017/0726/20170726030039849.jpg",h:620,w:990}
            ]
      	},
      	{
      	    elements: [
                {tag:"p", id:"e7bf72", text:"狂想写作本3"},
                {tag:"img", src:"http://image.nationalgeographic.com.cn/2017/0726/20170726030039849.jpg",h:620,w:990}
            ]
      	}
      ]
    }
  }){
    article{
      id
      content
    }
  }
}

/* 部分Paragraph为旧的paragraph */
mutation{
  updateArticle(data: {
    aid: "53a299a2219c4c",
    content: {
      paragraphs: [
        {
         	id: "7fc4e7",
      	 	elements: [
                {tag:"p", id:"e7bf72", text:"狂想写作本"},
                {tag:"img", src:"http://image.nationalgeographic.com.cn/2017/0726/20170726030039849.jpg",h:620,w:990}
            ]
        },
        {
      	 	elements: [
                {tag:"p", id:"e7bf72", text:"狂想写作本3"}
            ]
        },
        {
          	id: "cff83a"
      	    elements: [
                {tag:"p", id:"e7bf72", text:"狂想写作本2"},
                {tag:"img", src:"http://image.nationalgeographic.com.cn/2017/0726/20170726030039849.jpg",h:620,w:990}
            ]
      	}
      ]
    }
  }){
    article{
      id
      content
    }
  }
}
```



#### 6.1.4 Delete Article

```css
/*
	Input:bid, aid
	Output: success
*/
mutation {
	 deleteArticle(
		aid: "060b1717fa5da6",
        bid: "6f6cf37f40e0"
  	) {
	 	success
	 }
}
```

#### 6.1.5 Batch Delete Article

```css
/*
	Input: bid, aids(list),
	Output: success

	实际上，利用迭代器逐一删除
*/
mutation{
  batchDeleteArticles(bid: "6f6cf37f40e0", aids: ["e63522bb05f6f5", "7ac0d1bad0c7a8"]){
    success
  }
}
```



###  6.2 Article Query

#### 6.2.1 Qrticle Query

```css
/* input: id  output: ArticleNode */
query{
  article(id: "72394da3136fa5"){
    id
    title
    content
    user{
      id
      username
      userType
    }
  }
}
```



#### 6.2.2 Articles Query

##### 6.2.2.1 List

```css
/* input: cid, bid, uid, user_self   output: ArticleNode */
/* 其中cid>bid>uid>user_self */
query{
  articles(uid: "517ef24d2416d3"){
    id
    title
    content
    user{
      id
      username
      userType
    }
  }
}

query{
  articles(bid: "6f6cf37f40e0"){
    id
    title
    content
    user{
      id
      username
      userType
    }
  }
}
```

##### 6.2.2.2 Paginator

```css
{
  articles(first: 10) {
    totalCount
    edges {
      node {
        id
        title
        uid
        stat {
          aid
          viewC
          likeC
          shareC
          collectionC
          subscriptionC
          commentC
          score
          active
        }
      }
      cursor
    }
    pageInfo {
      hasNextPage
      hasPreviousPage
      startCursor
      endCursor
    }
  }
}
```



#### 6.2.3 Active Articles Query

```css
query{
  activeArticles{
    id
    title
    content
    user{
      id
      username
      userType
    }
  }
}
```



## 7 段落

### 7.1 Paragraph Mutation

#### 7.1.1 Add Paragraph

##### 7.1.1.1 Add a Paragraph

```css
/* Input: 
	aid(required): 	文章标题
	elements(required): [{"tag":"p", "text":"def","style":"bold;"}, ...]
	before: "the paragraph's pid which you want to add paragraph before"
	after: "the paragraph's pid which you want to add paragraph after"
	关于elements的格式，请见《业务文档说明》
*/

/* Output:
	paragraph
*/
mutation {
	 addParagraph(data: {
		aid: "72394da3136fa5",
    	elements: [
        	{tag: "p", text: "abc", style: "blod;"},
        	{
          		tag: "img", 
          		src: "http://image.nationalgeographic.com.cn/2017/0726/20170726030039849.jpg",
				w: 990,
          		h: 620
        	}
      
      	]
  	}) {
	 	paragraph
	 }
}


/* 每一个paragraph中仅仅存在一个text或者一个img，TODO */
mutation {
	 addParagraph(data: {
		aid: "e63522bb05f6f5",
    	elements: [
      		{
              tag: "a",
              url: "https://www.google.com",
              text: "谷歌大天朝"
      		}
      	]
  	}) {
	 	paragraph
	 }
}
```

##### 7.1.1.2 Batch add multiple Paragraph

```css
/*
 	Input: aid， paragraphs
*/
mutation{
  batchAddParagraphs(data: {
    aid: "231a20054367f6", 
    paragraphs: [
      {
      	elements: [
        	{tag: "p", text: "abc"},
        	{
          		tag: "img", 
          		src: "http://image.nationalgeographic.com.cn/2017/0726/20170726030039849.jpg",
						w: 990,
          		h: 620
        	}
        ]
      },
      {
        elements: [
        	{tag: "p", text: "abc"},
        	{
          		tag: "img", 
          		src: "http://image.nationalgeographic.com.cn/2017/0726/20170726030039849.jpg",
				w: 990,
          		h: 620
        	}
      	],
      }
    ]
  }){
    article{
      id
      title
      content
      user{
        id
        username
        userType
        avatar
      }
    }
		success
  }
}
```



#### 7.1.2 Update Paragraph

```css
/* Input:
	aid: required
	pid: required
	elements: 直接替换已有的Paragraph
	modifyElement: 
        {action:delete, id: element_id},
		{action:update, id: element_id, element: new_element_value}
		{action:add, element: new_element_value}
   Output:
	Paragraph
*/
mutation {
	 updateParagraph(data: {
		aid: "e63522bb05f6f5",
        pid: "44e871",
    	modifyElement: {
          action: "add",
          element: {
            tag: "img",
            src: "http://image.nationalgeographic.com.cn/2017/0726/20170726030039849.jpg",
            w: 990,
            h: 620,
          }
    	}
  	}) {
	 	paragraph
	 }
}


/* 确保所有text/image在某一个段落里面仅仅有一个 */
mutation {
	 updateParagraph(data: {
		aid: "e63522bb05f6f5",
        pid: "44e871",
    	modifyElement: {
          action: "update",
		  id: "93ab94"
          element: {
            tag: "a",
            text: "谷歌大大的天朝",
            url: "https://www.google.com"
		  }
    	}
  	}) {
	 	paragraph
	 }
}

mutation {
	 updateParagraph(data: {
		aid: "e63522bb05f6f5",
        pid: "44e871",
    	modifyElement: {
          action: "delete",
		  id: "7964cf"
    	}
  	}) {
	 	paragraph
	 }
}

```

#### 7.1.3 Delete Paragraph

```css
/*
	Input: aid, pid
	Output: success
*/
mutation {
	 deleteParagraph(
		aid: "e63522bb05f6f5",
        pid: "144dc6"
  	) {
	 	success
	 }
}
```

### 7.2 Paragraph Query

#### 7.2.1 Query a Paragraph

```css
/*
	Input: aid, pid, they are all required.
	Output: paragraph object
*/
{
  paragraph(aid: "e63522bb05f6f5", pid: "44e871")
}
```

#### 7.2.2 Query paragraphs

```css
/*
	Input: aid
	Output: [paragraph1, paragraph2, ..., paragraph-N]
*/
query{
  paragraph(aid: "749a078fce243d", pid: "971a59")
  paragraphs(aid: "749a078fce243d")
}
```



## 8 排版

### 8.1 Layout Mutation

### 8.2 Layout Query

#### 8.2.1 article layout

```css
/*
	Input: aid, typeset_type, they are all required
	Output: LayoutNode
	
	如果该aid没有排版完成，会再次触发排版操作
*/
{
  articleLayout(aid: "e63522bb05f6f5", typesetType: "a5-waterfall-blog"){
    id
    sourceId
    sourceType
    pages
    pageCount
  }
}
```

#### 8.2.2 book layout

```css
/*
	Input: bid, typeset_type, they are all required
	Output: LayoutNode

	注意，该节点返回的是book中所有articles的集合对象，souce_type变为book，结构同单一layoutnode保持一致
*/
{
  bookLayouts(bid: "6f6cf37f40e0", typesetType: "a5-waterfall-blog"){
    status
    sourceId
    sourceType
    pages
    pageCount
  }
}
```

### 8.3 触发排版

> 触发排版操作，为了心书预览调用，同老版本的接口调用保持一致

#### 8.3.1 排版文章

##### 8.3.1.1 API

/api/0.1/articles/aid/typeset/

##### 8.3.1.2 response

```json
{
  "data": {
    // 排版完的数据
    "pages": layout.pages,
    "source_id": aid,
    "source_type": "article",
    // 排版类型
    "type": layout.typeset_type,
    // 文章总页数
    "page_num": layout.page_count
  },
  "request": "success"
}
```

##### 8.3.1.3 introduction

article的总页数可以在graphql中的article_node中的pageNum获取，但是不保证该值时最终排版完成的文章总页数，所以一般情况下请调用该API获取最终的总页数。

#### 8.3.2 排版书籍

##### 8.3.2.1 API

/api/0.1/books/bid/typeset/

##### 8.3.2.2 response

```json
{
  "data": {
    "pages": pages,
    "source_id": bid,
    "source_type": "book",
    "type": typeset_type,
    "page_num": len(pages)
  },
  "request": "success"

}
```

##### 8.3.2.3 introduction

见8.3.1.3关于article的说明，大体情况一致。

## 9 社交账号

### 9.1 Social Oauth

社交账号的授权和登录流程同老版本的登录授权是完全一致的。

#### 9.1.1 Facebook

```json
// facebook登录与返回值
https://app.ilifediary.com/socials/facebook_login

// 返回URL

```



### 9.2 Social Query

#### 9.2.1 Query a Social

```css
/*
	Input: id(social user id)
	Output: SocialNode
*/
{
  social(id: "8b7361c4a5f659"){
    id
    socialId
    uid
    username
    location
    gender
  }
}
```







## 10 Django graphene测试

> 基于项目grocery-shop/project/graphql/cookbook测试结果

### 10.1 测试basic schma

```Python
# 在顶级schema中创建一个echo回复query
import graphene

class Query(graphene.ObjectType):
 hello = graphene.String(name=graphene.Argument(graphene.String, default_value="stranger"))

 def resolve_hello(self, args, context, info):
 return 'Hello ' + args['name']

schema = graphene.Schema(query=Query)
# 在shell上就可进行测试
from cookbook.schema import schema
result = schema.execute('{ hello }')
```



### 10.2 创建ingredients


```python
from cookbook.schema import schema
# 确保category存在,其中在InputField和OutputField上确保外键category能够正确的处理
desc = """mutation {
 createIngredient(name: "ingredient3", categoryId: 1){
 	outputIngredient{
 		name
 		notes
 		category{
 			id
 			name
 		}
 	}
 }
}"""
result = schema.execute(desc)
print result.data
```


## 11 数据互通与签名

### 11.1 默认签名

#### 11.1.1 功能

见notion中的说明:https://www.notion.so/2-f9b94b9aae57448ba4f02dcd909795cb

#### 11.1.2 api

见 notion 说明

#### 11.1.3 action

见 notion 中说明

#### 11.1.4 example

```css
/*
	用户个人信息同步签名
*/
{
  sign(action: "sync", device: "web")
}

/*
	书籍预览签名
*/
{
  sign(action: "preview", device: "web", bid: "1234556")
}
```



### 11.2 自定义签名

#### 11.2.1 功能

输入自定义的签名信息, 进行签名操作, 一般用于开发者自己使用

### 11.2.2 api

```css
/*
	自定义签名
*/
{
  customSign(
    sid: "105185093335445",
    action: "sync",
    source: "facebook",
    device: "web"
  )
}
```

## 12 书籍状态

### 12.1 book

### 12.2 article

### 12.2.1 like

```css
/*
	喜欢某一篇文章, 用户必须登录, aid必须存在
*/
mutation{
  updateArticleStat(data: {
    aid: "19fa3d99099832",
    stat: "like_c",
    action: "increase"
  }){
    article{
      id
      title
      stat{
        viewC
        likeC
        subscriptionC
      }
      trace
    }
  }
}
```

