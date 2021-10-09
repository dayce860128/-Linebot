# 這個檔案的作用是：建立功能列表
# ===============這些是LINE提供的功能套組，先用import叫出來=============
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
# ===============LINEAPI=============================================

from bs4 import BeautifulSoup
import requests

# 根據不同的URL都能拿出爬蟲資料
# 根據不同的URL去看有幾檔基金
# 然後把每一檔的基金八種資料拿出來

# ↓　　　　　　　　此八種　　　　　　　　↓
# strArr = ["1週", "1月", "3月", "6月", "1年",
#              "3年", "5年", "今年以來"]  # format string

# 我有找出每個URL資料的規律
# 所以能用同一個CODE跑每一個URL


def messageTest(strUrl):
    fundCount = 0  # 總共有幾個基金
    strArr = ["1週", "1月", "3月", "6月", "1年",
              "3年", "5年", "今年以來"]  # format string
    # 能任意選擇url
    url = strUrl
    fundValueSource = requests.get(url).text  # 拿取所有的網頁原始碼
    fundValue = BeautifulSoup(fundValueSource)  # 把網頁原始碼排版

    id_targetBody = fundValue.findAll('tbody', attrs={"id": "target_tbody"})
    # 基金個數計算
    fundCount = len(fundValue.findAll('td', attrs={"class": "_1OU0Y _2rwNH"}))

    returnStr = ''
    numberCounter = 0
    for fundIndex in range(0,):
        returnStr = returnStr+fundValue.findAll('td', attrs={"class": "_1OU0Y _2rwNH"})[
            fundIndex].findChild().getText() + '\n'
        for numIndex in range(0, 8):
            numberCounter = numberCounter + 1
            returnStr = returnStr + \
                strArr[numIndex] + " : " + \
                id_targetBody[0].findAll('td')[numberCounter].getText() + '\n'
        numberCounter = numberCounter + 2
        returnStr = returnStr + '\n'
    return returnStr
