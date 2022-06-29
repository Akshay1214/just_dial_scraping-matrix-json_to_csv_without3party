# Importing Libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import openpyxl
from openpyxl import load_workbook
from openpyxl import Workbook

# Loading Driver
driver = webdriver.Chrome()
driver.get("https://www.justdial.com/Delhi/Ceiling-Tile-Dealers-Armstrong/nct-11271379")
time.sleep(2)

# Scrolling page down 
scroll_pause = 5
last_ht = driver.execute_script("return document.body.scrollHeight")
time.sleep(scroll_pause)
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(scroll_pause)
    new_ht = driver.execute_script("return document.body.scrollHeight")
    if new_ht == last_ht:
        break
    last_ht = new_ht

# Scraping Data
def data_scraped():  
    scraped_data = []
    res = []
    containers = driver.find_elements(By.CSS_SELECTOR, 'li.cntanr')
    address = driver.find_elements(By.XPATH, value=("//*[@class='mrehover dn']/span[2]"))
    for i in address:
        res.append(i.get_attribute("textContent"))
        
    for data in containers:
        name = data.find_element(By.CSS_SELECTOR, ('.lng_cont_name')).text
        ratings = data.find_element(By.CSS_SELECTOR, ('.green-box')).text
        image_url = data.find_element(By.XPATH, value="/html/body/div[2]/div[2]/div[2]/div[2]/div[1]/div/section/div/ul/li/section/div[1]/div/div/a[1]/img").get_attribute("src")
        image_alt_text = data.find_element(By.CLASS_NAME, ('altImgcls')).get_attribute("alt")
        hyperlink = data.find_element(By.TAG_NAME, ('a')).get_attribute("href")
        
        scraped_data.append([name, address, ratings, image_url, image_alt_text, hyperlink])
        time.sleep(2)
    driver.quit()

    scraped_output = []
    for i, j in zip(res, scraped_data):
        j[1] = i
        scraped_output.append(j)

    # Save to excel
    wb = openpyxl.Workbook()
    ws1 = wb.active
    headers = ["Name", "Address", "Ratings", "Image URL", "Image Alt Text", "Hyperlink"]
    ws1.append(headers)
    for row in scraped_data:
        ws1.append(row)
    wb.save("output_check1.xlsx")
data_scraped()