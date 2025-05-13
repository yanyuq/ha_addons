# Simple Aligenie Skill Server

一个简易天猫精灵技能服务后端，基于NodeJS，能响应天猫精灵技能的单一意图并向 HA 发送webhook请求，暂不支持连续对话、参数追问等复杂操作。

## 使用前准备
1. 家里有天猫精灵并能正常使用。
2. HA 通过 DDNS 能在外网访问。
3. 前往天猫精灵技能平台[https://iap.aligenie.com/](https://iap.aligenie.com/) ，注册成为开发者，最好和天猫精灵绑定的账号一致。
4. 开发语音技能，获取到技能认证文件（一串字母+数字.txt，内容是另一串字母+数字）。

## 安装
`Home Assistant` -> `设置` -> `加载项` -> `加载项商店` -> `右上角三个点` -> `仓库` -> `添加`
输入框中填入 
https://github.com/bigxixi/bigxixi_ha_addons/   
添完成后刷新 HA 页面，在加载项商店页面中找到 Simple Aligenie Skill Server ，点进去，点击安装。

## 加载项配置
```
certificates:
  - certificate_file_name: 认证文件名.txt
    certificate_file_content: 认证文件内容
intents:
  - intent_name: 意图标识1
    webhook_id: 该意图发送给 homeassistant 的 webhook id1
    reply: 天猫精灵回复的文案1
  - intent_name: 意图标识2
    webhook_id: 该意图发送给 homeassistant 的 webhook id2
    reply: 天猫精灵回复的文案2
    ...

ha_url_with_port: 
    http(s)://[外网可访问的 home Assitant地址]:[端口]
route: 
    天猫精灵服务器发送请求的路由
```

## Home Assitant 配置

1. 新建自动化
`Home Assistant` -> `设置` -> `自动化与场景` -> `新建自动化 `-> `创建新的自动化`

2. `添加触发条件` 中搜索 webhook，webhook ID 填入 `加载项配置` 中对应的 `webhook id`。

3. 后续的条件和执行根据自己需求设置，建议先联动一个虚拟开关测试整个链路是否跑通，OK 了再替换成真实需要控制的设备。