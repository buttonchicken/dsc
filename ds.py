from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait 
import time
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
import csv
url='https://npcil.etenders.in/'
driver=webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(5) 
templist=[]
driver.implicitly_wait(10) 
rows=len(driver.find_elements_by_xpath('//*[@id="container"]/div[5]/div[1]/div[2]/table/tbody/tr'))
print(rows)
for r in range(2,rows+1):
 Tender_ID=driver.find_element_by_xpath('//*[@id="container"]/div[5]/div[1]/div[2]/table/tbody/tr['+str(r)+']/td[1]').text
 Tender_No=driver.find_element_by_xpath('//*[@id="container"]/div[5]/div[1]/div[2]/table/tbody/tr['+str(r)+']/td[2]').text
 Tender_type=driver.find_element_by_xpath('//*[@id="container"]/div[5]/div[1]/div[2]/table/tbody/tr['+str(r)+']/td[3]').text
 Department=driver.find_element_by_xpath('//*[@id="container"]/div[5]/div[1]/div[2]/table/tbody/tr['+str(r)+']/td[4]').text
 Tender_Desc=driver.find_element_by_xpath('//*[@id="container"]/div[5]/div[1]/div[2]/table/tbody/tr['+str(r)+']/td[5]').text
 corr=driver.find_element_by_xpath('//*[@id="container"]/div[5]/div[1]/div[2]/table/tbody/tr['+str(r)+']/td[6]').text
 Due_date=driver.find_element_by_xpath('//*[@id="container"]/div[5]/div[1]/div[2]/table/tbody/tr['+str(r)+']/td[7]').text
 url=driver.current_url
 tend_item={
 'Tender ID':Tender_ID,
 'Tender No.':Tender_No,
 'Tender Type':Tender_type,
 'Department':Department,
 'Tender Description':Tender_Desc,
 'Corrigendum/Amendment':corr,
 'Due Date/Time':Due_date,
 'URL':url
 }
 templist.append(tend_item)
 df=pd.DataFrame(templist)
df.to_csv('npcil.csv')
driver.close()
l=list()
file=open('keywords.txt','r')
lines = file.readlines()
keylist=[]
csv_file=csv.reader(open('npcil.csv','r'))
for row in csv_file:
 for line in lines:
  if line.rstrip().lower() in row[5].lower():
   tend_item={
   'Tender ID':row[1],
   'Tender No.':row[2],
   'Tender Type':row[3],
   'Department':row[4],
   'Tender Description':row[5],
   'Corrigendum/Amendment':row[6],
   'Due Date/Time':row[7],
   'URL':row[8]
   }
   keylist.append(tend_item)
   df1=pd.DataFrame(keylist)
try:
 df1.to_csv('npcilfinal.csv')
except NameError:
 print("NO FILE MATCHING THE KEYWORDS!!")
