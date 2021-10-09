from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *


# ======這裡是呼叫的檔案內容=====
from message import *
from new import *
from Function import *
# ======這裡是呼叫的檔案內容=====


# ======python的函數庫==========
import tempfile
import os
import datetime
import time

from bs4 import BeautifulSoup
import requests
# ======python的函數庫==========

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi(
    'QQfRtT616WDzpgdI4nqi35t2yNOm1Wl7o38JgTkkUhX4LshwXxVCMyTE6i4rg7TuP7hV3h5R4wQmn1yvnVs+z2VGnHPqOODe4q42U5vzHFxaK9NC7kFE0sePKgaEFVHHd0T3xNEpZCab1AJ8FD0yTQdB04t89/1O/w1cDnyilFU=                          ')
# Channel Secret
handler = WebhookHandler('0f0acb797b22a4bc0cdf6f76d927dc2a')


# 監聽所有來自 /callback 的 Post Request123
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body123
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息


@ handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    if '最新合作廠商' in msg:
        message = imagemap_message()
        line_bot_api.reply_message(event.reply_token, message)
    # main 第一層
    elif '基金' == msg:
        message = mainTmpTwo(
            '選擇地區',
            '境內',
            '境內',
            '境外',
            '境外')
        line_bot_api.reply_message(event.reply_token, message)
    elif '熱門方案' == msg:
        message = function_list()
        line_bot_api.reply_message(event.reply_token, message)
    ########################################
    # 境內 基金第二層
    elif '境內' == msg:
        message = mainTmpTwo(
            '選擇類型',
            '股票型',
            '境內_股票型',
            '債券型',
            '境內_債券型')
        line_bot_api.reply_message(event.reply_token, message)
    # 境內 基金第三層
    elif '境內_股票型' == msg:
        message = mainTmpTwo(
            '選擇幣型',
            '美元',
            '境內_股票型_美元',
            '新台幣',
            '境內_股票型_新台幣')
        line_bot_api.reply_message(event.reply_token, message)
    elif '境內_債券型' == msg:
        message = mainTmpTwo(
            '選擇幣型',
            '美元',
            '境內_債券型_美元',
            '新台幣',
            '境內_債券型_新台幣')
        line_bot_api.reply_message(event.reply_token, message)
    # 境內 基金第四層
    elif '境內_股票型_新台幣' == msg:
        message = inStockFundTW()
        line_bot_api.reply_message(event.reply_token, message)
    # 境內 基金第五層
    elif '境內_股票型_新台幣_元大' == msg:
        url = 'https://fund.cnyes.com/search/?classCurrency=TWD&focusTab=1&fundGroup=G1&investmentProviderShortName=I11&onshore=1'
        msg = messageTest(url)
        message = TextSendMessage(text=msg)
        line_bot_api.reply_message(event.reply_token, message)
    elif '境內_股票型_新台幣_群益' == msg:
        url = 'https://fund.cnyes.com/search/?classCurrency=TWD&focusTab=1&fundGroup=G1&investmentProviderShortName=I65&onshore=1'
        msg = messageTest(url)
        message = TextSendMessage(text=msg)
        line_bot_api.reply_message(event.reply_token, message)
    elif '境內_股票型_新台幣_國泰' == msg:
        url = 'https://fund.cnyes.com/search/?classCurrency=TWD&focusTab=1&fundGroup=G1&investmentProviderShortName=I22&onshore=1'
        msg = messageTest(url)
        message = TextSendMessage(text=msg)
        line_bot_api.reply_message(event.reply_token, message)
    elif '境內_股票型_新台幣_復華' == msg:
        url = 'https://fund.cnyes.com/search/?classCurrency=TWD&focusTab=1&fundGroup=G1&investmentProviderShortName=I33&onshore=1'
        msg = messageTest(url)
        message = TextSendMessage(text=msg)
        line_bot_api.reply_message(event.reply_token, message)
    elif '境內_股票型_新台幣_富邦' == msg:
        url = 'https://fund.cnyes.com/search/?classCurrency=TWD&focusTab=1&fundGroup=G1&investmentProviderShortName=I31&onshore=1'
        msg = messageTest(url)
        message = TextSendMessage(text=msg)
        line_bot_api.reply_message(event.reply_token, message)
    elif '境內_股票型_新台幣_第一金' == msg:
        url = 'https://fund.cnyes.com/search/?classCurrency=TWD&focusTab=1&fundGroup=G1&investmentProviderShortName=I60&onshore=1'
        msg = messageTest(url)
        message = TextSendMessage(text=msg)
        line_bot_api.reply_message(event.reply_token, message)
#####################################
    # main 基金第二層
    elif '境外' == msg:
        message = mainTmpTwo(
            '選擇類型',
            '股票型',
            '境外_股票型',
            '債券型',
            '境外_債券型')
        line_bot_api.reply_message(event.reply_token, message)
    # main 基金第三層
    elif '境外_股票型' == msg:
        message = mainTmpTwo(
            '選擇幣型',
            '美元',
            '境外_股票型_美元',
            '新台幣',
            '境外_股票型_新台幣')
        line_bot_api.reply_message(event.reply_token, message)
    elif '境外_債券型' == msg:
        message = mainTmpTwo(
            '選擇幣型',
            '美元',
            '境外_債券型_美元',
            '新台幣',
            '境外_債券型_新台幣')
        line_bot_api.reply_message(event.reply_token, message)
    # main 基金第四層
    elif '境外_股票型_美元' == msg:
        message = mainTmpTwo(
            '選擇幣型',
            '美元',
            '境外_股票型_美元',
            '新台幣',
            '境外_股票型_新台幣')
        line_bot_api.reply_message(event.reply_token, message)
    else:
        #msg = messageTest(strUrl)
        #message = TextSendMessage(text=msg)
        message = mainTmp()
        line_bot_api.reply_message(event.reply_token, message)


# main
def mainTmp():
    message = TemplateSendMessage(
        alt_text='電腦版無法觀看',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title='基金查詢',
                    text='點選以下按鈕',
                    actions=[
                        PostbackTemplateAction(
                            label='基金',
                            data='將這個訊息偷偷回傳給機器人',
                            text='基金'
                        ),
                        MessageTemplateAction(
                            label='熱門方案',
                            data='將這個訊息偷偷回傳給機器人',
                            text='熱門方案'
                        )
                    ]
                )
            ]
        )
    )
    return message
# duplicate template
#ColumnTitle, FirLabel, FirText, SecLabel, SecText


def mainTmpTwo(ColumnTitle, FirLabel, FirText, SecLabel, SecText):
    message = TemplateSendMessage(
        alt_text='電腦版無法觀看',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title=ColumnTitle,
                    text='點選以下按鈕',
                    actions=[
                        PostbackTemplateAction(
                            label=FirLabel,
                            data='',
                            text=FirText
                        ),
                        MessageTemplateAction(
                            label=SecLabel,
                            data='',
                            text=SecText
                        )
                    ]
                )
            ]
        )
    )
    return message

# 境內_股票型_新台幣_


def inStockFundTW():
    message = TemplateSendMessage(
        alt_text='電腦版無法觀看',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title='境內股票型新台幣選擇',
                    text='點選以下按鈕',
                    actions=[
                        MessageTemplateAction(
                            label='元大',
                            data='將這個訊息偷偷回傳給機器人',
                            text='境內_股票型_新台幣_元大'
                        ),
                        MessageTemplateAction(
                            label='群益',
                            data='將這個訊息偷偷回傳給機器人',
                            text='境內_股票型_新台幣_群益'
                        ),
                        MessageTemplateAction(
                            label='國泰',
                            data='將這個訊息偷偷回傳給機器人',
                            text='境內_股票型_新台幣_國泰'
                        )
                    ]
                ),
                CarouselColumn(
                    title='境內股票型新台幣選擇',
                    text='點選以下按鈕',
                    actions=[
                        MessageTemplateAction(
                            label='復華',
                            data='將這個訊息偷偷回傳給機器人',
                            text='境內_股票型_新台幣_復華'
                        ),
                        MessageTemplateAction(
                            label='富邦',
                            data='將這個訊息偷偷回傳給機器人',
                            text='境內_股票型_新台幣_富邦'
                        ),
                        MessageTemplateAction(
                            label='第一金',
                            data='將這個訊息偷偷回傳給機器人',
                            text='境內_股票型_新台幣_第一金'
                        )
                    ]
                )
            ]
        )
    )
    return message


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
