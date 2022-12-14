# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class Test554():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_554(self):
    self.driver.get("https://qa.neapro.site/login/")
    self.driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(2) input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(1) input").send_keys("ser5697@yandex.ru")
    self.driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(2) input").send_keys("gbyzrepz")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.CSS_SELECTOR, ".form:nth-child(2) .document-tile:nth-child(1)").click()
    self.driver.find_element(By.ID, "surname").click()
    self.driver.find_element(By.ID, "surname").send_keys("петров")
    self.driver.find_element(By.CSS_SELECTOR, ".blender").click()
    self.driver.find_element(By.ID, "name").click()
    self.driver.find_element(By.ID, "name").send_keys("петр")
    self.driver.find_element(By.ID, "patronymic").click()
    self.driver.find_element(By.ID, "patronymic").send_keys("петрович")
    self.driver.find_element(By.NAME, "date").click()
    self.driver.find_element(By.NAME, "date").send_keys("09.11.1970")
    self.driver.find_element(By.ID, "passportSeries").click()
    self.driver.find_element(By.ID, "passportSeries").send_keys("32-60")
    self.driver.find_element(By.ID, "passportNumber").click()
    self.driver.find_element(By.ID, "passportNumber").send_keys("4320000")
    self.driver.find_element(By.CSS_SELECTOR, "#dateOfIssue .mx-input").click()
    self.driver.find_element(By.CSS_SELECTOR, "#dateOfIssue .mx-input").send_keys("11.11.1987")
    self.driver.find_element(By.ID, "code").click()
    self.driver.find_element(By.ID, "code").send_keys("321-567")
    self.driver.find_element(By.ID, "cardId").click()
    self.driver.find_element(By.ID, "cardId").send_keys("234-765-890 53")
    self.driver.find_element(By.ID, "issued").click()
    self.driver.find_element(By.ID, "issued").send_keys("пензенским щвд")
    self.driver.find_element(By.ID, "phone").click()
    self.driver.find_element(By.ID, "phone").send_keys("(_937)234-56 72")
    self.driver.find_element(By.CSS_SELECTOR, ".outline").click()
    self.driver.find_element(By.CSS_SELECTOR, ".fill").click()

