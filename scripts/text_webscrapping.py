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
def comments_webscrpping(data,pos_ini,pos_fin,ruta):

    ### Reads tha database
    try: 
        comments_data=pd.read_csv(ruta+'/comments.csv')
    except: 
        comments_data=pd.DataFrame()
    # Open firefox navigator
    driver = webdriver.Firefox()
    contador=0
    # Iterates over the list of apps
    for i in data['App Name'][pos_ini:pos_fin]:
        print(contador)
        contador=contador+1
        print(i)
        driver.get("https://play.google.com/")
        # search for the search field in the webpage
        select = driver.find_element_by_id('gbqfq')
        # send the name of the app to the search field  
        select.send_keys(i)
        # click in search button 
        driver.find_element_by_id("gbqfb").click()

        # sleep for 1 seconds
        sleep(1)
        # find the first element of the search that belogs to an app 
        l=driver.find_elements_by_class_name("poRVub")

        for j in l:
            if j.get_attribute('href')[30:34]=='apps':
                j.click()
                break
        try:
            ## Scroll until the review button
            driver.execute_script("window.scrollTo(0, 1230)") 
            sleep(2)
            driver.find_elements_by_class_name("CwaK9")[2].click()
            ## Order by newest
            driver.find_elements_by_class_name("vRMGwf")[2].click()
            sleep(1)
            driver.find_elements_by_class_name("MocG8c")[3].click()
            sleep(1)
            lista_texto=[]
            lista_comments=[]
            lista_dates=[]
            for h in range(4,14):
                try:
                    texto=driver.find_elements_by_class_name("UD7Dzf")
                    fecha=driver.find_elements_by_class_name("p2TkOb")
                    aux_var=texto[h].text
                    aux_var_1=fecha[(h+1)].text
                    lista_comments.append(aux_var)
                    lista_dates.append(aux_var_1)
                except: 
                    aux_var=None
                    aux_var_1=None
                    lista_comments.append(aux_var)
                    lista_dates.append(aux_var_1)

            data_text=pd.DataFrame()
            data_text['date']=lista_dates
            data_text['comment']=lista_comments
            data_text['app_name']=i

            comments_data=comments_data.append(data_text)
            comments_data.to_csv(ruta+'/comments.csv',index=False)
        except: 
            a=1


comments_webscrpping(data,263,1000,'/Users/richardgil/Documents/BGSE/stats/finalproyect-stats/data/comments')

# FOR TEST
# pru=pd.read_csv('/Users/richardgil/Documents/BGSE/stats/finalproyect-stats/data/comments'+'/comments.csv')
# pd.set_option('display.max_columns', None)
# pru.shape
# pru.tail(40)