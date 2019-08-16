# ChrisBot
蛋蛋小分队专属订制 Telegram Bot


## 信息需求

### 购物类

- 命令： `/shop`

- 网址：
  - 北美烧钱快报 <https://www.dealmoon.cn/>
  - ...



### 社会新闻类

- 命令: `/news`
- 网址:
  - xxx



### 计算机类

- 命令: `/cs`
- 网址:
  - Hacker News <https://news.ycombinator.com/>



### 金融类

- 命令: `/fin`
- 网址:
  - xxx



### 新闻查找

- 命令: `/search` + 关键字
- 支持在 xxx 网站关键字搜索并返回第一个 (or 前三个) 新闻



### 图片搜索

- 命令: `/pic` + 关键字
- 支持在 google image 中按关键字搜索并返回第一张图片



### 图灵机器人回复

已接入 Tuling 机器人 API. 但访问次数限制极大，不是很好用



### 订阅服务

- `/subscribe`,  `/unsubscribe`
- 用户可订阅机器人的定时推送 (暂时固定推送内容，可选内容待开发)
- 使用 sqlite3 维护订阅用户的 chatID， 当用户删除对话后或者取消订阅后需要重新订阅

