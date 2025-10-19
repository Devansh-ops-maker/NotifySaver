from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

def open_blackboard():
    driver=webdriver.Chrome()
    driver.get(r"https://blackboard.snu.edu.in/ultra/stream")
    driver.implicitly_wait(5)
    Agree_button= driver.find_element(By.XPATH, r'//*[@id="agree_button"]')
    Agree_button.click()
    Login_button=driver.find_element(By.XPATH,r'//*[@id="login-block"]/div/button')
    Login_button.click()
    driver.implicitly_wait(5)
    Email_text_box=driver.find_element(By.XPATH,r'//*[@id="i0116"]')
    email=os.getenv("BLACKBOARD_MAIL")
    Email_text_box.send_keys(email)
    Enter=driver.find_element(By.XPATH,r'//*[@id="idSIButton9"]')
    Enter.click()
    driver.implicitly_wait(5)
    Pass_text_box=driver.find_element(By.XPATH,r'/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div/div[2]/input')
    password=os.getenv("BLACKBOARD_PASS")
    Pass_text_box.send_keys(password)
    Submit=driver.find_element(By.XPATH,r'/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[5]/div/div/div/div/input')
    Submit.click()
    element=driver.find_element(By.XPATH,r'/html/body/div/form/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[1]/input')
    element.click()
    driver.implicitly_wait(10)
    today=driver.find_element(By.XPATH,r'/html/body/div[1]/div[2]/bb-base-layout/div/main/div/div/div[3]/div[1]/div/div/div[3]/ul')
    return today.text.split('\n')
