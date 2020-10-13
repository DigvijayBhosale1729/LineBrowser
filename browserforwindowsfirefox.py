from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os


#Adds Browser to the PATH so that the drivers can be accessed
os.environ['PATH'] += 'C:\\Browser'
def windowsOpenSite(website):
    if website=='close':
        return()
    #create a webdriver object
    driver= webdriver.Firefox(executable_path='./geckodriver_win64.exe')
    driver.get(website)


    return (driver)

def windowsSearchByID(website, identifier, uinput):
    driver= webdriver.Firefox(executable_path='./geckodriver_win64.exe')
    driver.get(website)
    try:
        search=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,identifier)))
    except:
        print('Error in waiting for loading page')
        driver.quit()
        return ('error')
    #search= driver.find_element_by_id(identifier)
    search.send_keys(uinput)
    search.send_keys(Keys.RETURN)



    return (driver)

def windowsSearchByName(website, identifier, uinput):
    driver= webdriver.Firefox(executable_path='./geckodriver_win64.exe')
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



    return (driver)

def windowsSearchByXpath(website, identifier, uinput):
    driver= webdriver.Firefox(executable_path='./geckodriver_win64.exe')
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



    return (driver)

def windowsSearchByTagName(website, identifier, uinput):
    driver= webdriver.Firefox(executable_path='./geckodriver_win64.exe')
    driver.get(website)
    try:
        search=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.TAG_NAME,identifier)))
    except:
        print('Error in waiting for loading page')
        driver.quit()
        return ('error')

    #search= driver.find_element_by_tag_name(identifier)
    search.send_keys(uinput)
    search.send_keys(Keys.RETURN)



    return (driver)

def windowsSearchByLinkText(website, identifier, uinput):
    driver= webdriver.Firefox(executable_path='./geckodriver_win64.exe')
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



    return (driver)
