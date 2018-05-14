

## 1 facebook

### 1.1 feed

#### 1.1.1 all

```js
https://graph.facebook.com/v2.11/10158789924855187/feed?fields=from,type,created_time,message,status_type,permalink_url,attachments{title,target,type,url,description,subattachments.limit(100),media}&debug=all&access_token=
```

#### 1.1.2 time range

##### 1.1.2.1 since and until

其中since表示最老的时间点，until表示最新的时间点

```js
https://graph.facebook.com/v2.10/10158789924855187/feed?fields=from,type,created_time,message,status_type,permalink_url,attachments{title,target,type,url,description,subattachments.limit(100),media}&debug=all&access_token=&since=1503504000&until=1504281600
```

##### 1.1.2.2 until

例如获取20171012之前的所有数据

```js
https://graph.facebook.com/v2.11/10158789924855187/feed?fields=from,type,created_time,message,status_type,permalink_url,attachments{title,target,type,url,description,subattachments.limit(100),media}&debug=all&access_token=&until=1509379200
```

#### 1.1.3 Test Code

```python
from apps.item.services import ImportService, ItemService

social_id='10158789924855187'
suid = '1570be4eb2ca6c'
book_source = 'facebook'
access_token = ''
since = 1506787200
until = 1509465600
types = [u'status', u'note', 'photo']
items = ImportService.build_user_fb_posts(
  social_id, suid, book_source, access_token, since, until, types)


from apps.book.tasks.book_task import create_or_update_book
suid = '1570be4eb2ca6c'
book_source = '1c4025247a427da72da5bbb41e6083d8'
create_or_update_book(suid, book_source)
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
https://graph.facebook.com/v2.10/110282206173035/albums?fields=type,name,id,created_time,description,from,count,updated_time&limit=100&access_token=
```

#### 1.4.2 获取某一个相册

```js
https://graph.facebook.com/v2.10/8050039453/photos?fields=width,height,created_time,source,message&limit=100&access_token=
```

### 1.5 获取用户信息

#### 1.5.1 user info

```json
https://graph.facebook.com/v2.10/me/?fields=name,first_name,last_name,gender,id,location{location{{country, country_code}},email,timezone,locale
```

### 1.7 User Pages

#### 1.7.1 获取用户的所有粉丝页

```js
https://graph.facebook.com/v2.10/112272155946887/accounts?fields=picture,cover,name&access_token=
```

#### 1.7.2 获取粉丝页内容

```js
https://graph.facebook.com/v2.10/499176050152957/feed/?fields=from,type,created_time,message,status_type,permalink_url,attachments{title,target,type,url,description,subattachments.limit(12),media}&access_token=
```

```json
https://api.instagram.com/v1/users/5340179102/media/recent/?access_token=5340179102.4637258.5bdd1ecd772747f380542c0fef71e050&max_timestamp=1518280486
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

## 3 迁移脚本

### 3.1 未下单用户ilifediary老书迁移

```python
from apps.book.dbmigrate import migrate_book
# 当前用户的id信息
suid='7cfd92da41c8d6'
# ilifediary上的书籍
bid='fc12b2a6b00c'
migrate_book(suid=suid, bid=bid)
```

### 3.2 线上用户拷贝到本地

```python
from apps.user.dbmigrate.migrate_copy_user import migrate_copy_user
uid='45751fd57f'
source='facebook'
migrate_copy_user(uid, source)
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
uid='e328ae51d3'
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



## 6 SQL

### 6.1 更新整个表

```sql
SET SQL_SAFE_UPDATES = 0;
```

### 6.2 raw_sql

```python
# 查询item项
from apps.shard_utils import sharding_required, model_from_suid

suid=''
model = model_from_suid(suid=suid)
sql = 'select item_id, origin_id, suid, type from pastbook.item use index (suid) where (origin_id in %s and source=%s and suid=%s);'
params = [(u'10155330605619454_10151243055724454', u'10155330605619454_10151248513484454', u'1422026527864696_421850074549018', u'10155330605619454_10151240673214454', u'10155330605619454_10151236308434454'), 'facebook', 'c04575199deec3']
value = model.objects.raw(sql, params=params)
```



## 7 Time

```python
# timestamp to str
from customs import TimeService
timestamp = 1530374400
TimeService.timestamp_to_strtime(timestamp)

# str to timestamp
from customs import TimeService
TimeService.date_str_to_timestamp('2017-09-02 00:00:00')

# datetime to month
from apps.item.services import *
import datetime
from django.utils import timezone
d1 = datetime.datetime(2016, 12, 31, 9, 27, 16, tzinfo=timezone.utc)
ImportService._month(d1, 8, coverse=False)
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
print_order(order_id='01304558')

# ilifediary
from apps.autoprint.services import print_order
from apps.order.services import *
order = OrderService.get(order_id='07202793')
print_order(order)
```

#### 15.2.2 Fix

```python
from apps.autoprint.services import fix
fix(order_id='02264621')
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

