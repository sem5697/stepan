import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s=Service('C:/Users/KServis/Downloads/chromedriver.exe')

driver=webdriver.Chrome(service=s)
driver.get("https://qa.neapro.site/login/")
driver.find_element(By.XPATH,"//*[@id='__layout']/div/section/div[2]/div/div/div/form/div[1]/div[1]/div/input").send_keys("ser5697@yandex.ru")
driver.find_element(By.XPATH,"//*[@id='__layout']/div/section/div[2]/div/div/div/form/div[1]/div[2]/div/input").send_keys("gbyzrepz")
driver.find_element(By.XPATH,"//*[@id='__layout']/div/section/div[2]/div/div/div/form/div[2]/button").click()
time.sleep(30)

#Откроем блок паспорт
driver.find_element(By.CSS_SELECTOR,".form:nth-child(2) .document-tile:nth-child(1)").click()

#Фамилия
driver.find_element(By.ID,"surname").clear()
driver.find_element(By.ID,"surname").send_keys("Кот")

#Имя
driver.find_element(By.ID,"name").clear()
driver.find_element(By.ID,"name").send_keys("Степан")




