from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from settings import Settings


def login(driver, url):
    sets = Settings()
    driver.get(url)
    try:
        acp_all_cookies = driver.find_element(By.XPATH, "/html/body/dialog/div/div/div[3]/button")
        acp_all_cookies.click()
    except Exception as e:
        print(e)
    sleep(5)
    login_via_ins = driver.find_element(By.XPATH, '//*[@id="sidebar"]/aside/div[3]/div/div[1]/div[1]/a/span')
    login_via_ins.click()
    school_input = driver.find_element(By.XPATH, '//*[@id="searchFormTextInput"]')
    school_input.send_keys('Southeast')
    sleep(5)
    school = driver.find_element(By.XPATH, '//*[@id="autocomplete-results"]/a')
    school.click()
    sleep(10)
    username_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/span[1]/input')
    password_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/span[2]/input')
    username_input.send_keys(sets.username)
    password_input.send_keys(sets.password)
    login_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/button')
    login_button.click()


