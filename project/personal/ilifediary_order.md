#iLifeDiary与 Openbook对接



## 1. 预览

> ***2.0 --> openbook ，跨域进行书籍预览操作***

### 1.1 url

#### 1.1.1 url值

```json
https://[test-]mp.xinshu.me/preview/?source_url=q:base64_str
```
#### 1.1.2 base64算法

> ***所有与openbook交互的请求都采用这种格式，对参数进行base64编码封装，下面章节不再另加说明***

```python
query = {
  'bid': 'xxx',
  'uid': 'xx',
  'timestamp': 123123123,
  'source': 'ilifediary',
  'redo': true/false, # false就不要传递这个参数,
  'host': 'app.ilifediary.com',
  'sign': 'xxxx'
}
base64_str = base64.b64encode(json.dumps(query).encode('uft8'))
```



### 1.2 query 

> ***凡是在这里进行注释的参数，在其他接口中都不再说明，请注意***

```json
- bid				书籍id
- uid				用户id
- timestamp         时间戳
- source            社交来源，这里特指相对于openbook的数据来源，不同于下面的sid/source值
- host      		域名信息       
- redo 				是否触发排版操作，true-则触发； 若为false，则一般不携带该字段
- sign				签名值
```

### 1.3 签名算法

#### 1.3.1 拼接规则

所有的sign拼接规则如下，下面章节不再说明：

- 全部为字符串，即所有其他类型都转为str类型
- 按照query和key的首字母排序，如果首字母相等，依次类推，例如对于参数:abc,dbc的签名就是：sign(abc+dbc)

#### 1.3.2 算法

> ***注意，这里的拼接并非无序的，请依照1.3.1的规则进行拼接操作。***

sign=md5(sort_and_join_all_string(key + 其他参数))

#### 1.3.3 例子

// 预览未定稿书籍，在2.0上调用，bid为预排版预览的书籍id值：

```python
{
  "data": {
    "xinshuSign": {
      "openbook_url": "https://test-mp.xinshu.me/preview/",
      "source_url": "q:eyJob3N0IjogImh0dHBzOi8vdGVzdC5hcHAuaWxpZmVkaWFyeS5jb20iLCAiYmlkIjogIjI2ZmVkODc0OTMxOSIsICJyZWRvIjogdHJ1ZSwgInNpZ24iOiAiMmE4MzQzOTEzNjk2ZmRhZTQxMTBiNjBkOTBhYzk0ODQiLCAidWlkIjogImMyZjc5YjU0Mzk3ZGYwIiwgInRpbWVzdGFtcCI6IDE1MDM1NjM4NTMsICJzb3VyY2UiOiAiaWxpZmVkaWFyeSJ9"
    }
  }
}
```



// 预览已定稿书籍，在1.0上调用，里面的bid是下单后Openbook返回的定稿书籍id值：

```python
{
    "data": {
        "openbook_url": "https://test-mp.xinshu.me/preview/",
        "source_url": "q:eyJ1aWQiOiAiMzFiOTZkMGM0MSIsICJ0aW1lc3RhbXAiOiAxNTAzNTYzNjU2LCAiYmlkIjogIjI2ZmVkODc0OTMxOSIsICJzaWduIjogImJkOWU5OThkMzJiNTdkYWM3M2NlNzZmMTQ4ZDA1NGJjIiwgInNvdXJjZSI6ICJpbGlmZWRpYXJ5IiwgImhvc3QiOiAiaHR0cDovLzEyNy4wLjAuMTo4MDgwIn0="
    },
    "request": "success"
}
```





## 2. 获取书籍内容

> ***openbook  --> 2.0， 从ilifediary上获取整本书（不是文章）的预览信息***

### 2.1 url
```Json
https://app.ilifediary.com/book/<bid>/content?uid=123&sign=12311254&timestamp=123123
```
### 2.2 query 

```json
- bid
- uid
- timestamp
- sign
```

### 2.3 签名算法

***拼接规则见1.3.1***

### 2.4 response	

```javascript
{
    "data": {
      	"host": "https://app.ilifediary.com（当前域名值）",
        "post_date": 1502823944,
        "source": "ilifediary",
        "avatar": "头像URL",
        "cover": {
          	"height": 848,
          	"width": 1280,
            "image": "绝对路径URL"
        },
        "share": "文档预览的URL，绝对路径",
        "title": "文档标题",
        "author": "文档作者",
      	// chapter id
        "chapters": [
        	{
              "cid": "chapter id",
              "articles": [
                {
                  "id": "article id",
                  "title": "文档标题",
                  "content": {// 文章内容
                    "paragraphs": [
                      {
                        "elements": [
                          {
                            "id": "d24efb",
                            "h": 848,
                            "w": 1280,
                            "src": "绝对路径URL",
                            "tag": "img"
                          }
                        ],
                        "id": "85acd1"
                      }
                    ]
                  }
                }
              ]
           }
        ]
    },
    "request": "success"
}
```



## 3. 同步排版状态

> ***openbook--->2.0，用于通知2.0此时排版操作完成，以便2.0更新DB中的文章排版状态版本号，避免下次再次调用1.0-"预览"接口时触发排版***

### 3.1 url

```json
https://app.ilifediary.com/book/<bid>/notification?typeset=1&timestamp=123456&sign=
```

### 3.2 query

```json
- typeset			1--书籍已经排版结束
- timestamp
- sign
```



### 3.3 签名算法

***拼接规则见1.3.1***

### 3.4 response

```javascript
{
    "request": "success"
}
```



## 4. 付款结算 

> ***openbook-->1.0，传递下单所需的基本信息用于在1.0进行如下操作：伪造定稿书籍、创建订单并进行付款操作***

### 4.1 url

> URL 发生变动, /orders/pay/ --> /orders/detail/

```json
https://[beta.]ilifediary.com/orders/detail/?bid=123&sid=123&source=facebook&sign=&..
```
### 4.2 query 

> ***所有下面的信息暂时为初版，请openbook这边根据实际情况进行更改，之后1.0再进行相应改动。***

#### 4.2.1 书籍基本数据

```json
- bid: 原始书籍 bid 
- page: 书籍总页数
- title: 书籍标题
- author：书籍作者
- template：书籍封面模板
- code_name: 封面类型（用于在1.0的书架页上显示书籍简单信息）
- image：封面图片url，绝对路径
- version: 版本号
- timestamp
- sign
```



### 4.3 response

该请求在1.0的后台处理，并且直接返回一个指向1.0主站的redirect_url，openbook必须处理好各种错误返回以及进行重定向操作。

```json
{
  "data": {
    "redirect": https://[beta.]ilifediary.com/login/?uid=&token=&bid=&state=&action=
  }
}
```

### 4.4 签名算法

#### 4.4.1 算法

***拼接规则见1.3.1***

该接口目前仅仅对如下字段进行签名：bid, page, sid, source, timestamp，如果需要对全部字段都做签名请告知。

#### 4.4.2 例子

```python
"""
  - bid: 原始书籍 bid 
  - page: 书籍总页数
  - title: 书籍标题
  - author：书籍作者
  - template：书籍封面模板
  - code_name: 封面类型（用于在1.0的书架页上显示书籍简单信息）
  - image：封面图片url，绝对路径
  - version: 版本号
  - timestamp
  - sign
"""
from apps.sign.services import *
from apps.utils import get_redirect
d = {
  'bid': '52941d4d6098',
  'page': 27,
  'title': 'run',
  'author': 'xiaoxiao',
  'template': 'type-1',
  'code_name': 'Cover-23',
  'image': 'http://ilife.xinshu.me/upload/media/MjAxNzA4MDMxMjU5NDg3MTQuanBnPzE1MDMzMTIzODMzMDZjMmY3OWI1NDM5N2RmMA==',
  'timestamp': 123456,
}
d = SignService.sign(d)
url = 'http://127.0.0.1:8080/orders/detail/?'
print(get_redirect(url, **d))
```





## 5. 付款成功通知

> ***1.0--->openbook，告知订单的创建和付款完成，以便openbook启动自动打印流程，另外此操作为同步操作，调用方需要等待接收方定稿并返回定稿后的书籍id信息以便更新Order表***

### 5.1 url

如果还需要其他字段，请告知

```json
https://[test-]mp.xinshu.me/?order_id=123&bid=76876888&timestamp=898979253&sign=
```
### 5.2 query 

```json
- order_id：订单号
- bid: 原始书籍id信息(这里写成origin_bid_1234，下面会引用)
- timestamp
- sign
```

### 5.3 response

在1.0付款完成后，会等待openbook对书籍origin_bid_1234进行finalize_book操作，并返回最终定稿的书籍id（layout_bid__1234），具体返回Json格式如下（若需改动，请openbook这边改动并通知即可）：

```json
{
  "data": {
    // 定稿之后的新的书籍id，不同于原始书籍id，1.0会将该值填入order中
    "bid": 'layout_bid_1234'
  },
  "request": "success"
}
```

### 5.4 签名算法

#### 5.4.1 算法

***拼接规则见1.3.1***

#### 5.4.2 例子

```python
from apps.book.services import *
d = {'order_id': '0829792', 'timestamp': 1503976502, 'bid': u'f1e2443d92b7', 'sign': '244bedad7084c7dafcfb1e670e90c137', 'source': u'origin', 'version': 0}

sign = sign_service.sign(d)
print sign
```





## 6.  订单状态和快递信息更改

> ***openbook---->1.0，用以通知1.0某一个订单当前的状态和快递信息，用于订单打印中***

### 6.1 url
```json
// 订单状态
https://ilifediary.com/orders/<order_id>/status/?sign=&status=xxx&timestamp=

// 快递信息
https://ilifediary.com/orders/0829797/status/?ship_company=shunfeng&ship_no=123456&timestamp=123456&sign=05085f10c58ccf5c9ee3e285176cc031&status=4
```
### 6.2 query 

#### 6.2.1 状态值

- 0---未支付
- 1---支付
- 2---生成了Pdf
- 3---已打印成书(pdf电子版类型的最终状态)
- 4---派送中
- 5---正在生成pdf
- 6--生成pdf错误

```json
- status: 订单状态
- sign
- timestamp
```

#### 6.2.2 快递信息

```
- ship_company: 快递公司
- ship_no: 快递单号
```

### 6.3 response

```json
{
    "request": "success"
}
```

### 6.4 签名算法

#### 6.4.1 算法

***拼接规则见1.3.1***

#### 6.4.2 例子

##### 6.4.2.1 签名

```python
# 订单状态签名
from apps.book.services import *
d = {
  "status": "2",
  "order_id": "0829797",
  "timestamp": 123456,
}
sign = sign_service.sign(d)
# e20d45c3930afec7f771ce3ef28aca50
print sign

# 快递信息签名
from apps.book.services import *
d = {
  "ship_company": "shunfeng",
  "ship_no": "123456",
  "order_id": "0829797",
  'sign': '952c36850cce4b76eb46e6b2e2232bf7',
  "timestamp": '123456',
  'status': '4'
}
sign = sign_service.sign(d)
# e20d45c3930afec7f771ce3ef28aca50
print sign
```

## 7 获取原始书籍信息

### 7.1 URL

```css
https://story.api.xinshu.me/sign/sync/?bid=aa84f9bd9f82&action=bookinfo&timestamp=&sign=
```

### 7.2 query

```css
bid : 原始书籍 ID
action: "bookinfo", 固定值
timestamp: 时间戳
sign: 签名
```

### 7.3 response

```json
{
    "request": "success",
    "data": {
        "bid": "aa84f9bd9f82",
        "source_site": "story",
        "page_count": 30,
        "version": 1506072314,
        "author": "先锋",
        "header_img": "",
        "typeset_type": "",
      	// 模板
        "template": "",
      	// 封面
        "cover": {
            "code_name": "cover-1",
            "image": "http://ilife.xinshu.me/upload/media/Z3UuanBnPzE1MDU5ODc1NDU4NDllZDMyYmRlYjdlZTU3Yw?imageView2/2/w/1600/interlace/0/q/100"
        },
        "openid": "oi7rhjoGUKfLtAknINW1zoy3JZtk",
        "nickname": "先锋",
        "avatar": "http://wx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTKnqWujdyfP4eOntpDSMaQJ5NsM0uAAEDN9US2DnicLWzor3DyRng9BdUic7LOjZv2JmiaI2w6XSDznA/0"
    }
}
```

### 7.4 签名算法

#### 7.4.1 算法

***拼接规则见1.3.1***