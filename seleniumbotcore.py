import time 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__)) + "/"
DRIVER_BIN = os.path.join(PROJECT_ROOT, "/Users/ibrahimediz/Documents/GitHub/BN_Project_1/drivers/chromedriver") # path to chromedriver


class InstaBotCore:
    def __init__(self,username,password,wait=20):
        self.username = username
        self.password = password
        self.wait = wait
        self.driver = webdriver.Chrome(executable_path=DRIVER_BIN)
        self.driver.implicitly_wait(self.wait)
        
    def login(self,username=None,password=None):
        self.driver.get("https://www.instagram.com/accounts/login/")
        usernameentry = self.driver.find_element_by_name("username")
        usernameentry.send_keys(username or self.username)
        passwordentry = self.driver.find_element_by_name("password")
        passwordentry.send_keys(password or self.password)
        passwordentry.send_keys(Keys.ENTER)
        # /html/body/div[1]/section/main/div/div/div/div/button
        alternative = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
        alternative.click()
        # /html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]
        # time.sleep(3)
        # alternative2 = self.driver.find_element_by_xpath("# /html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]")
        # alternative2.click()
    def follow(self,kullanici = None):
        self.driver.get(f"https://www.instagram.com/{kullanici or self.username}/")
        try:
            takipdugme = self.driver.find_element_by_css_selector("button._5f5mN:nth-child(1)")
            if (takipdugme.text != ""):
                takipdugme.click()
        except:
            takipdugme = self.driver.find_element_by_css_selector("button.sqdOP:nth-child(1)")
            if (takipdugme.text != ""):
                takipdugme.click()
        self.driver.get(f"https://www.instagram.com")