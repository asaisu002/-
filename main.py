from flask import Flask, request
import requests

app = Flask(__name__)

# ★ここに自分のMacroDroid URLを貼り付ける
MACRODROID_URL = "https://trigger.macrodroid.com/c541398f-d6e5-4532-8f13-c98c66a71c99/1"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if data and 'data' in data:
        status = data['data']['object']['payment']['status']
        if status == 'COMPLETED':
            print("決済完了！スマホを動かします。")
            requests.get(MACRODROID_URL)
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
