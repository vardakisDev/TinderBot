from selenium import webdriver
from time import sleep



class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('http://tinder.com')


        fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/div[2]/button')
        fb_btn.click()
        
        #switch to login window
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])

        #email
        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys('stelios13vardakis@gmail.com')
        #password
        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys()
        #click login
        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]') 
        login_btn.click()





