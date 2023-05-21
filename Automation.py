from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


class Automation:

    def __init__(self):
        self.fill_again_button = None
        self.submit_button = None
        self.link_field = None
        self.rent_field = None
        self.address_field = None
        exe_path = "/Users/macintosh/Development/chromedriver"
        #replace the path above with your own driver path.
        ser = Service(executable_path=exe_path)
        self.driver = webdriver.Chrome(service=ser)
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.get("https://forms.gle/nSB14iGaou2dmBK2A")
        #creata a smiliar form like this and replace the link with your own.
        time.sleep(5)

    def fill_details(self, address, rent, link):
        self.address_field = self.driver.find_element(By.XPATH, '//input[@aria-labelledby="i1"]')
        self.address_field.send_keys(address)
        time.sleep(1)
        self.rent_field = self.driver.find_element(By.XPATH, '//input[@aria-labelledby="i5"]')
        self.rent_field.send_keys(rent)
        time.sleep(1)
        self.link_field = self.driver.find_element(By.XPATH, '//input[@aria-labelledby="i9"]')
        self.link_field.send_keys(link)
        time.sleep(1)
        self.submit_button = self.driver.find_element(By.XPATH, '//span[contains(text(),"Gönder")]')
        self.submit_button.click()
        time.sleep(2)
        self.fill_again_button = self.driver.find_element(By.XPATH, '//a[contains(text(),"Başka bir yanıt gönder")]')
        self.fill_again_button.click()
        time.sleep(5)

    def create_google_sheet(self):
        self.driver.get("https://docs.google.com/forms/d/1pS6mZAflTIt_zIZ-fcHz1HL6oIdAPD9te633N_CidRg/edit#responses")
        #replace the link above with your own google form response link. Make sure the response link is editable
        #for all those who have the link.
        time.sleep(5)
        got_it_button = self.driver.find_element(By.XPATH, '//button[@class="iph-button"]')
        got_it_button.click()
        time.sleep(2)
        menu_button = self.driver.find_element(By.XPATH, '//*[@id="ResponsesView"]/div/div[1]/div[1]/div[2]/div['
                                                         '2]/div/div/span/span/div')
        menu_button.click()
        time.sleep(2)
        create_csv = self.driver.find_element(By.XPATH, "//div[contains(text(),'Yanıtları indir (.csv)')]")
        create_csv.click()
        time.sleep(5)
