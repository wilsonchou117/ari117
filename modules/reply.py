from linebot.models import (
    MessageEvent, TextMessage, StickerMessage, TextSendMessage, ImageSendMessage, StickerSendMessage, LocationSendMessage, TemplateSendMessage, ButtonsTemplate, PostbackAction, MessageAction, URIAction, CarouselTemplate, CarouselColumn, QuickReply, QuickReplyButton
)

# 官方文件
# https://github.com/line/line-bot-sdk-python

# 常見問答表
faq = {
    '貼圖': StickerSendMessage(
        package_id='1',
        sticker_id='1'
    ),
    '美股即時報價': TemplateSendMessage(
        alt_text='Carousel template2',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    # 匯率選單一圖片網址
                    title='美股選單一',
                    text='點選下方按鈕查詢美股即時報價',
                    actions=[
                        MessageAction(
                            label='查詢蘋果',
                            text='AAPL'
                        ),
                        MessageAction(
                            label='查詢谷歌',
                            text='GOOGL'
                        ),
                        MessageAction(
                            label='查詢微軟',
                            text='MSFT'
                        )
                    ]
                ),
                CarouselColumn(
                    # 匯率選單二圖片網址
                    title='美股選單二',
                    text='點選下方按鈕查詢美股即時報價',
                    actions=[
                        MessageAction(
                            label='查詢輝達',
                            text='NVDA'
                        ),
                        MessageAction(
                            label='查詢超微',
                            text='AMD'
                        ),
                        MessageAction(
                            label='查詢特斯拉',
                            text='TSLA'
                        )
                    ]
                ),
                CarouselColumn(
                    # 匯率選單三圖片網址
                    title='美股選單三',
                    text='點選下方按鈕查詢美股即時報價',
                    actions=[
                        MessageAction(
                            label='查詢亞馬遜',
                            text='AMZN'
                        ),
                        MessageAction(
                            label='查詢臉書',
                            text='META'
                        ),
                        MessageAction(
                            label='查詢摩根大通銀行',
                            text='JPM'
                        )
                    ]
                )
            ]
        )
    ),
    '台股即時報價': TemplateSendMessage(
        alt_text='Carousel template2',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    # 匯率選單一圖片網址
                    title='台股選單一',
                    text='點選下方按鈕查詢台股即時報價',
                    actions=[
                        MessageAction(
                            label='查詢台積電',
                            text='台積電'
                        ),
                        MessageAction(
                            label='查詢大立光',
                            text='大立光'
                        ),
                        MessageAction(
                            label='查詢聯發科',
                            text='聯發科'
                        )
                    ]
                ),
                CarouselColumn(
                    # 匯率選單二圖片網址
                    title='台股選單二',
                    text='點選下方按鈕查詢台股即時報價',
                    actions=[
                        MessageAction(
                            label='查詢和泰車',
                            text='和泰車'
                        ),
                        MessageAction(
                            label='查詢國巨',
                            text='國巨'
                        ),
                        MessageAction(
                            label='查詢聯詠',
                            text='聯詠'
                        )
                    ]
                ),
                CarouselColumn(
                    # 匯率選單三圖片網址
                    title='台股選單三',
                    text='點選下方按鈕查詢台股即時報價',
                    actions=[
                        MessageAction(
                            label='查詢群聯',
                            text='群聯'
                        ),
                        MessageAction(
                            label='查詢瑞昱',
                            text='瑞昱'
                        ),
                        MessageAction(
                            label='查詢環球晶',
                            text='環球晶'
                        )
                    ]
                )
            ]
        )
    ),
    '聯絡方式': TextSendMessage(
        text="請加入Line Id: wenjuichou"
    ),
    '門市照片': ImageSendMessage(
        original_content_url='https://picsum.photos/id/395/900/400',
        preview_image_url='https://picsum.photos/id/395/900/400'
    ),
    '美股買賣點': TextSendMessage(text='請問您想詢問哪家公司？',
                          quick_reply=QuickReply(items=[
                              QuickReplyButton(action=MessageAction(
                                  label="蘋果公司", text="蘋果")
                              ),
                              QuickReplyButton(action=MessageAction(
                                  label="谷歌", text="谷歌")
                              ),
                              QuickReplyButton(action=MessageAction(
                                  label="微軟", text="微軟")
                              ),
                              QuickReplyButton(action=MessageAction(
                                  label="臉書", text="臉書")
                              ),
                              QuickReplyButton(action=MessageAction(
                                  label="輝達", text="輝達")
                              ),
                              QuickReplyButton(action=MessageAction(
                                  label="超微", text="超微")
                              ),
                              QuickReplyButton(action=MessageAction(
                                  label="特斯拉", text="特斯拉")
                              ),
                              QuickReplyButton(action=MessageAction(
                                  label="亞馬遜", text="亞馬遜")
                              )
                             ])
                          ),
    '台股買賣點': TextSendMessage(text='請問您想詢問哪家公司？',
                          quick_reply=QuickReply(items=[
                              QuickReplyButton(action=MessageAction(
                                  label="台積電", text="TSMC")
                              ),
                              QuickReplyButton(action=MessageAction(
                                  label="鴻海", text="Foxconn")
                              ),
                              QuickReplyButton(action=MessageAction(
                                  label="聯發科", text="MediaTek")
                              )
                          ])
                          ),
    '蘋果': TextSendMessage(
        text="蘋果 2023/5/25 買點:173，賣點182"
    ),
    '谷歌': TextSendMessage(
        text="谷歌 2023/5/25 買點:99，賣點120"
    ),
    '微軟': TextSendMessage(
        text="微軟 2023/5/25 買點:290，賣點307"
    ),
    '臉書': TextSendMessage(
        text="臉書 2023/5/25 買點:130，賣點150"
    ),
    '輝達': TextSendMessage(
        text="輝達 2023/5/25 買點:277，賣點297"
    ),
    '超微': TextSendMessage(
        text="超微 2023/5/25 買點:90，賣點102"
    ),
    '特斯拉': TextSendMessage(
        text="特斯拉 2023/5/25 買點:155，賣點166"
    ),
    '亞馬遜': TextSendMessage(
        text="亞馬遜 2023/5/25 買點:97，賣點109"
    ),
    'TSMC': TextSendMessage(
        text="台積電 2023/5/25 買點:528，賣點534"
    ),
    'Foxconn': TextSendMessage(
        text="鴻海 2023/5/25 買點:98，賣點99"
    ),
    'MediaTek': TextSendMessage(
        text="聯發科 2023/5/25 買點:695，賣點703"
    ),
    '營業地址': LocationSendMessage(
        title='my location',
        address='Taiwan',
        latitude=25.03528,
        longitude=121.56473
    ),
    '查詢匯率': TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    # 匯率選單一圖片網址
                    thumbnail_image_url='https://picsum.photos/id/352/900/400',
                    title='匯率選單一',
                    text='點選下方按鈕查詢即時匯率',
                    actions=[
                        MessageAction(
                            label='查詢美金',
                            text='美金'
                        ),
                        MessageAction(
                            label='查詢港幣',
                            text='港幣'
                        ),
                        MessageAction(
                            label='查詢英鎊',
                            text='英鎊'
                        )
                    ]
                ),
                CarouselColumn(
                    # 匯率選單二圖片網址
                    thumbnail_image_url='https://picsum.photos/id/364/900/400',
                    title='匯率選單二',
                    text='點選下方按鈕查詢即時匯率',
                    actions=[
                        MessageAction(
                            label='查詢澳幣',
                            text='澳幣'
                        ),
                        MessageAction(
                            label='查詢加拿大幣',
                            text='加拿大幣'
                        ),
                        MessageAction(
                            label='查詢新加坡幣',
                            text='新加坡幣'
                        )
                    ]
                ),
                CarouselColumn(
                    # 匯率選單三圖片網址
                    thumbnail_image_url='https://picsum.photos/id/355/900/400',
                    title='匯率選單三',
                    text='點選下方按鈕查詢即時匯率',
                    actions=[
                        MessageAction(
                            label='查詢瑞士法郎',
                            text='瑞士法郎'
                        ),
                        MessageAction(
                            label='查詢日圓',
                            text='日圓'
                        ),
                        MessageAction(
                            label='查詢瑞典幣',
                            text='瑞典幣'
                        )
                    ]
                )
            ]
        )
    )
}












# 主選單
menu = TemplateSendMessage(
    alt_text='Carousel template',
    template=CarouselTemplate(
        columns=[
            CarouselColumn(
                # 卡片一圖片網址
                thumbnail_image_url='https://picsum.photos/id/296/900/400',
                title='報價查詢',
                text='點選下方按鈕開始互動',
                actions=[
                    MessageAction(
                        label='查詢匯率',
                        text='查詢匯率'
                    ),
                    MessageAction(
                        label='美股即時報價',
                        text='美股即時報價'
                    ),
                    MessageAction(
                        label='台股即時報價',
                        text='台股即時報價'
                    )
                ]
            ),
            CarouselColumn(
                # 卡片二圖片網址
                thumbnail_image_url='https://picsum.photos/id/355/900/400',
                title='明牌報價',
                text='點選下方按鈕開始互動',
                actions=[
                    MessageAction(
                        label='美股買賣點',
                        text='美股買賣點'
                    ),
                    MessageAction(
                        label='台股買賣點',
                        text='台股買賣點'
                    ),
                    MessageAction(
                        label='其他公司買賣點諮詢',
                        text='聯絡方式'
                    )
                ]
            )
        ]
    )
)
