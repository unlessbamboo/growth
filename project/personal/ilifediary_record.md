

## 1 facebook

### 1.1 feed

#### 1.1.1 all

```js
https://graph.facebook.com/v2.10/10154976616113441/feed?fields=from,type,created_time,message,status_type,permalink_url,attachments{title,target,type,url,description,subattachments.limit(100),media}&debug=all&access_token=EAAV2J7HZA9RwBAFK9bWEYlwr1ZCU3q3LtMXJMFdZBUdUAkCDWQhdigjfJYWx8V1JCJtQfYCua6QBOaewNIKHSse3V4REQWPgsfFvDd9dM8N7nfC5X54n7ISqDPaWrLrv2rdyxifOSzwcDkUI0tlwZCkVKaYR047B3EZAQAPuUgAZDZD
```

#### 1.1.2 time range

##### 1.1.2.1 since and until

其中since表示最老的时间点，until表示最新的时间点

```js
https://graph.facebook.com/v2.10/10156545949721509/feed?fields=from,type,created_time,message,status_type,permalink_url,attachments{title,target,type,url,description,subattachments.limit(100),media}&debug=all&access_token=&since=1367337600&until=1369929600
```

##### 1.1.2.2 until

例如获取20171012之前的所有数据

```js
https://graph.facebook.com/v2.10/10208283791245277/feed?fields=from,type,created_time,message,status_type,permalink_url,attachments{title,target,type,url,description,subattachments.limit(100),media}&debug=all&access_token=EAAV2J7HZA9RwBAJOcewWtUkMwaNIjhh2jfuoNQV5tGiT2f6INgMfjvR7BSwWoZCFcuywWrO4mu9Q0uF6aZB4I97NI6L5xl0ymDBWZCTSoZBT9IR2J8wsgLEkUTPusoGz9PjjbTrc12y9wTvVutsgsc6sKZCUeF3EAH8ulZAQuxwZBwZDZD&until=1483027200
```

### 1.2 get timestamp

```python
from customs.base import TimeService
TimeService.date_get_timestamp('20091201')
TimeService.date_get_timestamp('20091231')
```

### 1.3 post

#### 1.3.1 all

```js
https://graph.facebook.com/v2.9/11111/posts?fields=from,type,created_time,message,status_type,permalink_url,attachments{title,target,type,url,description,subattachments.limit(12),media}&debug=all&access_token=
```

#### 1.3.2 time range

##### 1.3.2.1 since and until

```js
https://graph.facebook.com/v2.9/111/posts?fields=from,type,created_time,message,status_type,permalink_url,attachments{title,target,type,url,description,subattachments.limit(12),media}&access_token=&since=&until=1377964800
```

##### 1.3.2.1 until

```js
https://graph.facebook.com/v2.9/111/posts?fields=from,type,created_time,message,status_type,permalink_url,attachments{title,target,type,url,description,subattachments.limit(12),media}&access_token=&until=1377964800
```



### 1.4 albums

#### 1.4.1 获取所有相册

```js
https://graph.facebook.com/v2.10/110282206173035/albums?fields=type,name,id,created_time,description,from,count,updated_time&limit=100&access_token=EAAaDlo1ciSgBAFz3Q9EXsscVRQLI9MZCp88VQmZBZAuUuYAc9yFBgVPAdaG9uewQZBloBEEaBQpMSKoBZC5S0z3T3YppgSQO221vZCHLm4cbdXaEw1nmCNzasy72Id1gDo4tQAVu3ijNx7KwMnoYqklvt22Tuuyd3O9r1LjjVSIQZDZD
```

#### 1.4.2 获取某一个相册

```js
https://graph.facebook.com/v2.10/10204949261279533/photos?fields=width,height,created_time,source,message&limit=100&access_token=EAAV2J7HZA9RwBAKFZAFHg55qstRJU59O6XCUbsbGC3gZB6oVu7mf7Mhcp7PcpWpmqZATGp9T7rVcQQw0GoRcndZAKfGzQONGydCEZCYVTAbcXXq2Y9Y04bQh1Sr2R8QgKbZCQxCB6zfGY3yjqfBJlVU5yDYTek4Yig1jWDvLJg059eVHXkZCyzCZB
```

### 1.5 获取用户信息

#### 1.5.1 user info

```json
https://graph.facebook.com/v2.10/me/?fields=name,first_name,last_name,gender,id,location{location{{country, country_code}},email,timezone,locale
```

### 1.6 本地登录

#### 1.6.1 步骤

* 更改setting以及队列
* 配置facebook的app中的login白名单URL
* 访问：http://127.0.0.1:8080/social/facebook_login，开启

#### 1.6.2 说明

确保数据库以及相应的URL是一致的。

### 1.7 User Pages

#### 1.7.1 获取用户的所有粉丝页

```js
https://graph.facebook.com/v2.10/112272155946887/accounts?fields=picture,cover,name&access_token=EAAV2J7HZA9RwBAL1ItkZAlWVASkEVqScD3lTTBcm6EEOkfKC6GhM2tXJZC69VnwwApjBeG9qBAmGsZBzP8vm0qDRGbP5ZBXTnt8N1rx7biilNAyZC5BkKr2aPQOx1Fh3d0Kt3ZBZBAgN1vQ81mWhZCR6UQJIyJGjUtCUYJJruU3TWrwZDZD
```

#### 1.7.2 获取粉丝页内容

```js
https://graph.facebook.com/v2.10/499176050152957/feed/?fields=from,type,created_time,message,status_type,permalink_url,attachments{title,target,type,url,description,subattachments.limit(12),media}&access_token=EAAV2J7HZA9RwBAIYD2f98ZAoWreVF0FEoT70oMZAzwMhrJhAaGnOcPAFbV6iUKUG7tqh01wgp0oEpCnOlMx91m4SMLV7BNKBGzjaZCCXc4qvq5HOY9isaigODzWcJZBYwx4aU6EQNVu2qXZAK4criYRlDI8DbV5TpLrZAbZA5gUYJQZDZD
```



## 2 Facebook App Token

### 2.1 Get App Token

```python
import requests

# 线上
import requests
url = "https://graph.facebook.com/v2.10/oauth/access_token?client_id={}&client_secret={}&grant_type=client_credentials"
client_id = '1537287743206684'
client_secret = ''
rsp = requests.get(url.format(client_id, client_secret))
rsp.json()

# beta
rsp = requests.get("https://graph.facebook.com/v2.8/oauth/access_token?client_id=1833532500248872&client_secret=&grant_type=client_credentials")
rsp.json()
```

### 2.2 Debug User Access Token
```python
import requests

params = {
    "input_token": "user token",
    "access_token": "app token"
}
rsp = requests.get("https://graph.facebook.com/v2.9/debug_token", params=params)
rsp.json()
```

### 2.3 调用api获取token

```python
from apps.manager.services.social_manager_service import get_facebook_authority
rsp = get_facebook_authority('')
```

## 3 数据不全

> 指定队列：python manage.py rqworker book typeset autoprint migrate data
>
> 三种原因导致数据不全：Facebook API版本、用户时间线上很多好友帖子、用户删除了Facebook数据

### 3.1 book

```python
from apps.book.services import *
from apps.book.dbmigrate import *

book = BookService.get(bid='80c41b38c938')
migrate_book(book, force=True)
```

### 3.2 item

#### 3.2.1 补全item不更新图片

```python
from apps.book.tasks.book_task import refresh_all_fb_posts
suid = 'dbe99e2fcdc110'
refresh_all_fb_posts(suid, force_typeset=True)
```

#### 3.2.2 补全item并更新图片

```python
from apps.book.tasks.book_task import refresh_all_fb_posts
# 同时会补全和更新相册图片
suid = '129b686388ca0d'
refresh_all_fb_posts(suid, update_exist_images=True, force_typeset=True)
```

#### 3.2.3 补全用户post数据

```python
from apps.item.services import *
access_token = ''
suid='bced5a39c33eb3'
# 补全
ImportService.import_user_fb_posts(suid=suid, access_token=access_token, force_typeset=True)

# 补全+更新
ImportService.import_user_fb_posts(suid=suid, access_token=access_token, force_typeset=True, update_exist_images=True)

# 更新文字内容，重置所有文字状态，谨慎使用
ImportService.import_user_fb_posts(suid=suid, access_token=access_token, force_typeset=True, update_exist_images=True, update_exist_content=True)
```

#### 3.2.4 抓取他人post数据

```python
from apps.book.tasks.book_task import refresh_all_fb_posts
suid = '720c8c533780f3'
refresh_all_fb_posts(suid, update_exist_images=True, force_typeset=True, update_other_post=True)
```

### 3.3 chapter

#### 3.3.1 排版某一个月份

```python
from apps.book.tasks.book_task import typeset_month
kwargs = {
    'new_item_ids': [u'937562bfeab359', u'bde0207eac1e01', u'c3b45e44c7614d', u'178359e6057138'], 
    'source': 'facebook', 'month': u'201410', 'suid': 'd3e53768f4611e'
}
kwargs['book_source'] = kwargs.pop('source')
typeset_month(**kwargs)
```



## 4 清除用户

### 4.1 ilifediary

```python
# uid
from apps.dangerous_utils import vanish_users
uid='00398890ab'
vanish_users(uid)
```

### 4.2 app

```python
from apps.dangerous_utils import *
uid='41a1499d4ec565'
vanish_social_user(uid)
```

### 4.3 story

```python
from apps.dangerous_utils import *
uids=['b577c28ec474b8', 'f295cc7bbca136', '556c06554bb788']
for uid in uids:
    vanish_social_user(uid)
```

### 4.4 IPastbook

```python
from apps.dangerous_utils import *
uid='ca71f849f4'
vanish_users(uid)
```



## 5 重启服务

### 5.1 ilifediary_beta

```shell
# 主服务
pm2 start gunicorn_start_service.sh --name 'beta' -x -- -p 8088 -v xinshu-service -c 1 -u ubuntu -g ubuntu

pm2 start gunicorn_start_service.sh --name 'test' -x -- -p 8088 -v pastbook-python2 -c 1 -u ubuntu -g ubuntu

# 更改配置信息，并启动队列
pm2 start manage.py  --name 'test-rq' --interpreter /home/ubuntu/.virtualenvs/pastbook-python2/bin/python -i 1 -x -- rqworker book-beta typeset-beta autoprint-beta migrate-beta data-beta

pm2 start manage.py  --name 'beta-rq' --interpreter /home/ubuntu/.virtualenvs/pastbook-python2/bin/python -i 1 -x -- rqworker book-beta typeset-beta autoprint-beta migrate-beta data-beta
```

### 5.2 ilifediary_production

```shell
# 初始阶段
pm2 start gunicorn_start_service.sh --name 'ilife' -x -- -p 8089 -v xinshu-service -c 4

pm2 start manage.py  --name 'ilife-rq' --interpreter /home/xinshu/.virtualenvs/xinshu-service/bin/python -i 16 -x -- rqworker book typeset autoprint migrate data


pm2 start gunicorn_start_service.sh --name 'pastbook' -x -- -p 8089 -v pastbook-python2 -c 4 -u ubuntu -g ubuntu

pm2 start manage.py  --name 'pastbook-rq' --interpreter /home/ubuntu/.virtualenvs/pastbook-python2/bin/python -i 16 -x -- rqworker book typeset autoprint migrate data
```

### 5.3 origin_app

```shell
# 启动app服务
pm2 start start_gunicorn_service.sh --name 'app' -x -- -p 9088 -v ilifediary-app -c 2
```

### 5.4 origin_app_test

```shell
# 启动app服务
pm2 start start_gunicorn_service.sh --name 'test' -x -- -p 9098 -v ilifediary-app -c 1
```

### 5.6 重启

```python
# Step 1 -- 查看当前队列中正在执行排版的信息
tail -f logs/book.log

# Step 2 -- 在用户量很少的情况重启Pm2服务
pm2 restart ilife ilife-rq

# Step 3 -- 清除队列DB中的错误队列
from redis import Redis
from redis import StrictRedis
for db in [1, 9]:
    r = Redis(db=db)
    r.flushdb()
    

```

### 5.7 story

```python
pm2 start start_gunicorn_service.sh --name 'story' -x -- -p 9088 -v story -c 2

pm2 start start_gunicorn_service.sh --name 'test' -x -- -p 9089 -v story -c 2 -u bifeng -n test-story
```

### 5.8 ding

```python
pm2 start gunicorn_start_service.sh --name 'ding' -x -- -p 7088 -v dingding -c 2 -u bifeng -g bifeng
```



## 6 订单

### 6.1 检查订单价格

```python
from apps.order.services import *
from apps.book.services import *
orders = OrderService.filter(paid=True, status__in=['1', '2'], deleted=False).order_by('created_at')
delivery_info = {'pdf': '0-day-delivery', 'hardback':'3-day-delivery', 'paperback': '3-day-delivery'}
for order in orders:
    book = BookService.get(bid=order.bid)
    address = AddressService.get(address_id=order.address_id)
    coupon = None
    if order.coupon_no:
        coupon = CouponService.get_or_none(coupon_no=order.coupon_no)
        params = {'country_code': address.country_code, 'currency': order.currency.lower(), 'price_type': 'book'}
        unit_price = PriceService.get(**params).value['a5'][order.binding.lower()]['inner']['200']
        params1 = {'country_code': address.country_code, 'currency': order.currency.lower(), 'price_type': 'delivery'}
        delivery_price = PriceService.get(**params1).value[delivery_info[order.binding]]
        total_page = 50 if book.total_page <= 50 else book.total_page
        origin_price = total_page * unit_price
        coupon_price = origin_price * coupon.price if coupon else order.coupon_price
        if round(origin_price, 2) != round(order.price, 2):
            print ('订单:{} bid:{} 总页数:{} 本数:{} 书页单价:{}, 实际书页价格:{:<13f} 付款书页价格:{:<13f} '
                   '实际优惠价格:{:<13f} 最后优惠价格:{:<13f} 实际应付:{:<13f} 最后实付:{:<10f}').format(
                order.order_id, book.bid, book.total_page, order.quantity, unit_price,
                origin_price, order.price, coupon_price, order.coupon_price,
                origin_price * order.quantity + float(delivery_price) - order.coupon_price, 
                order.paid_money)
```

### 6.2 验证订单的页数

```python
from apps.order.services import *
from apps.autoprint.services.decode_page import checkout_pages
orders = OrderService.filter(status='2', deleted=False, paid=1).exclude(binding='pdf').order_by('created_at')

for order in orders:
    checkout_pages(order)
```

### 6.3 删除订单图片

#### 6.3.1 根据日志删除

不推荐

```python
from apps.autoprint.services.decode_page import delete_and_retypeset

items = [(u'7d3c2106f14b48', u'https://fb-s-b-a.akamaihd.net/h-ak-fbx/v/t15.0-10/15390235_1132827096786353_996340938458529792_n.jpg?oh=49bd92893ea3127c14d94c8765957dca&oe=598FA6B1&__gda__=1502652783_abfaff1edf5b27d9750b205cfe1e570d#720x404#720x404')]
book_id = 'e6599c651f1a'
order_id = '08253372'
delete_and_retypeset(order_id, book_id, items)
```

#### 6.3.2 根据order删除

```python
# 改名了执行完后会自动重新开始排版并更改订单状态
from apps.autoprint.services.decode_page import fix_order_printbooks
fix_order_printbooks('c4053fd3b10096')
```

#### 6.3.3 获取Order错误信息

```python
from apps.autoprint.models import PrintError
from apps.autoprint.services.decode_page import delete_and_retypeset

order_id='06252447'
print_errors = PrintError.objects.filter(order_id=order_id)
for print_error in print_errors:
    if print_error.error == 'ERROR_IMAGES' and len(print_error.damaged_images) > 0:
        delete_and_retypeset(order_id, print_error.pbid, print_error.damaged_images)
```



### 6.4 下载图片

测试某一张图片在代码中的下载过程

#### 6.4.1 下载图片

```python
# 仅仅下载图片
from apps.autoprint.services.image import DownloadImage
from apps.autoprint.services.parse_html import HtmlParser
url = 'https://weixinshu.com/static/wxbook/images/wx_emoji/1f981-fe0f.png'
path = HtmlParser.get_image_path(url)
rsp = DownloadImage.download(url, path)
print rsp
print path
```

#### 6.4.2 刷新图片

```python
# 更新图片URL，重新拉取
https://graph.facebook.com/2.10/128223514378904?fields=picture,images&type=normal&access_token=EAAaDlo1ciSgBAFz3Q9EXsscVRQLI9MZCp88VQmZBZAuUuYAc9yFBgVPAdaG9uewQZBloBEEaBQpMSKoBZC5S0z3T3YppgSQO221vZCHLm4cbdXaEw1nmCNzasy72Id1gDo4tQAVu3ijNx7KwMnoYqklvt22Tuuyd3O9r1LjjVSIQZDZD
```

### 6.5 paypal

#### 6.5.1 oAuth

```shell
# 请求
curl -v https://api.paypal.com/v1/oauth2/token \
  -H "Accept: application/json" \
  -H "Accept-Language: en_US" \
  -u "client_id信息:secret秘钥" \
  -d "grant_type=client_credentials"
  
# 返回值
{
  "scope":"https://api.paypal.com/v1/payments/.* https://api.paypal.com/v1/vault/credit-card https://api.paypal.com/v1/vault/credit-card/.*",
  "access_token":"Access-Token",
  "token_type":"Bearer",
  "app_id":"APP-6XR95014SS315863X",
  "expires_in":28800
}
```

#### 6.5.2 payment

```shell
# 根据oAuth获取的token来进行payment创建流程，返回一个redirect_urls
curl -v https://api.paypal.com/v1/payments/payment \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer A21AAFrmnp9gIOkmtzZVR6AdHk6h_wMZHlSXOfWdk3rx_g8mDf2avANpVQft7axvfVBQUUVD2kUjLq-3UV3DDg" \
  -d '{
  "intent":"sale",
  "redirect_urls":{
    "return_url":"http://127.0.0.1:3000/orders/paypal/",
    "cancel_url":"http://127.0.0.1:3000/"
  },
  "payer":{
    "payment_method":"paypal"
  },
  "transactions":[
    {
      "amount":{
        "total":"7.47",
        "currency":"USD"
      }
    }
  ]
}'


# 返回信息
{
  "id": "PAY-3V942641DD692394XLEYNEHY",
  "intent": "sale",
  "state": "created",
  "payer": {
    "payment_method": "paypal"
  },
  "transactions": [
    {
      "amount": {
        "total": "0.01",
        "currency": "USD"
      },
      "related_resources": []
    }
  ],
  "create_time": "2017-06-02T02:49:02Z",
  "links": [
    {
      "href": "https://api.paypal.com/v1/payments/payment/PAY-3V942641DD692394XLEYNEHY",
      "rel": "self",
      "method": "GET"
    },
    {
      "href": "https://www.paypal.com/cgi-bin/webscr?cmd=_express-checkout&token=EC-7CX352478S089263U",
      "rel": "approval_url",
      "method": "REDIRECT"
    },
    {
      "href": "https://api.paypal.com/v1/payments/payment/PAY-3V942641DD692394XLEYNEHY/execute",
      "rel": "execute",
      "method": "POST"
    }
  ]
}
```

### 6.6 email

#### 6.6.1 自动发送订单邮件

```python
from apps.order.services import *
from apps.autoprint.management.commands.check_stash_pdf import send_pdf_order_email

order = OrderService.get(order_id='06232360')
send_pdf_order_email(order)
```

#### 6.6.2 手动发送订单邮件

```python
from apps.email.services import *
pdf_links = ['http://iprint.xinshu.me/static/print_pdf/yinjie/ilifediary/PDF/W06232360/W06232360-A5-4e0f9ab8f15cF.pdf', 'http://iprint.xinshu.me/static/print_pdf/yinjie/ilifediary/PDF/W06232360/W06232360-A5-4e0f9ab8f15cN.pdf']
parameters = {
    'username': '郑碧锋',
    'book_name': '狂想写作本',
    'order_id': '06232360',
    'tz': 8,
    'pdf_links': pdf_links,
    # 'locale': 'zh-TW',
    'locale': 'jp',
}
subject = '小组2'
email = EmailService.send_pdf_order_email(
    subject=subject,
    to='ilifediary3@163.com',
    parameters=parameters)
print email.sent
```

#### 6.6.3 手动发送新人邮件

```python
from apps.email.services import *
parameters = {
    'username': "bifengzheng",
    'coupon_no': "123456",
    'locale': "jp"
}
email = EmailService.send_newuser_email(
    subject='IlifeDiary New User',
    to="ilifediary3@163.com",
    parameters=parameters)
print email.sent
```

#### 6.6.4 自动发送新人邮件

```python
from apps.user.services import *
user = UserService.get_or_none(uid='2a0971795d')
UserService.auto_send_mail_to_newuser(user, '2E09B46E55C850', 3)
```



### 6.7 Emoji表情

#### 6.7.1 下载网址

​	一般而言，直接搜索相应的emoji图片名称就能直接通过URL下载到服务器上，如果不行，那么就需要下载图片字节码并保存为图片：

​	http://punchdrunker.github.io/iOSEmoji/table_html/ios6/

​	http://unicode.org/emoji/charts/full-emoji-list.html#1f62d

#### 6.7.2 另存为图片

```python
import base64
imgstring = "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"

imgdata = base64.b64decode(imgstring)
imgname = 'd83c.png'
with open(imgname, 'wb') as f:
    f.write(imgdata)
```



## 7 测试和配置

### 7.1 配置

通过设置默认的DJANGO_SETTINGS_MODULE, DJANGO_CONFIGURATION来控制manage.py的执行，其中

* common.py作为一个基类，仅仅涉及基础配置，不参与实际的生产环境
* 其余local.py,beta.py,test.py,production.py都是不同环境下调用的配置信息
* 中控中心在manage.py

### 7.2 自动化测试

#### 7.2.1 说明

格式如下：python manage.py test APP_MODULE_NAME --configuration=配置 --nomigrations

说明：django-test-without-migration模块，增加配置信息、添加命令参数--nomigrations/-n

#### 7.2.2 测试套件集合

```Shell
# 测试coupon用例
python manage.py test apps.order.tests.test_coupon_service --configuration=Test --nomigrations
# 测试price用例
python manage.py test apps.order.tests.test_price_service --configuration=Test --nomigrations
# 测试order用例
python manage.py test apps.order.tests.test_order_service --configuration=Test --nomigrations
# 测试address
python manage.py test apps.order.tests.test_address_service --configuration=Test --nomigrations

# ============promotion==============
# 测试promotion用例
python manage.py test apps.order.services.tests.test_normal --configuration=Test --nomigrations
# 测试promotion-coupon
python manage.py test apps.order.services.tests.test_coupon --configuration=Test --nomigrations
# 新用户
python manage.py test apps.order.services.tests.test_newuser --configuration=Test --nomigrations

# 测试套件集合目录
# 订单
python manage.py test apps.order.tests --configuration=Test --nomigrations
```

#### 7.2.3 测试套件

```python
# 测试某一个类
python manage.py test apps.order.tests.test_coupon_service.TestCouponServiceCase --configuration=Test --nomigrations
```

#### 7.2.4 测试case

```python
# 测试某个函数
python manage.py test apps.order.tests.test_coupon_service.TestCouponServiceCase.test_delete_coupon --configuration=Test --nomigrations

# 测试price中价格计算
python manage.py test apps.order.tests.test_price_service.TestPriceServiceCase.test_calculate_book_price --configuration=Test --nomigrations

# 测试order
python manage.py test apps.order.tests.test_order_service.TestOrderServiceCase.test_create_order_with_coupon --configuration=Test --nomigrations
```

### 7.3 management测试

## 8 异常处理

### 8.1 异常追踪

```python
import sys
import traceback
exc_type, exc_value, exc_tb = sys.exc_info()
traceList = traceback.extract_tb(exc_tb)
for file, lineno, function, text in traceList:
    logInfo = "错误：%s\t%s\t%s\t%s\t%s" % (
        file, lineno, function, text, err)
    print logInfo

```

## 9 SQL更新

### 9.1 更新整个表

```sql
SET SQL_SAFE_UPDATES = 0;
```





## 10 Time and Image

### 10.1 Timestamp to dt

```python
from customs.base import TimeService
TimeService.date_get_timestamp('20130830')
```

### 10.2 Timestamp to Str

```python
from customs import TimeService
TimeService.timestamp_to_strtime(1525104000)
```

### 10.3 datetime to Month

```python
from apps.item.services import *
import datetime
from django.utils import timezone
d1 = datetime.datetime(2016, 12, 31, 9, 27, 16, tzinfo=timezone.utc)
ImportService._month(d1, 8, coverse=False)
```





### 10.7 Save Image

```python
import requests
import shutil
url = 'https://scontent.xx.fbcdn.net/v/t1.0-0/p180x540/17990871_1699196130109771_2151454011134318126_n.jpg?oh=fefe898d04e1ed347e43d009abcbd798&oe=5990BA03'
rsp = requests.get(url, stream=True)
if rsp.status_code == 200:
  with open('/tmp/s1.jpg', 'wb') as f:
    rsp.raw.decode_content = True
    shutil.copyfileobj(rsp.raw, f)
```

## 11 sign

### 11.1 同步签名

```python
from apps.sign.services import *
d = {
  "order_id": "0911852",
  "status": "3",
  "timestamp": "123456",
}
d = SignService.sign(d)
print d

from apps.sign.services import *
d = {
  "bid": "7fa884127497",
  "active": False,
  "action": "status",
  "timestamp": 1505209247,
}
d = SignService.sign(d)
print(d)
```

### 11.2 token签名

```python
from customs import *
d = {
  "suid": "112272155946887",
  "source": "facebook",
  "device": "web",
  "action": "token",
}
d = SignService.sign(d)
print(d)
```

### 11.3 文章上架签名

```python
from customs import *
from apps.utils import get_redirect
d = {
  "aid": "ce7f560c339744",
  "device": "web",
  "action": "status",
  "active": "True"
}
d = SignService.sign(d)
url = "https://story.api.xinshu.me/sign/sync/?"
url = get_redirect(url, **d)
print url
```

### 11.4 获取书籍内容签名

```python
from customs import *
from __future__ import print_function
from apps.utils import get_redirect
d = {
  "bid": "d6b13e68c6cc",
  "uid": "68eff9049341f6",
  "timestamp": "1503313443",
}
d = SignService.sign(d)
url = "https://story.api.xinshu.me/book/{}/content/?".format(d['bid'])
d.pop('bid')
url = get_redirect(url, **d)
print(url)
```

### 11.5 书籍排版完成通知

```python
from customs import *
from __future__ import print_function
from apps.utils import get_redirect
d = {
  "bid": "d6b13e68c6cc",
  "timestamp": "1503313443",
  "typeset": 1,
  "version": 0,
  "page": 10,
}
d = SignService.sign(d)
url = "https://story.api.xinshu.me/book/{}/notification/?".format(d['bid'])
d.pop('bid')
url = get_redirect(url, **d)
print(url)
```

### 11.6 书籍详细信息签名

```python
from customs import *
from __future__ import print_function
from apps.utils import get_redirect
d = {
  "bid": "6beaae662343",
  "action": "bookinfo",
  "timestamp": "1503313443",
}
d = SignService.sign(d)
url = "https://story.api.xinshu.me/sign/sync/?"
url = get_redirect(url, **d)
print(url)
```



## 12 标签匹配

### 12.1 匹配多个标签

```python
from apps.utils import *
s1 = "测试50字内多标签:<b>我小粗体</b><i>我是斜体</i><u>我是下划线</u>我是其他字符串哦,你知道吗?<b>我>50</b>"
match_html_tags(s1, 50)
```

### 12.2 匹配内嵌标签

```python
from apps.utils import *
s1 = "测试50字内多标签:<b>我小粗体<u>我是内嵌下划线</u>呵呵</b><i>我是斜体</i><u>我是下划线</u>我是其他字符串哦,你知道吗?<b>我>50</b>"
match_html_tags(s1, 50)
```

### 12.3 匹配空串

```python
from apps.utils import *
s1 = ""
match_html_tags(s1, 50)
```

```python
from apps.utils import *
s1 = "我是50字内的测试:<b>测试粗体,记得50字 </b>&nbsp;测试<i>斜体注意,是斜体...</i>"
match_html_tags(s1, 50)
```

## 13 文章

### 13.1 更改文章所属用户

```python
from apps.article.dbmigrate import move_article
aid='d6b93ab2a8af0f'
to_uid='28df6521b7cc98'
move_article(aid, to_uid)
```

## 14 分册

### 14.1 获取分割页数

```python
from apps.book.services.split_book import split_chapters
chapter_list = [['a56204cec1abad', 605, 0]]
split_chapters(chapter_list, 110, 220, (110 + 220)/2)
# 返回如下值
l1 = [
  {
    'pages': 201,
    'chapters': [
      # cid, left-page, offset
      # 即0~201页
      ['a56204cec1abad', 201, 0]
    ]
  }, 
  {
    'pages': 202,
    'chapters': [
      # 200~402页
      ['a56204cec1abad', 202, 200]
    ]
  }, 
  {
    'pages': 204, 
    'chapters': [
      ['a56204cec1abad', 204, 401]
    ]
  }
]
```

```python
from apps.user.services import *
user = UserService.get(uid='6854c3d3ef')
user.set_password('test@297413')
user.save()
```



## 15 自动化打印

### 15.1 服务启动

```python
# pdf脚本
pm2 start /home/ubuntu/iLifeDiary/ilifeauto.sh --name 'ilife-pdf'

# 主服务
pm2 start /home/ubuntu/iLifeDiary/gunicorn_start_service.sh --name 'ilife-print' -x -- -p 8009 -v ilife -g ubuntu -u ubuntu -c 2

# 队列
pm2 start /home/ubuntu/iLifeDiary/iLifeDiary/manage.py  --name 'ilife-rq' --interpreter /home/ubuntu/.virtualenvs/ilife/bin/python -i 2 -x -- rqworker autoprint


# pdf脚本
pm2 start /home/ubuntu/workspace/ipastbook/ipastauto.sh --name 'ipast-pdf'

# 主服务
pm2 start /home/ubuntu/workspace/ipastbook/gunicorn_start_service.sh --name 'ipast-print' -x -- -p 8010 -v ilife -g ubuntu -u ubuntu -c 2

# 队列
pm2 start /home/ubuntu/workspace/ipastbook/iLifeDiary/manage.py  --name 'ipast-rq' --interpreter /home/ubuntu/.virtualenvs/ilife/bin/python -i 8 -x -- rqworker autoprint
```



### 15.2 手动打印一个订单

#### 15.2.1 Download image and Parse html

```python
# ipastbook
from apps.autoprint.services import print_order
print_order(order_id='07202793')

# ilifediary
from apps.autoprint.services import print_order
from apps.order.services import *
order = OrderService.get(order_id='07202793')
print_order(order)
```

#### 15.2.2 Fix

```python
from apps.autoprint.services import fix
fix(order_id='01304558')
```

### 15.3 调试

#### 15.3.1 手动下载某一张图片

```python
from apps.autoprint.services import DownloadImage
from apps.autoprint.services.parse_html import HtmlParser

url = 'https://ilife.xinshu.me/static/image/ipastbook-end-page-02.svg'
path = HtmlParser.get_image_path(url)
succ = DownloadImage.download(url, HtmlParser.get_image_path(url))
print '下载图片:', succ
```

#### 15.3.2 验证pdf是否全部生成

```python
from apps.autoprint.management.commands.check_stash_pdf import *
from apps.order.services import *
order = OrderService.get(order_id='01274555')
provider = 'yinjie'
binding = 'JZ'
succ = check_order(order, provider, binding)
print 'Check result:', succ
```

