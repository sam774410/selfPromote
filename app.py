# encoding: utf-8
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

#load config info
from util.config import CHANNEL_SECRET, CHANNEL_ACCESS_TOKEN

app = Flask(__name__)

handler = WebhookHandler(CHANNEL_SECRET) 
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN) 


@app.route('/')
def index():
    return "<p>Hi I'm running</p>"

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

#handle txt msg
@handler.add(MessageEvent, message=TextMessage)  
def handle_text_message(event):                  
    msg = event.message.text 
    
    
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=msg))





# ==================================

import os
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=os.environ['PORT'])
