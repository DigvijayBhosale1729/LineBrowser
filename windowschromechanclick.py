from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os

#adds /Browser to Path so webdriver can be accessed
os.environ['PATH'] += 'C:\\Browser'
def windowsClick(driver, identifier):
    try:
        search=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,identifier)))
    except:
        print('Error in waiting for loading page')
        driver.quit()
    try:
        search.click()
    except:
        print('Could not find desired text')

    driver.quit()
