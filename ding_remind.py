import requests
import time
import hmac
import hashlib
import base64
import os

def get_ding_sign(timestamp, secret):
    secret_enc = secret.encode("utf-8")
    string_to_sign = f"{timestamp}\n{secret}"
    string_to_sign_enc = string_to_sign.encode("utf-8")
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = base64.b64encode(hmac_code).decode("utf-8")
    return sign

def send_dingtalk():
    webhook_base = os.getenv("DING_WEBHOOK")
    secret = os.getenv("DING_SECRET")
    if not webhook_base or not secret:
        print("缺少环境变量 DING_WEBHOOK 或 DING_SECRET")
        return

    timestamp = str(round(time.time() * 1000))
    sign = get_ding_sign(timestamp, secret)
    url = f"{webhook_base}&timestamp={timestamp}&sign={sign}"

    content = """⏰ 每日提醒
记得吃鱼油！
@13800138000
"""
    payload = {
        "msgtype": "text",
        "text": {
            "content": content
        }
    }
    resp = requests.post(url, json=payload)
    print(resp.text)

if __name__ == "__main__":
    send_dingtalk()
