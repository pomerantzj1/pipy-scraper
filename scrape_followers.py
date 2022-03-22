import os
import time
import selenium
import sys
from webfunctions import startup
from login import login
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager as CM
from filter import filter_names
import time

# Complete these 2 fields ==================
USERNAME = 'jtate69420'
PASSWORD = 'imissari123'
# ==========================================

TIMEOUT = 15

options = webdriver.ChromeOptions()
# options.add_argument("--headless")
options.add_argument('--no-sandbox')
options.add_argument("--log-level=3")
mobile_emulation = {
    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/90.0.1025.166 Mobile Safari/535.19"}
options.add_experimental_option("mobileEmulation", mobile_emulation)

bot = webdriver.Chrome(executable_path=CM().install(), options=options)
bot.set_window_size(600, 1000)

bot.get('https://www.instagram.com/accounts/login/')

time.sleep(2)

print("[Info] - Logging in...")

user_element = WebDriverWait(bot, TIMEOUT).until(
    EC.presence_of_element_located((
        By.XPATH, '//*[@id="loginForm"]/div[1]/div[3]/div/label/input')))

user_element.send_keys(USERNAME)

pass_element = WebDriverWait(bot, TIMEOUT).until(
    EC.presence_of_element_located((
        By.XPATH, '//*[@id="loginForm"]/div[1]/div[4]/div/label/input')))

pass_element.send_keys(PASSWORD)

login_button = WebDriverWait(bot, TIMEOUT).until(
    EC.presence_of_element_located((
        By.XPATH, '//*[@id="loginForm"]/div[1]/div[6]/button')))

time.sleep(0.4)

login_button.click()

time.sleep(5)
    
def main():
    file = open('account_list.txt')
    accounts = eval(file.readline())
    file.close()
    
    failed_accounts = []
    while accounts:
        usr = accounts.pop(0)
        file = open("C:/Users/pomer/Documents/Rush/instagram-follower-scraper/nameslists/{}.txt".format(usr), "w")
        file.write('Followers:\n\n')
        file.close()
        try:
            scrape(usr)
        except selenium.common.exceptions.TimeoutException:
            failed_accounts.append(account)
            pass
        
    file = open('queue.txt', 'w')
    for account in failed_accounts:
        file.write(str(account))
        print('{} placed back into queue.'.format(account))
    file.close()
    bot.close()

def scrape(usr):  
    
    bot.get('https://www.instagram.com/{}/'.format(usr))

    time.sleep(3.5)

    WebDriverWait(bot, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '//*[@id="react-root"]/section/main/div/ul/li[2]/a'))).click()

    time.sleep(2)

    print('Scraping {}'.format(usr))
    users = set()
    
    end = False
    counter = 0
    while not end:
    #for hund in range(round(user_input // 100)):
                
        data = []
            
        for j in range(1, 11):

            ActionChains(bot).send_keys(Keys.END).perform()

            time.sleep(2)
             
            for i in range(1, 11):
                counter += 1
                try:
                    print(bot.find_element_by_xpath("/html/body/div[1]/section/main/div/ul/div/li[{}]/div/div[1]/div[2]/div[2]".format(counter)).text)
                    name = bot.find_element_by_xpath("/html/body/div[1]/section/main/div/ul/div/li[{}]/div/div[1]/div[2]/div[2]".format(counter)).text
                        
                    print(bot.find_element_by_xpath("/html/body/div[1]/section/main/div/ul/div/li[{}]/div/div[1]/div[2]/div[1]/a/span".format(counter)).text)
                    username = bot.find_element_by_xpath("/html/body/div[1]/section/main/div/ul/div/li[{}]/div/div[1]/div[2]/div[1]/a/span".format(counter)).text
                        
                    data.append('{}: {}'.format(name, username))
                    
                # in case of emoji hoes
                except UnicodeEncodeError:
                    continue
                        
                except selenium.common.exceptions.NoSuchElementException:
                    print('Element unable to be found. Limit may have been reached.')
                    end = True
                    break
                    
            if end:
                break
                
            
        file = open("C:/Users/pomer/Documents/Rush/pipy-scraper/nameslists/{}.txt".format(usr), "a")
        for point in data:
            try:
                file.write(str(point).strip('{').strip('}') + '\n')
            except UnicodeEncodeError:
                continue
        file.close()            
                    
                    
    print('[Info] - Saving...')
    print('[DONE] - Your followers are saved in {}.txt file!'.format(usr))
        


if __name__ == '__main__':
    main()
