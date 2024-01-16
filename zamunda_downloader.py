from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By

options = Options()
options.add_argument('--headless')

# Set the path to browser driver
PATH = r"YOUR PATH TO CHROME DRIVER"
# Set the starting page
page = 34
# Set your Zamunda username and password
password = 'YOUR PASSWORD'
username = 'YOUT USERNAME'

url = 'https://zamunda.net/catalogs/books?comb=yes&t=books&page='
driver = webdriver.Chrome()

driver.get(f'{url}{page}')

# Log In
username_find = driver.find_element(By.XPATH,
                                    '/html/body/div[4]/div/table/tbody/tr[1]/td/table/tbody/tr/td/form/table/tbody/tr[1]/td[2]/input')
username_find.send_keys(username)
password_find = driver.find_element(By.XPATH,
                                    '/html/body/div[4]/div/table/tbody/tr[1]/td/table/tbody/tr/td/form/table/tbody/tr[2]/td[2]/input')
password_find.send_keys(password)
submit_button = driver.find_element(By.XPATH,
                                    '/html/body/div[4]/div/table/tbody/tr[1]/td/table/tbody/tr/td/form/table/tbody/tr[3]/td/input')
submit_button.click()


def download_books(page):
    while page >= 0:
        for row in range(2, 12):
            try:
                link = f'/html/body/div[4]/div/table/tbody/tr[1]/td/table/tbody/tr/td/center/b/b/table[4]/tbody/tr[{row}]/td[1]/center[1]/a'
                bulgarian = f'/html/body/div[4]/div/table/tbody/tr[1]/td/table/tbody/tr/td/center/b/b/table[4]/tbody/tr[{row}]/td[1]/center[2]/img'
                html_el_link = driver.find_element(By.XPATH, link)
                html_el_bulgarian = driver.find_element(By.XPATH, bulgarian)

                html_el_link.send_keys(Keys.CONTROL + Keys.RETURN)

            except:
                print('no bulgarian')
        page -= 1
        driver.get(f'{url}{page}')


download_books(page)

driver.quit()
