from flask import Flask, request
import requests
import os

app = Flask(__name__)

# ★ここに自分のMacroDroid URLを貼り付ける
MACRODROID_URL = "https://trigger.macrodroid.com/c541398f-d6e5-4532-8f13-c98c66a71c99/1"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print(f"受信データ: {data}") # ログで中身を確認できるようにします

    # Squareのテスト(order.updated)でも本番(payment.updated)でも反応するようにします
    if data and 'type' in data:
        status = data['type']
        # テスト送信または本番の決済完了ならスマホに通知
        if status == 'order.updated' or status == 'payment.updated':
            print("条件一致！スマホを動かします。")
            requests.get(MACRODROID_URL)
        else:
            print(f"ステータスが {status} なので何もしません。")

    return "OK", 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
