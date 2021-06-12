import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# To Run: 
# blank = InstagramBot("<username of your account>", "<password of your account>")
# blank.login()
# blank.findPage("<username of target page>")
# blank.likeAllPicsOnPage()
# blank.commentAllPicsOnPage("<comment>")
# blank.likeAndCommentAllPicsOnPage("<comment>")

class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()

    def closeBrowser(self):
        self.driver.quit()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(1)
        driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(self.username)
        driver.find_element_by_name('password').send_keys(self.password)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(3)
        driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        time.sleep(2)

    def findPage(self, page):
        driver = self.driver
        driver.get("https://www.instagram.com/" + page + "/")

    def likeAllPicsOnPage(self):
        driver = self.driver
        picList = []
        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]

        for pic in pic_hrefs:
            if "/p/" in pic:
                picList.append(pic)

        for pic in picList:
            driver.get(pic)
            time.sleep(1)
            try: 
                driver.find_element_by_xpath('//*[name()="svg"][@aria-label="Like"][@width="24"]').click()
            except selenium.common.exceptions.NoSuchElementException:
                print("Picture already liked")
            time.sleep(1)

    def commentAllPicsOnPage(self, comment):
        driver = self.driver
        picList = []
        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]

        for pic in pic_hrefs:
            if "/p/" in pic:
                picList.append(pic)

        for pic in picList:
            driver.get(pic)
            time.sleep(2)
            driver.find_element_by_xpath("//section[@class='sH9wk  _JgwE ']").click()
            time.sleep(1)

            action = webdriver.ActionChains(driver)
            action.send_keys(comment)
            action.perform()

            time.sleep(1)
            driver.find_element_by_xpath("//button[@type='submit']").click()
            time.sleep(2)

    def likeAndCommentAllPicsOnPage(self, comment):
        driver = self.driver
        picList = []
        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]

        for pic in pic_hrefs:
            if "/p/" in pic:
                picList.append(pic)

        for pic in picList:
            driver.get(pic)
            time.sleep(1)
            try: 
                driver.find_element_by_xpath('//*[name()="svg"][@aria-label="Like"][@width="24"]').click()
            except selenium.common.exceptions.NoSuchElementException:
                print("Picture already liked")
            time.sleep(2)
            driver.find_element_by_xpath("//section[@class='sH9wk  _JgwE ']").click()
            time.sleep(1)

            action = webdriver.ActionChains(driver)
            action.send_keys(comment)
            action.perform()

            time.sleep(1)
            driver.find_element_by_xpath("//button[@type='submit']").click()
            time.sleep(2)
