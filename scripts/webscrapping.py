from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import urllib

driver = webdriver.Firefox()


driver.get("https://play.google.com/")
select = driver.find_element_by_id('gbqfq')
select.send_keys("imocci")
driver.find_element_by_id("gbqfb").click()

l=driver.find_elements_by_class_name("poRVub")
l[0]
for i in l:
    if i.get_attribute('href')[30:34]=='apps':
        i.click()
        break


r=driver.find_elements_by_xpath("//*[@class='T75of' or @class='sHb2Xb']")
r=driver.find_elements_by_xpath("//div[contains(@class, 'T75of') and contains(@class, 'sHb2Xb')]")

print(r)

<img src="https://play-lh.googleusercontent.com/fNcZB0MzK9uwBAqkcqeJxblWn6o_R5rTwt4XgbUbt2gFIbGLYnFm7xML0_Y0XgYtlm8=s180" srcset="https://play-lh.googleusercontent.com/fNcZB0MzK9uwBAqkcqeJxblWn6o_R5rTwt4XgbUbt2gFIbGLYnFm7xML0_Y0XgYtlm8=s360 2x" class="T75of sHb2Xb" aria-hidden="true" alt="Cover art" itemprop="image" data-atf="false" data-iml="12152">
h=r[0].get_attribute('src')
print(h)
r[1]
print(h.get_attribute('src'))

import urllib.request
urllib.request.urlretrieve(h, "captcha.png")


<div class="xSyT2c"><img src="https://play-lh.googleusercontent.com/fNcZB0MzK9uwBAqkcqeJxblWn6o_R5rTwt4XgbUbt2gFIbGLYnFm7xML0_Y0XgYtlm8=s180" srcset="https://play-lh.googleusercontent.com/fNcZB0MzK9uwBAqkcqeJxblWn6o_R5rTwt4XgbUbt2gFIbGLYnFm7xML0_Y0XgYtlm8=s360 2x" class="T75of sHb2Xb" aria-hidden="true" alt="Cover art" itemprop="image" data-atf="false" data-iml="12152"></div>
<img src="https://play-lh.googleusercontent.com/fNcZB0MzK9uwBAqkcqeJxblWn6o_R5rTwt4XgbUbt2gFIbGLYnFm7xML0_Y0XgYtlm8=s180" srcset="https://play-lh.googleusercontent.com/fNcZB0MzK9uwBAqkcqeJxblWn6o_R5rTwt4XgbUbt2gFIbGLYnFm7xML0_Y0XgYtlm8=s360 2x" class="T75of sHb2Xb" aria-hidden="true" alt="Cover art" itemprop="image" data-atf="false" data-iml="11624">
src = img.get_attribute('src')

# download the image

data = urllib.request.urlretrieve
urllib.request.urlretrieve(src, "captcha.png")
#l=driver.find_elements_by_class_name("poRVub")
#for i in l:
#    print(i.get_attribute('href'))


#<div class="WsMG1c nnK0zc" title="Netflix">Netflix</div>
#<a href="/store/apps/details?id=com.netflix.mediaclient" aria-hidden="true" tabindex="-1" class="poRVub"></a>
#<a href="/store/apps/details?id=com.netflix.mediaclient" aria-hidden="true" tabindex="-1" class="JC71ub"></a>