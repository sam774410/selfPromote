# encoding: utf-8
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,VideoSendMessage,ImageSendMessage,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URIAction,
    PostbackAction, DatetimePickerAction,
    CameraAction, CameraRollAction, LocationAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent,
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
    TextComponent, SpacerComponent, IconComponent, ButtonComponent,
    SeparatorComponent, QuickReply, QuickReplyButton
)

# load config info
from util.config import CHANNEL_SECRET, CHANNEL_ACCESS_TOKEN

# Menu
from template.dashboard import Dashboard

# Intent
from dialogflow.intent import Intent

# USER_ID、NAME
USER_ID = ''
USER_NAME = ''


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

# =================================
#  Handle TEXT Message
# =================================

@handler.add(MessageEvent, message=TextMessage)  
def handle_text_message(event):                  

    if isinstance(event.source, SourceUser) or isinstance(event.source, SourceGroup) or isinstance(event.source, SourceRoom):
        profile = line_bot_api.get_profile(event.source.user_id)
        USER_ID = profile.user_id
        USER_NAME = profile.display_name

    # msg from user
    msg = event.message.text 

    # get user intent
    intent = Intent()
    response = intent.get_user_intent(msg)

    dashboard = Dashboard()

    if bool(response["isOk"]):
          
        if response['intent'] == '簡介':

            line_single_push(USER_ID, response['response'])
            line_bot_api.reply_message(event.reply_token, dashboard.intro(USER_NAME))
            
        elif response['intent'] == '技能':

            line_single_push(USER_ID, response['response'])
            line_bot_api.reply_message(event.reply_token, dashboard.skill())

        elif response['intent'] == '作品':

            line_single_push(USER_ID, response['response'])
            line_bot_api.reply_message(event.reply_token, dashboard.portfolio())

        elif response['intent'] == '證照':

            line_single_push(USER_ID, response['response'])
            line_single_push(USER_ID, '這次只找到這些~\n想要看其他的可以再請我幫忙唷~')
            line_bot_api.reply_message(event.reply_token, dashboard.certification())
        
        # help
        elif response['intent'] == 'help':

            # response from dialogflow with quick reply
            line_bot_api.reply_message(
            event.reply_token,[
                TextSendMessage(text='Hello～ '+ USER_NAME +'\n' + response['response'], quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(action=MessageAction(label='About Me', text='簡介'), image_url='https://i.imgur.com/amj6uyp.png'),
                        QuickReplyButton(action=MessageAction(label='Skill', text='你會什麼?'), image_url='https://i.imgur.com/NPsJzhp.png'),
                        QuickReplyButton(action=MessageAction(label='Portfolio', text='做過什麼project?'), image_url='https://i.imgur.com/eRcetCu.png'),
                        QuickReplyButton(action=MessageAction(label='Certification', text='有拿過什麼認證?'), image_url='https://i.imgur.com/5wWwmWb.png'),
                    ]))
                ]
            )

        else:
            line_bot_api.reply_message(event.reply_token,
                TextSendMessage(text='Hello～'+ USER_NAME +'\n可以輸入help或使用下方選單唷！'))            


    # fallback
    elif bool(response["isOk"]) == False:

        line_bot_api.reply_message(
            event.reply_token,[
                TextSendMessage(text=response['response'], quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(action=MessageAction(label='About Me', text='簡介'), image_url='https://i.imgur.com/amj6uyp.png'),
                        QuickReplyButton(action=MessageAction(label='Skill', text='你會什麼?'), image_url='https://i.imgur.com/NPsJzhp.png'),
                        QuickReplyButton(action=MessageAction(label='Portfolio', text='做過什麼project?'), image_url='https://i.imgur.com/eRcetCu.png'),
                        QuickReplyButton(action=MessageAction(label='Certification', text='有拿過什麼認證?'), image_url='https://i.imgur.com/5wWwmWb.png'),
                ]))
            ]
        )
# =================================
#  Handle Welcome event
# =================================

@handler.add(FollowEvent)
def handle_join(event):

    if isinstance(event.source, SourceUser) or isinstance(event.source, SourceGroup) or isinstance(event.source, SourceRoom):
        profile = line_bot_api.get_profile(event.source.user_id)
        USER_ID = profile.user_id
        USER_NAME = profile.display_name

        # welcome message
        dashboard = Dashboard()

        line_bot_api.reply_message(
        event.reply_token,[
            dashboard.welcome(),
            TextSendMessage(text='也可以使用下方的選單唷~\n祝您有個美好的體驗'),
            ImageSendMessage(preview_image_url='https://i.imgur.com/rqVarv1.png', original_content_url='https://i.imgur.com/rqVarv1.png')
            ]
        )


# =================================
#  Basic Function
# =================================

#push text
def line_single_push(id, txt):
    line_bot_api.push_message(id, 
        TextSendMessage(text=txt))
    
#push sticker    
def line_single_sticker(id, packed_id, sticker_id):
    line_bot_api.push_message(id, 
        StickerSendMessage(package_id=packed_id,
    sticker_id=sticker_id))

#push img    
def line_single_img(id, preview, orign):
    line_bot_api.push_message(id, 
        ImageSendMessage(
    original_content_url=orign,
    preview_image_url=preview
))



import os
if __name__ == "__main__": 
    # heroku
    app.run(host='0.0.0.0',port=os.environ['PORT'])
    # locle test
    #app.run(host='0.0.0.0',port=2000)

