import os
import time
import hmac
import hashlib
import base64
import urllib.parse
import requests

webhook = os.getenv("DING_WEBHOOK")
secret = os.getenv("DING_SECRET")

if not webhook or not secret:
    print("缺少环境变量 DING_WEBHOOK 或 DING_SECRET")
else:
    timestamp = str(round(time.time() * 1000))
    secret_enc = secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    url = f"{webhook}&timestamp={timestamp}&sign={sign}"

    msg = {
        "msgtype": "text",
        "text": {
            "content": "这是定时钉钉提醒消息"
        }
    }
    resp = requests.post(url, json=msg)
    print(resp.text)
