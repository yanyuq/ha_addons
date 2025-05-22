import os
import json
from flask import Flask, request, send_from_directory, jsonify
import requests

app = Flask(__name__, static_folder='static')

# 配置文件路径
opt = '../data/options.json'

# 默认天猫精灵返回格式
res2TM = {
    "returnCode": "0",
    "returnErrorSolution": "",
    "returnMessage": "",
    "returnValue": {
        "reply": "",
        "resultType": "RESULT",
        "executeCode": "SUCCESS"
    }
}

# 读取配置
with open(opt, 'r', encoding='utf-8') as f:
    dataJSON = json.load(f)

certs = dataJSON.get('certificates', [])
port = 20255
intents = dataJSON.get('intents', [])
route = dataJSON.get('route', '')
ha_url = dataJSON.get('ha_url_with_port', '')

# 创建天猫精灵认证文件
for cert in certs:
    try:
        name = cert['certificate_file_name']
        content = cert['certificate_file_content']
        cert_path = os.path.join(app.static_folder, 'aligenie')
        os.makedirs(cert_path, exist_ok=True)
        file_path = os.path.join(cert_path, name)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print('技能认证文件路径:', file_path)
    except Exception as e:
        print('写入证书出错:', e)

# 提供静态文件访问（等价于 express.static）
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)


@app.route('/aligenie/<path:filename>')
def serve_aligenie_cert(filename):
    return send_from_directory(os.path.join(app.static_folder, 'aligenie'), filename)


# 天猫精灵 POST 请求入口
@app.route(f'/{route}', methods=['POST'])
def handle_tm_post():
    req_data = request.get_json()
    intent_name = req_data.get('intentName', '')

    for intent in intents:
        if intent.get('intent_name') == intent_name:
            webhook_id = intent.get('webhook_id')
            reply = intent.get('reply', '命令执行成功')
            ha_webhook_url = f"{ha_url}/api/webhook/{webhook_id}"
            try:
                requests.post(ha_webhook_url, timeout=5)
                res2TM["returnValue"]["reply"] = reply
                return jsonify(res2TM)
            except Exception as e:
                print('请求 Home Assistant 出错:', e)
                res2TM["returnValue"]["reply"] = '命令执行失败，home assistant响应出错。'
                return jsonify(res2TM)

    # 没有匹配到 intent
    res2TM["returnValue"]["reply"] = '未识别的指令。'
    return jsonify(res2TM)

# 默认首页
@app.route('/')
def index():
    return "Simple Aligenie Skill Server for HomeAssistant"

if __name__ == '__main__':
    print('当前端口', port)
    app.run(host='0.0.0.0', port=port)