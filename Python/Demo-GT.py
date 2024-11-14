from githubUserInfo import username, password
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Github:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.followers = []

    def signIn(self):
        self.browser.get("https://github.com/login")
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.ID, "login_field"))
        ).send_keys(self.username)
        self.browser.find_element(By.ID, "password").send_keys(self.password)
        self.browser.find_element(By.XPATH, '//*[@id="login"]/div[4]/form/div/input[13]').click()
        time.sleep(2)

    def loadFollowers(self):
        items = self.browser.find_elements(By.CSS_SELECTOR, ".d-table.table-fixed")
        for item in items:
            self.followers.append(item.find_element(By.CSS_SELECTOR, ".Link--secondary.pl-1").text)

    def getFollowers(self):
        self.browser.get(f"https://github.com/muhammetfurkanaltin?tab=followers")
        time.sleep(2)

        self.loadFollowers()

        while True:
            try:
                next_button = WebDriverWait(self.browser, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "BtnGroup"))
                ).find_element(By.LINK_TEXT, "Next")

                if next_button:
                    next_button.click()
                    time.sleep(2)
                    self.loadFollowers()
                else:
                    break
            except:
                break

        self.browser.close()

github = Github(username, password)
github.signIn()
github.getFollowers()
print(github.followers)
