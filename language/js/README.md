---
title: 各个项目的功能介绍

date: 2017-09-29 07:43:19

---


## 1 Band

### 1.1 Requirement
一个介绍一个乐队的简易网站, 主要用于发布乐队的信息. 整个网站有5个页面: Home, Photos, Live, About, Contact.

### 1.2 网站结构
- Template: template.html, 实际上仅仅是作为一个参考和依据
- Home: index.html
- Photos: photos.html
- Live: live.html
- About: about.html
- Contact: contact.html, submit.html

### 1.3 页面结构
#### 1.3.1 头部区域
- 品牌信息: LOGO等
- 导航区域: 包含一组链接, 使用nav元素来实现

#### 1.3.2 内容区域
- 使用article来包含实质性内容

### 1.3 外部文件
#### 1.3.1 Styles
- layout.css: 用于布局
- color.css: 用于上色
- typography.css: 用于版式

整体开发步骤: 布局为先-->中期上色与版式-->后期调试

#### 1.3.2 Images
存放所有静态文件, 当然也可以使用 URL 来构建.

#### 1.3.3 Scripts
- photos.js: 用于图片库
- add_load_event.js: 用于页面加载之后的 JAVASCRIPT 启动
- modernizr.js: HTML5库
