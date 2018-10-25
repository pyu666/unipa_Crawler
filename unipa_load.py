# ブラウザ操作およびスクレイピング

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import re
import datetime
import sys
import time

senju_data = []
chiba_data = []
hatoyama_data = []
day = datetime.date.today()
# today = day.strftime("%m/%d")
today = "{}/{}".format(day.month, day.day)

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(
    '/usr/lib/chromium-browser/chromedriver', chrome_options=options)


def load_unipa_kyuko_data():
    global driver, senju_data, chiba_data, hatoyama_data
    user = "YOUR USER NAME"
    password = "YOUR PASSWORD"
    URL = 'https://portal.sa.dendai.ac.jp/up/faces/login/Com00505A.jsp'
    driver.get(URL)
    # ログインする
    trycount = 20
    for i in range(trycount):
        data = driver.page_source.encode('utf-8')
        soup = BeautifulSoup(data, "html.parser")
        timeout = soup.find(id="form1:logout")
        id = soup.find(id="form1:login")
        if timeout is not None:
            driver.find_element_by_id('form1:logout').click()
        elif id is not None:
            driver.find_element_by_id('form1:htmlUserId').send_keys(user)
            driver.find_element_by_id(
                'form1:htmlPassword').send_keys(password)
            driver.find_element_by_id('form1:login').click()
            break
# driver.reload()
        print("retry")
        time.sleep(5)
        if i == trycount:
            print("login error")
            raise
        print("login try: " + str(i))
    # ホームから全授業表示、そこから履修中のみにする
    # 5件以上あった場合、すべて表示させるため
    driver.find_element_by_id(
        'form1:Poa00201A:htmlParentTable:1:htmlHeaderTbl:0:allJugyo').click()
    driver.find_element_by_id(
        'form1:Poa00201A:htmlParentTable:1:htmlDisplayOfAll:0:htmlCountCol217').click()
    print('ログイン成功')
    data = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(data, "html.parser")
    # 件数を取得
    number = soup.findAll(
        'span', id="form1:Poa00201A:htmlParentTable:htmlDetailTbl2:htmlListCount")
    info_count = int(number[0].contents[0].replace('件', ""))
    # 面倒なので1ページのみ見る
    print('合計件数' + str(info_count))
    if info_count >= 25:
        info_count = 25
    # データ取得
    for number in range(info_count):
        info_text = soup.find(
            'span', id="form1:Poa00201A:htmlParentTable:0:htmlDetailTbl2:" + str(number) + ":htmlTitleCol3")
        from_jim = soup.find(
            'span', id="form1:Poa00201A:htmlParentTable:0:htmlDetailTbl2:" + str(number) + ":htmlFromCol3")
        info_text = info_text.get_text()
        format_jim = from_jim.get_text()
        format_jim = re.sub('[*]', '', format_jim)
        if info_text.find('%s（' % today) != -1:
            if str(format_jim).find("東京千住キャンパス事務部") != -1:
                print("senju")
                senju_format(info_text)
            elif str(format_jim).find("情報環境学部事務部") != -1:
                chiba_format(info_text)
                print("chiba")
            elif str(format_jim).find("理工学部事務部教務担当") != -1:
                hatoyama_format(info_text)
                print("hatoyama")
            else:
                print("other" + info_text)

    if len(senju_data) == 0:
        senju_data.append("今日の休講情報はありません")
    if len(chiba_data) == 0:
        chiba_data.append("今日の休講情報はありません")
    if len(hatoyama_data) == 0:
        hatoyama_data.append("今日の休講情報はありません")


def senju_format(text):
    # print(text)
    global senju_data
    text = re.sub('千住・|%s（.）' % today, '', text)
    text = re.sub('\u3000', ' ', text)
    senju_data.append(text)


def chiba_format(text):
    # print(text)
    global chiba_data
    text = re.sub('%s（.）' % today, '', text)
    text = re.sub('\u3000', ' ', text)
    chiba_data.append(text)


def hatoyama_format(text):
    # print(text)
    global hatoyama_data
    text = re.sub('【鳩山】|%s（.）|「|」' % today, '', text)
    text = re.sub('\u3000', ' ', text)
    hatoyama_data.append(text)


def main():
    global driver
    try:
        load_unipa_kyuko_data()
    except:
        print("URL_error")
        senju_data = "取得エラー"
        chiba_data = "取得エラー"
        hatoyama_data = "取得エラー"
    finally:
        driver.quit()


if __name__ == '__main__':
    main()
    print(senju_data)
    print(chiba_data)
    print(hatoyama_data)
