from flask import Flask, request
import requests

BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

app = Flask(__name__)

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": msg, "parse_mode": "HTML"}
    requests.post(url, data=data)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    signal = data.get("signal", "").upper()

    if signal == "BUY":
        msg = "🟢<b><u><i> BUY </i></u></b> 📈"
        send_telegram(msg)

    elif signal == "SELL":
        msg = "🔴<b><u><i> SELL </i></u></b> 📉"
        send_telegram(msg)

    return {"status": "ok"}

@app.route("/", methods=["GET"])
def home():
    return "Bot Running Successfully 24/7"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
