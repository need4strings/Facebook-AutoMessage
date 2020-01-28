from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os
import time
from secretStuff import password

class FaceBot:
    def __init__(self, username, password):
        # Allowing facebook notifications
        option = Options()

        option.add_argument("--disable-infobars")
        option.add_argument("start-maximized")
        option.add_argument("--disable-extensions")

        # Pass the argument 1 to allow and 2 to block
        option.add_experimental_option("prefs", { 
            "profile.default_content_setting_values.notifications": 1 
        })
        # driver: Selenium.webdriver.Chrome: The driver that is used to control Chrome
        self.username = username
        self.password = password
        self.base_url = 'https://www.facebook.com/'
        self.driver = webdriver.Chrome(options=option , executable_path='chromedriver')

        self.login()

    def login(self):
        self.driver.get('{}/login'.format(self.base_url))
        time.sleep(4)
        self.driver.find_element_by_name('email').send_keys(self.username)
        self.driver.find_element_by_name('pass').send_keys(self.password)
        time.sleep(2)
        self.driver.find_element_by_name('login').click()

        self.clickChat()

    def clickChat(self):
        time.sleep(2)
        message = 'You are the first person in my chat, congrats!'
        self.driver.find_element_by_xpath('//*[@id="navItem_217974574879787"]/a/div').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="js_1q"]/div/div/div').send_keys(message)
        self.driver.find_element_by_xpath('//*[@id="js_1q"]/div/div/div').send_keys(Keys.RETURN)

if __name__ == '__main__':
    face_bot = FaceBot('anemail@email.com', password)
    time.sleep(2)