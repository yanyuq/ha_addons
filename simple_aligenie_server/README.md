# Simple Aligenie Skill Server

一个简易天猫精灵技能服务后端，基于NodeJS，能响应天猫精灵技能的单一意图并向 HA 发送 webhook 请求，暂不支持连续对话、参数追问等复杂操作。


![Supports aarch64 Architecture][aarch64-shield] ![Supports amd64 Architecture][amd64-shield] ![Supports armhf Architecture][armhf-shield] ![Supports armv7 Architecture][armv7-shield] ![Supports i386 Architecture][i386-shield]

 👉 详细使用步骤看[文档](https://github.com/yanyuq/ha_addons/blob/main/simple_aligenie_server/DOCS.md) 👈  
 👇 简明使用步骤看下面 👇 

## 使用前准备
1. 家里有天猫精灵并能正常使用。
2. HA 通过 DDNS 能在外网访问。
3. 前往天猫精灵技能平台 [https://iap.aligenie.com](https://iap.aligenie.com/) ，注册成为开发者，最好和天猫精灵绑定的账号一致。
4. 开发语音技能，获取到技能认证文件（一串字母+数字.txt，内容是另一串字母+数字+符号）。


## 安装
`Home Assistant` -> `设置` -> `加载项` -> `加载项商店` -> `右上角三个点` -> `仓库` -> `添加`
输入框中填入 
```
https://github.com/yanyuq/ha_addons  
```
或者   
```
https://gitee.com/bigxixi2022/bigxixi_ha_addons  
```
添完成后刷新 HA 页面，在加载项商店页面中找到 Simple Aligenie Skill Server ，点进去，点击`安装`，安装完成后点击`启动`。

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

2. **添加触发条件**  中搜索 webhook，在 **当收到某个 Webhook 有效载荷时** 下的 webhook ID 填入加载项配置中对应的 **webhook id** 。

3. 点击 webhook ID 输入框右边的 **⚙ 齿轮图标**，勾上**POST**（默认应该是勾上的），去掉**只能从本地网络访问**（默认是勾上的，需要去掉）。

4. 后续的条件和执行根据自己需求设置，建议先联动一个虚拟开关测试整个链路是否跑通，OK 了再替换成真实需要控制的设备。

[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[armhf-shield]: https://img.shields.io/badge/armhf-yes-green.svg
[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg
[i386-shield]: https://img.shields.io/badge/i386-yes-green.svg