const fs = require('fs');
const path = require('path');
const express = require('express');
const axios = require('axios');
const app = express();

// 配置文件目录
const opt = '../data/options.json';
// 静态文件目录
const staticFolder = 'static';
app.use(express.static(staticFolder));

// 返回天猫精灵请求模板
const res2TM = {
  "returnCode": "0",
  "returnErrorSolution": "",
  "returnMessage": "",
  "returnValue": { 
      "reply": "",
      "resultType": "RESULT",
      "executeCode": "SUCCESS"
  }
}

// 读取配置
fs.readFile(opt, (err, data) => {
  if(!err){
    const dataJSON = JSON.parse(data);
    const certs = dataJSON.certificates;
    // console.log('certs',certs);
    const port = 20255;
    const intents = dataJSON.intents;
    const route = dataJSON.route;
    const ha_url = dataJSON.ha_url_with_port;

    // 创建天猫精灵配置文件
    for(let i=0;i<certs.length;i++){
      try{
        const name = certs[i].certificate_file_name;
        const content = certs[i].certificate_file_content;
        const cpath = path.join('./', staticFolder,'aligenie',name);
        console.log('技能认证文件路径',cpath);
        fs.writeFileSync(cpath, content);

      }catch(err){
        console.log(err);
      }
    }

    // 监听来自天猫精灵服务器的 post 请求
    app.post('/'+route,express.json(),(req,res) =>{
      // 获取意图
      const intentName = req.body.intentName;
      // 匹配意图，发送请求到HA
      intents.forEach(intent => {
        if(intent.intent_name === intentName){
          const ha_webhook_url = path.join(ha_url,'api','webhook',intent.webhook_id);
          const reply = intent.reply;
          // 向HA发送 webhook_id
          axios.post(ha_webhook_url)
              .then(ha_res => {
                  // console.log(ha_res)
                  // 向天猫精灵服务器发送回复文案
                  res2TM["returnValue"]["reply"] = reply ? reply : '命令执行成功';
                  res.send(res2TM);                  
                })
              .catch(error => {
                console.error(error);
                // 若失败，天猫精灵服务器发送失败兜底文案
                res2TM["returnValue"]["reply"] = '命令执行失败，home assistant响应出错。';
                res.send(res2TM);                
              });

        }
      });
      
    })
    // 默认页面显示文案
    app.get('/', (req, res) => {
        res.end("Simple Aligenie Skill Server for HomeAssistant");
    });

    console.log('当前端口',port);
    app.listen(port);
  }
})