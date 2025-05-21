# 天猫精灵 Simple Server 使用说明

一个简易天猫精灵技能服务后端，基于NodeJS，能响应天猫精灵技能的单一意图并向 HA 发送 webhook 请求，暂不支持连续对话、参数追问等复杂操作。

## 👉 使用前准备
1. 家里有天猫精灵并能正常使用。
2. HA 通过 DDNS 能在外网访问。

## 👉 天猫精灵技能平台配置(1)
前往天猫精灵技能平台 [https://iap.aligenie.com](https://iap.aligenie.com/) ，注册成为开发者，最好和天猫精灵绑定的账号一致。

![](https://gitee.com/bigxixi2022/readmes/raw/master/SimpleAligenieServer/002.jpeg)
![](https://gitee.com/bigxixi2022/readmes/raw/master/SimpleAligenieServer/003.jpeg)
![](https://gitee.com/bigxixi2022/readmes/raw/master/SimpleAligenieServer/004.jpeg)
![](https://gitee.com/bigxixi2022/readmes/raw/master/SimpleAligenieServer/005.jpeg)
![](https://gitee.com/bigxixi2022/readmes/raw/master/SimpleAligenieServer/006.jpeg)
![](https://gitee.com/bigxixi2022/readmes/raw/master/SimpleAligenieServer/007.jpeg)
![](https://gitee.com/bigxixi2022/readmes/raw/master/SimpleAligenieServer/008.jpeg)
![](https://gitee.com/bigxixi2022/readmes/raw/master/SimpleAligenieServer/009.jpeg)
![](https://gitee.com/bigxixi2022/readmes/raw/master/SimpleAligenieServer/010.jpeg)
![](https://gitee.com/bigxixi2022/readmes/raw/master/SimpleAligenieServer/011.jpeg)
![](https://gitee.com/bigxixi2022/readmes/raw/master/SimpleAligenieServer/012.jpeg)
![](https://gitee.com/bigxixi2022/readmes/raw/master/SimpleAligenieServer/013.jpeg)
![](https://gitee.com/bigxixi2022/readmes/raw/master/SimpleAligenieServer/014.jpeg)

## 👉 加载项安装与配置
#### 加载项安装
`Home Assistant` -> `设置` -> `加载项` -> `加载项商店` -> `右上角三个点` -> `仓库` -> `添加`
输入框中填入 
```
https://github.com/bigxixi/bigxixi_ha_addons  
```
或者   
```
https://gitee.com/bigxixi2022/bigxixi_ha_addons  
```
添完成后刷新 HA 页面，在加载项商店页面中找到 Simple Aligenie Skill Server ，点进去，点击`安装`，安装完成后点击`启动`。

#### 加载项配置
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

![](https://gitee.com/bigxixi2022/readmes/raw/master/SimpleAligenieServer/016.jpeg)
![](https://gitee.com/bigxixi2022/readmes/raw/master/SimpleAligenieServer/017.jpeg)
![](https://gitee.com/bigxixi2022/readmes/raw/master/SimpleAligenieServer/018.jpeg)
![](https://gitee.com/bigxixi2022/readmes/raw/master/SimpleAligenieServer/019.jpeg)
![](https://gitee.com/bigxixi2022/readmes/raw/master/SimpleAligenieServer/020.jpeg)
![](https://gitee.com/bigxixi2022/readmes/raw/master/SimpleAligenieServer/021.jpeg)
![](https://gitee.com/bigxixi2022/readmes/raw/master/SimpleAligenieServer/022.jpeg)
![](https://gitee.com/bigxixi2022/readmes/raw/master/SimpleAligenieServer/023.jpeg)

## 👉 天猫精灵技能平台配置(2)

![](https://gitee.com/bigxixi2022/readmes/raw/master/SimpleAligenieServer/025.jpeg)
![](https://gitee.com/bigxixi2022/readmes/raw/master/SimpleAligenieServer/026.jpeg)
![](https://gitee.com/bigxixi2022/readmes/raw/master/SimpleAligenieServer/027.jpeg)
![](https://gitee.com/bigxixi2022/readmes/raw/master/SimpleAligenieServer/028.jpeg)
![](https://gitee.com/bigxixi2022/readmes/raw/master/SimpleAligenieServer/029.jpeg)

## 👉 Home Assitant 配置

1. 新建自动化
`Home Assistant` -> `设置` -> `自动化与场景` -> `新建自动化 `-> `创建新的自动化`

2. **添加触发条件**  中搜索 webhook，在 **当收到某个 Webhook 有效载荷时** 下的 webhook ID 填入加载项配置中对应的 **webhook id** 。

3. 点击 webhook ID 输入框右边的 **⚙ 齿轮图标**，勾上**POST**（默认应该是勾上的），去掉**只能从本地网络访问**（默认是勾上的，需要去掉）。

4. 后续的条件和执行根据自己需求设置，建议先联动一个虚拟开关测试整个链路是否跑通，OK 了再替换成真实需要控制的设备。

![](https://gitee.com/bigxixi2022/readmes/raw/master/SimpleAligenieServer/031.jpeg)
![](https://gitee.com/bigxixi2022/readmes/raw/master/SimpleAligenieServer/032.jpeg)
![](https://gitee.com/bigxixi2022/readmes/raw/master/SimpleAligenieServer/033.jpeg)
![](https://gitee.com/bigxixi2022/readmes/raw/master/SimpleAligenieServer/034.jpeg)
![](https://gitee.com/bigxixi2022/readmes/raw/master/SimpleAligenieServer/035.jpeg)
![](https://gitee.com/bigxixi2022/readmes/raw/master/SimpleAligenieServer/036.jpeg)
![](https://gitee.com/bigxixi2022/readmes/raw/master/SimpleAligenieServer/037.jpeg)
![](https://gitee.com/bigxixi2022/readmes/raw/master/SimpleAligenieServer/038.jpeg)
![](https://gitee.com/bigxixi2022/readmes/raw/master/SimpleAligenieServer/039.jpeg)
![](https://gitee.com/bigxixi2022/readmes/raw/master/SimpleAligenieServer/040.jpeg)
![](https://gitee.com/bigxixi2022/readmes/raw/master/SimpleAligenieServer/041.jpeg)

## 👉 真机测试与使用

![](https://gitee.com/bigxixi2022/readmes/raw/master/SimpleAligenieServer/043.jpeg)
![](https://gitee.com/bigxixi2022/readmes/raw/master/SimpleAligenieServer/044.jpeg)
![](https://gitee.com/bigxixi2022/readmes/raw/master/SimpleAligenieServer/045.jpeg)
![](https://gitee.com/bigxixi2022/readmes/raw/master/SimpleAligenieServer/046.jpeg)
![](https://gitee.com/bigxixi2022/readmes/raw/master/SimpleAligenieServer/047.jpeg)
