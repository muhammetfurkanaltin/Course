from instagramUserInfo import email, password
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

class Instagram :

    def __init__(self, email, password):
        self.browser  = webdriver.Chrome()
        self.email    = email
        self.password = password 

    def signIn(self):

        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)
     
        self.browser.find_element(By.XPATH,'/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]').click()
        
        time.sleep(2)

        emailInput    = self.browser.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')
        passwordInput = self.browser.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')
        time.sleep(2)

        emailInput   .send_keys(self.email)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(10)

    def getFollowers(self):

        self.browser.get(f"https://www.instagram.com/{self.email}/")
        time.sleep(10)

        followers = self.browser.find_element(By.XPATH,'//*[@id="mount_0_0_my"]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[2]')
        followers.send_keys(Keys.ENTER)
        time.sleep(5)
        
        follower= self.browser.find_element(By.CSS_SELECTOR,"div[role=dialog] class").find_elements(By.CLASS_NAME,"x1dm5mii")

        for user in follower:
            link = user.find_element(By.CSS_SELECTOR,"a" ).get_attribute("href")
            print(link)
            
instgram = Instagram(email,password)
instgram.signIn()
instgram.getFollowers()
