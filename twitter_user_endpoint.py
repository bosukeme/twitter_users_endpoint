from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options=Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')
options.add_argument('--disable-extensions')
options.add_argument('headless')

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from time import sleep
import re
import os
import pandas as pd
import json


#handles=''
#handles=[handles]



def process_metadata(handles):

    handles=[handles]
    driver=webdriver.Chrome(executable_path="/usr/lib/chromium-browser/chromedriver", chrome_options=options)
    driver.wait = WebDriverWait(driver, 5)
    
 

    names=[]
    followers_counts=[]
    profile_photos=[]
    biographies=[]
    
    for handle in handles:
        
        

        url='https://twitter.com/'+ handle

        #print(url)
        driver.get(url) ##open the site
        driver.wait = WebDriverWait(driver, 5)
        #sleep(5)


        ##getting the name
        class_path= "[class='css-1dbjc4n r-15d164r r-1g94qm0']"
        driver.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, class_path)))
        main=driver.find_elements_by_css_selector(class_path)
        sleep(5)
        name=[a.text.split('\n') for a in main][0][0]
        names.append(name)
       # name=[name]
       # print(name)



        ##getting the followers count
        class_path= "[class='css-1dbjc4n r-18u37iz r-1w6e6rj']"
        driver.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, class_path)))
        main=driver.find_elements_by_css_selector(class_path)
        #sleep(3)
        followers_count=[a.text.split('\n') for a in main][0][1]
        followers_count=followers_count.strip('Followers ')
        
        if 'M' in followers_count:
            followers_count=followers_count.strip('M')
            followers_count=followers_count.replace(',','')
            followers_count=float(followers_count)
            followers_count=followers_count*1000000
            
        elif 'K' in followers_count:
            followers_count=followers_count.strip('K')
            followers_count=followers_count.replace(',','')
            followers_count=float(followers_count)
            followers_count=followers_count*1000
        else:
            followers_count=followers_count.replace(',','')
            followers_count=float(followers_count)

        
        followers_counts.append(followers_count)
        #followers_count=[followers_count]
        #print(followers_count)



        profile_photo="https://twitter.com/" +handle+ "/photo"
        profile_photos.append(profile_photo)
        #profile_photo=[profile_photo]
        #print(profile_photo)



        ##getting the biography
        class_path= "[class='css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-qvutc0']"
        driver.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, class_path)))
        main=driver.find_elements_by_css_selector(class_path)
        sleep(5)
        biography=[a.text for a in main]
        biographies.append(biography)
        #biography=[biography]
        #print(biography)
        
        handle=handles[:7]
        
        
    
    return_dict={"Handle": handle[0],
                "Full name": names[0],
                "Followers_count": followers_counts[0],
                "Profile_photo":profile_photos[0],
                "Bio Data": biographies[0]}
    
        
        
    #print(return_dict)
    return  return_dict
#process_metadata(handles)
