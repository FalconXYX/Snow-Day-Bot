from selenium import webdriver
import os
import keyboard
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import getimg, ConvertToString
import matplotlib.pyplot as plt
from selenium import webdriver
import threading, time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
string = getimg.final_string()
message = ConvertToString.remove_html_tags()



dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'Chromedriver')
driver = webdriver.Chrome(executable_path = filename)
driver.get("https://www.instagram.com")
time.sleep(2)
username = driver.find_element(By.NAME, "username")
password = driver.find_element(By.NAME, "password")
loginbutton = driver.find_element(By.XPATH, " /html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button")
username.send_keys("snow_day_detector_innisdale")
password.send_keys("snowdayisss")
loginbutton.click()
time.sleep(3)
notnowb = driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div/div/div/button")
notnowb.click()
time.sleep(1)
nownotif = driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/div[3]/button[2]")
nownotif.click()
time.sleep(1)
createbutton = driver.find_element(By.XPATH, "/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[3]/div/button")
createbutton.click()
time.sleep(1)
filebutton = driver.find_element(By.XPATH, "/html/body/div[8]/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]/div/button")
filebutton.click()
time.sleep(1)
keyboard.write(string)
keyboard.press_and_release('enter')
time.sleep(1)
nextbutton = driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div/div/div[1]/div/div/div[2]/div/button")
nextbutton.click()
time.sleep(1)
nextbutton = driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div/div/div[1]/div/div/div[2]/div/button")
nextbutton.click()
time.sleep(1)
caption = driver.find_element(By.XPATH, " /html/body/div[6]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/textarea")
caption.send_keys(message)
time.sleep(5)
sharebutton = driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div/div/div[1]/div/div/div[2]/div/button")
sharebutton.click()
driver.close()  