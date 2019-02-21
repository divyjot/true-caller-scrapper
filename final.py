
import csv      #importing CSV module
import bs4      #importing BeautifulSoup4
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

#Giving driver the default firefox profile
profile = webdriver.FirefoxProfile('/root/.mozilla/firefox/9oz6e427.default')
driver=webdriver.Firefox(profile)
f1=open("numbers.txt","w")

#Reading the CSV file and storing the object in "contents"
with open('num.csv','r') as file:
    contents = csv.reader(file)

    for x in contents:  #Parsing the contents i.e. numbers
            #Requesting truecaller with phone number appended url ;)
            driver.get('https://truecaller.com/search/in/'+x[0])

            #Delay to allow webpage to load fully (may have to change accordingly)
            time.sleep(3)

            response=driver.execute_script('return document.documentElement.innerHTML')
            soup=BeautifulSoup(response,'html.parser')

            #finding div containing name
            result=soup.find('div',{'class':'ProfileName'}).text
            #driver.quit()f
            print(x[0]+" : "+result)
            f1.write(x[0]+" : "+result+"\n")

driver.quit()
