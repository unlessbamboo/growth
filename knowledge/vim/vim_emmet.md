---
title: Emmet-vim使用

date: 2017-12-12 06:46:04

---


## 1 Install
参考[Emmet-vim](https://github.com/mattn/emmet-vim)


## 2 Rule
### 2.1 Format
E#id>N*3
### 2.2 Introduction
E: 代表 HTML 标签
E#id: 代表ID 属性为id的 HTML 标签
E.className: 代表 Class 为 className的 HTML 标签
E[attr=foo]: 代表某一个属性值的 HTML 标签
E{info}: 代表包含内容info的 HTML 标签
E>N: 代表N 是 E 的子元素
E+N: 代表 N 是 E 的同级元素
E^N: 代表 N 是 E 的上级元素
E*3: 代表3个连续的 HTML 标签
E#id$: 代表一个自动增加id值的 HTML 标签, 从1开始


## 3 Example
### 3.1 基本框架
插入模式下: html:5 + <C-y> + ,


