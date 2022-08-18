import time
import csv
import urllib.parse
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

csv_path = "D:/myprojects/import_lutein/lutein.csv"


def get_url(query):
    #取得目標網址
    query_enc = urllib.parse.quote(query)
    url = "https://consumer.fda.gov.tw/Food/CapsuleAuditQuery.aspx?nodeID=165&cn=" + query_enc
    if url:
        return url
    else:
        return None


def get_target_list(search):
    #在所有抓取下來的資料中，取出所需要的目標資料
    target_list = []
    for i in range(len(search)):
        if search[i][0] == "中文品名":
            target_list.append(search[i][1])
        elif search[i][0] == "申請商名稱":
            target_list.append(search[i][1])
        elif search[i][0] == "申請商電話":
            target_list.append(search[i][1])
        elif search[i][0] == "產地":
            target_list.append(search[i][1])
    return target_list


def get_result(target_list):
    #將目標資料的列表處理成可以轉換成csv的格式
    result = [["中文品名", "申請商名稱", "申請商電話", "產地"]]
    for j in range(0, len(target_list), 4):
        result.append(target_list[j:j + 4])
    return result


def get_csv(result):
    #將結果存成csv檔
    with open(csv_path, "w", encoding="utf-8") as f:
        writer = csv.writer(f)
        csv_file = writer.writerows(result)
        return csv_file


def main():
    query = "葉黃素"
    try:
        #取得driver
        path = "D:/myprojects/import_lutein/geckodriver.exe"
        s = Service(path)
        driver = webdriver.Firefox(service=s)
        driver.set_page_load_timeout(60)
        driver.get(get_url(query))

        items_counts = driver.find_element(By.XPATH, "//*[@id='tabs']/div/span").text.strip()  #找出搜尋總數量
        total_pages = int(items_counts)//10 + 1
        search = []
        #點進每一個搜尋結果的網頁，抓取資料，第一頁結果抓完後按下一頁，直到沒有下一頁為止
        for page in range(total_pages):
            try:
                items = driver.find_elements(By.CSS_SELECTOR, "td.txt_L a")
                page = driver.find_element(By.CLASS_NAME, "page")
                next_page = page.find_element(By.CLASS_NAME, "page_nn")
                driver.execute_script("window.scrollTo(0, 643)")
                for item in items:
                    item.send_keys(Keys.RETURN)
                    WebDriverWait(driver, 10).until(lambda d: d.find_element(By.CLASS_NAME, "RL-th"))
                    soup = BeautifulSoup(driver.page_source, 'html5lib')
                    ul = soup.find("ul","resultList")
                    all = ul.find_all("li")
                    for i in all:
                        tmp = [s for s in i.stripped_strings]
                        search.append(tmp)
                    driver.back()
                    time.sleep(2)

                next_page.click()
                time.sleep(2)
            except:
                break
        target_list = get_target_list(search)
        result = get_result(target_list)
        csv_file = get_csv(result)

        #印出所取得的csv檔中"中文品名"的部分
        with open(csv_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                print(row["中文品名"])

    finally:
        driver.quit()

main()


