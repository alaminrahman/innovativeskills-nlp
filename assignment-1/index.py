from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get('https://www.daraz.com.bd/apple/laptops/?spm=a2a0e.searchList.cate_5_2.6.7d2d3ZfA3ZfAGU')
driver.maximize_window()

# Class Work Practice
# text = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/a').text
# link = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/a').get_attribute('href')

# print(text, link)

# Home work
imgLinkList = []

for i in range(1, 10):
    num = str(i)
    imgLink = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div['+ num +']/div/div/div[1]/div/a/div/img').get_attribute('src')
    
    imgLinkList.append(imgLink)
    
print('================== Home Work =================')
print('================== Printing Img link from Daraz =================')
print(imgLinkList)
print('================== End Printing Img link from Daraz =================')

time.sleep(60)

driver.quit()