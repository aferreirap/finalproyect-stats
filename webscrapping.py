from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
from time import sleep
import urllib.request
import pandas as pd


### Read the csv 
data=pd.read_csv('./data/app_sample.csv')

### Function that webscrape images from the google playstore
### @data: dataframe with the names of the apss
### @pos_ini: initial position of the list of apps, the webscrap begins in this app
### @pos_fin: final position of the list of apps, the webscrap ends in this app
def image_webscrpping(data,pos_ini,pos_fin):
    # Open firefox navigator
    driver = webdriver.Firefox()
    # Iterates over the list of apps
    for i in data['App Name'][pos_ini:pos_fin]:
        # Open the google playstore webpage
        driver.get("https://play.google.com/")
        # search for the search field in the webpage
        select = driver.find_element_by_id('gbqfq')
        # send the name of the app to the search field
        select.send_keys(i)
        # click in search button 
        driver.find_element_by_id("gbqfb").click()
        # sleep for 3 seconds
        sleep(3)
        # find the first element of the search that belogs to an app 
        l=driver.find_elements_by_class_name("poRVub")
        for j in l:
            if j.get_attribute('href')[30:34]=='apps':
                j.click()
                break
        # sleep for 3 second
        sleep(3)
        # find the element for the image
        r=driver.find_elements_by_xpath("//*[@itemprop='image']")
        # get the attribute image
        src = r[0].get_attribute('src')
        #save the image in the path
        urllib.request.urlretrieve(src, "./data/images/"+i+".png")
   