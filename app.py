from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('37XJ4tX6LqFeuv3/vie+AqmLX5P+p3DOYdWq1wyJ95z2ee1ft6X+S2mgbYs2iQIVmKTq5JSXD+9HGZkNXenKcKHXvaJIdYN7svSr8SRG6PqcSWnAWgqfDsMD+Z518KXdM81bImT1T3a/51vNsI8P+QdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('b936f9058fe33c3a7c5b3b60a9ff963d')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text= Reply(event.message.text))
    line_bot_api.reply_message(event.reply_token, message)
def Reply(text):
    if text == "hi":
        return "hello"
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
