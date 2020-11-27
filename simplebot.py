from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
# whatsapp web link
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(10)
# define group and contacts
contacts = ['Parnasianos Amadores']
message = 'isso é um bot?'
# search group
def search_contact(contact):
    search_field = driver.find_element_by_xpath('//div[contains(@class, "_1awRl copyable-text selectable-text")]')
    time.sleep(3)
    search_field.click()
    search_field.send_keys(contact)
    search_field.send_keys(Keys.ENTER)
# message function
def send_message(message):
    message_field = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    message_field.click()
    time.sleep(3)
    message_field.send_keys(message)
    message_field.send_keys(Keys.ENTER)
# using functions
for contact in contacts:
    search_contact(contact)
    send_message(message)

#"_1awRl copyable-text selectable-text"
