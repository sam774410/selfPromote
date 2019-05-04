# encoding: utf-8
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,VideoSendMessage,
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

# imgur with random certification
from util.config import IMGUR_CLIENT_ID, IMGUR_CLIENT_SECRET, IMGUR_ALBUM_ID
from imgurpython import ImgurClient
import random


class Dashboard:

    def __init__(slef):
        pass

    # side project、others and github
    def portfolio(self):
        carousel_template_message = TemplateSendMessage(
        alt_text='SAM的作品',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/Hq4faXn.png',
                    title='運動中心小幫手',
                    text='查詢各地公有運動中心即時人流資訊',
                    actions=[
                        URIAction(
                            label='前往連結',
                            uri='line://app/1570355825-5DBnZ8B4'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/n20XpSlm.jpg',
                    title='ToolMan Finder',
                    text='尋找工具人司機 - iOS APP',
                    actions=[
                        URIAction(
                            label='前往連結',
                            uri='line://app/1570355825-y1kQ4akE'
                        )       
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/yESAFjem.png',
                    title='SAM的GitHub',
                    text='其他專案',
                    actions=[
                        URIAction(
                            label='前往連結',
                            uri='line://app/1570355825-rLKWJZK6'
                        )
                    ]
                )
            ])
        )
        return carousel_template_message

    # image carousel
    def certification(self):

        # get album from imgur with 4 random certification 
        client = ImgurClient(IMGUR_CLIENT_ID, IMGUR_CLIENT_SECRET)
        images = client.get_album_images(IMGUR_ALBUM_ID)
        num = len(images)
        image_list=[]
        for i in range(0,num):
            image_list.append(i)

        # get 4 random certification
        image_list = random.sample(image_list, 4)
        print(image_list)

        image_carousel_template_message = TemplateSendMessage(
                alt_text='SAM的Certification',
                template=ImageCarouselTemplate(
                columns=[
                ImageCarouselColumn(
                    image_url=images[image_list[0]].link,
                    action=URIAction(
                        uri=images[image_list[0]].link
                    )
                ),
                ImageCarouselColumn(
                    image_url=images[image_list[1]].link,
                    action=URIAction(
                        uri=images[image_list[1]].link
                    )
                ),
                ImageCarouselColumn(
                    image_url=images[image_list[2]].link,
                    action=URIAction(
                        uri=images[image_list[2]].link
                    )
                ),
                ImageCarouselColumn(
                    image_url=images[image_list[3]].link,
                    action=URIAction(
                        uri=images[image_list[3]].link
                    )
                ),
            ])
        )
        return image_carousel_template_message

    # skill flex msg
    def skill(self):

        bubble = BubbleContainer(
            body = BoxComponent(
                layout = 'vertical',
                contents = [
                    # header
                    TextComponent(text="SAM's SKIL", weight='bold', size='sm', color='#1DB446'),
                    TextComponent(text='Programming Skill', weight='bold', size='xxl', margin='md'),
                    SeparatorComponent(margin='xxl'),

                    # Body
                    BoxComponent(
                        layout = 'vertical',
                        margin ='md',
                        spacing = 'sm',
                        contents = [
                            # Backend
                            BoxComponent(
                                layout='baseline',
                                spacing='md',
                                contents=[
                                    IconComponent(url='https://i.imgur.com/8Uxdkpn.png', size='md'),
                                    TextComponent(text='Backend', size='lg', color='#7b7b7b')
                                ]
                            ),
                            # node go
                            BoxComponent(
                                layout = 'horizontal',
                                spacing = 'md',
                                contents = [
                                    TextComponent(text='Node.js - express', size='sm', color='#111111'),
                                    TextComponent(text='Golang - gin', size='sm', color='#111111'),
                                ] 
                            ),

                            # Mobile
                            BoxComponent(
                                layout='baseline',
                                spacing='md',
                                margin='xl',
                                contents=[
                                    IconComponent(url='https://i.imgur.com/0hOfB2w.png', size='md'),
                                    TextComponent(text='Mobile', size='lg', color='#7b7b7b')
                                ]
                            ),
                            # swift
                            BoxComponent(
                                layout = 'horizontal',
                                spacing = 'md',
                                contents = [
                                    TextComponent(text='Swift', size='sm', color='#111111'),
                                ] 
                            ),

                            # Others
                            BoxComponent(
                                layout='baseline',
                                spacing='md',
                                margin='xl',
                                contents=[
                                    IconComponent(url='https://i.imgur.com/etmNxkf.png', size='md'),
                                    TextComponent(text='Others', size='lg', color='#7b7b7b')
                                ]
                            ),
                            # py c# java html/css git docker
                            BoxComponent(
                                layout = 'horizontal',
                                spacing = 'md',
                                contents = [
                                    TextComponent(text='Python', size='sm', color='#111111'),
                                    TextComponent(text='C#', size='sm', color='#111111'),
                                    TextComponent(text='Java', size='sm', color='#111111')
                                ] 
                            ),
                            BoxComponent(
                                layout = 'horizontal',
                                spacing = 'md',
                                contents = [
                                    TextComponent(text='HTML/CSS', size='sm', color='#111111'),
                                    TextComponent(text='Git', size='sm', color='#111111'),
                                    TextComponent(text='Docker', size='sm', color='#111111')
                                ] 
                            ),                                                                                      

                            # DB
                            BoxComponent(
                                layout='baseline',
                                spacing='md',
                                margin='xl',
                                contents=[
                                    IconComponent(url='https://i.imgur.com/DaVwYMh.png', size='md'),
                                    TextComponent(text='Database', size='lg', color='#7b7b7b')
                                ]
                            ),
                            # mysql ms oracle pg redis mongo
                            BoxComponent(
                                layout = 'horizontal',
                                spacing = 'md',
                                contents = [
                                    TextComponent(text='MySQL', size='sm', color='#111111'),
                                    TextComponent(text='MSSQL', size='sm', color='#111111'),
                                    TextComponent(text='Oracle', size='sm', color='#111111')
                                ] 
                            ),
                            BoxComponent(
                                layout = 'horizontal',
                                spacing = 'md',
                                contents = [
                                    TextComponent(text='PostgreSQL', size='sm', color='#111111'),
                                    TextComponent(text='Redis', size='sm', color='#111111'),
                                    TextComponent(text='Mongo', size='sm', color='#111111')
                                ] 
                            ),

                            SeparatorComponent(margin='xxl'),
                            
                            # footer
                            BoxComponent(
                                layout = 'vertical',
                                spacing = 'md',
                                contents = [
                                    SpacerComponent(size='md'),
                                    ButtonComponent(
                                        style='primary',
                                        height='sm',
                                        color='#00BE00',
                                        action=MessageAction(label="SAM's Portfolio", text='你有什麼作品?'),
                                    ),
                                    ButtonComponent(
                                        style='secondary',
                                        height='sm',                                        
                                        action=URIAction(label="SAM's GitHub", uri='line://app/1570355825-rLKWJZK6'),
                                    )                                                                     
                                ]
                            )
                        ]
                    )
                ]
            )
        )
        message = FlexSendMessage(alt_text="SAM's Skill", contents=bubble)
        return message


    # intro flex
    def intro(self, name):

        bubble = BubbleContainer(

            # body
            body=BoxComponent(
                layout='vertical',
                spacing='md',
                contents=[
                    TextComponent(text='Hello {0},\n\n'.format(name), weight='bold', size='lg'),

                    # main info
                    TextComponent(text='我是呂明聲，現在就讀中央資管所碩一，熱愛開發、嘗試新技術，喜歡透過資訊科技解決問題 !\n\n如履歷所述，我曾擔任過資源教室助教及銀行資訊部實習生，喜歡協助同學也喜歡團隊合作解決問題，相信是TechFRESH不可或缺的Hack, everything 精神 !\n\n很高興能在這相遇，期望這是我們認識的開始！\n\nRegards,\nMing-Sheng,Lyu', size='md', wrap=True, color='#272727'),

                    SeparatorComponent(margin='xl'),

                    BoxComponent(
                        layout = 'vertical',
                        contents = [
                        SpacerComponent(size='md'),
                        ButtonComponent(
                            style='primary',
                            height='sm',
                            action=MessageAction(label="SAM's Skill", text='你會什麼?'),
                            )                                                                  
                        ]
                    )
                ]
            )
        )
        message = FlexSendMessage(alt_text="SAM's Intro", contents=bubble)
        return message


    def welcome(self):

        bubble = BubbleContainer(

            # header
            header=BoxComponent(
                layout='horizontal',
                contents=[
                    TextComponent(text='哆哆歡迎您', weight='bold', size='lg', color='#00BE00')
                ]
            ),

            #hero
            hero=ImageComponent(url='https://i.imgur.com/onXQU46.png', size='full', aspect_ratio='16:9', aspect_mode='cover'),
                

            # body
            body=BoxComponent(
                layout='vertical',
                spacing='md',
                contents=[
                    
                    # main info
                    TextComponent(text='嗨，我是哆哆，感謝您加我為好友，我會回答您的問題讓您更進一步了解明聲。讓我們開始吧！\n\n您可以直接輸入:\n\n可以介紹一下嗎?\n你會什麼?\n你有什麼作品?\n有拿過什麼認證嗎?\n\n當不知道如何使用時，請輸入help\n我會出來為您引導。', size='md', wrap=True, color='#6c6c6c'),

                    SeparatorComponent(margin='xl'),

                    BoxComponent(
                        layout = 'vertical',
                        contents = [
                        SpacerComponent(size='md'),
                        ButtonComponent(
                            style='primary',
                            height='sm',
                            action=MessageAction(label="Let's Start", text='可以介紹一下嗎?'),
                            )                                                                  
                        ]
                    )
                ]
            )
        )
        message = FlexSendMessage(alt_text="Welcome", contents=bubble)
        return message
