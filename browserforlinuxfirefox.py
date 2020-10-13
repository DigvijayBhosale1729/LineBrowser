from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import time

#Adds Browser to the PATH so that the drivers can be accessed
os.environ['PATH'] += ':/Browser'
def linuxOpenSite(website):
    #create a webdriver object
    driver= webdriver.Firefox(executable_path='./geckodriver_linux64', firefox_binary='/usr/lib/firefox/firefox')
    driver.get(website)


    driver.quit()
    return (driver)

def linuxSearchByID(website, identifier, uinput):
    driver= webdriver.Firefox(executable_path='./geckodriver_linux64', firefox_binary='/usr/lib/firefox/firefox')
    driver.get(website)
    try:
        search=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,identifier)))
    except:
        print('Error in waiting for loading page')
        driver.quit()
        return ('error')

    #search= driver.find_element_by_id(identifier)
    search.send_keys(uinput)
    search.send_keys(Keys.ENTER)


    driver.quit()
    return (driver)

def linuxSearchByName(website, identifier, uinput):
    driver= webdriver.Firefox(executable_path='./geckodriver_linux64', firefox_binary='/usr/lib/firefox/firefox')
    driver.get(website)
    try:
        search=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME,identifier)))
    except:
        print('Error in waiting for loading page')
        driver.quit()
        return ('error')

    #search= driver.find_element_by_name(identifier)
    search.send_keys(uinput)
    search.send_keys(Keys.RETURN)


    driver.quit()
    return (driver)

def linuxSearchByXpath(website, identifier, uinput):
    driver= webdriver.Firefox(executable_path='./geckodriver_linux64', firefox_binary='/usr/lib/firefox/firefox')
    driver.get(website)
    try:
        search=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,identifier)))
    except:
        print('Error in waiting for loading page')
        driver.quit()
        return ('error')

    #search= driver.find_element_by_xpath(identifier)
    search.send_keys(uinput)
    search.send_keys(Keys.RETURN)


    driver.quit()
    return (driver)

def linuxSearchByTagName(website, identifier, uinput):
    driver= webdriver.Firefox(executable_path='./geckodriver_linux64', firefox_binary='/usr/lib/firefox/firefox')
    driver.get(website)
    try:
        search=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.TAG_NAME,identifier)))
    except:
        print('Error in waiting for loading page or element not found')
        driver.quit()
        return ('error')

    #search= driver.find_element_by_tag_name(identifier)

    search.send_keys(uinput)
    search.send_keys(Keys.RETURN)


    driver.quit()
    return (driver)

def linuxSearchByLinkText(website, identifier, uinput):
    driver= webdriver.Firefox(executable_path='./geckodriver_linux64', firefox_binary='/usr/lib/firefox/firefox')
    driver.get(website)
    try:
        search=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.LINK_TEXT,identifier)))
    except:
        print('Error in waiting for loading page')
        driver.quit()
        return ('error')

    #search= driver.find_element_by_link_text(identifier)
    search.send_keys(uinput)
    search.send_keys(Keys.RETURN)


    driver.quit()
    return (driver)
