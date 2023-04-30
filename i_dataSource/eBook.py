#把library裝一裝
import requests
import urllib.request as req
import urllib.parse
import json
import bs4
import threading as td


#輸入
input1 = input("輸入想要找的書名：")

#轉換中文字串到urlencode
safe_string = urllib.parse.quote_plus(input1)




def task1():
    url = "https://ebook.nlpi.edu.tw/search/resultdata?search_field=TI&search_input=" + safe_string
    #讀取要的資料

    with req.urlopen(url) as response:
        data = response.read().decode("utf-8")
    #解析json
    js = json.loads(data)
    #印出來書名
    global result1
    result1 = ""
    result1 += "============國立公共資訊圖書館============ \n"
    #print("============國立公共資訊圖書館============")
    for i in range(0,len(js['record'])):
        result1 += js['record'][i]["t"] + "\n"
        #print(js['record'][i]["t"])
    #result1 += "========================" + "\n"
    #print("========================")

#===============================================
def task2():
    url = "https://www.airitibooks.com/Search/Results?SearchFieldList_obj=%5B%7B%22SearchString%22%3A%22"+ safe_string +"%22%2C%22SearchType%22%3A%22%25E6%2589%2580%25E6%259C%2589%25E6%25AC%2584%25E4%25BD%258D%22%2C%22SearchFieldCondition%22%3A%22AND%22%7D%5D&OutputKeyinSearchFieldList_obj=%5B%7B%22SearchString%22%3A%22Python%22%2C%22SearchType%22%3A%22%25E6%2589%2580%25E6%259C%2589%25E6%25AC%2584%25E4%25BD%258D%22%2C%22SearchFieldCondition%22%3A%22AND%22%7D%5D&IsLibraryCollections=Y&toPage="
    #讀取要的資料
    with req.urlopen(url) as response:
        data = response.read().decode("utf-8")
    root=bs4.BeautifulSoup(data,"html.parser")
    titles=root.find_all("div",class_="bookname")
    global result2
    result2 = ""
    result2 += "============華藝電子書============ \n"
    #print("============華藝電子書============")
    for title in titles:
        result2 += str.strip(title.string) + "\n"
        #print(str.strip(title.string))
    #result2 += "========================" + "\n"
    #print("========================")

#===============================================
def task3():
    url = "https://reading.udn.com/udnLibService/searchBookData/nccu/all?kw="+safe_string+"&page=1&amount=10&opt=all&orderby=name&type=asc"
    # #讀取要的資料
    with req.urlopen(url) as response:
        data = response.read().decode("utf-8")
    #print(data)

    global result3
    result3 = ""
    #解析json
    js = json.loads(data)
    #印出來書名
    result3 += "============udn============ \n"
    #print("============udn============")
    #print(type(js['data']['booklist'][0]['bookname']))
    for i in range(0,len(js['data']['booklist'])):
        result3 += js['data']['booklist'][i]['bookname'] + "\n"
        #print(js['data']['booklist'][i]['bookname'])

t1 = td.Thread(target=task1)
t2 = td.Thread(target=task2)
t3 = td.Thread(target=task3)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print(result1)
print(result2)
print(result3)

input1 = input("結束")

#===============================================