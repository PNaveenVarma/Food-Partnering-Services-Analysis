
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import regex
import re

driver = webdriver.Firefox(executable_path=r"/Users/naveenvarma/Documents/geckodriver")
# navigating through the pages until my reqired page for sraping the data is found.
ubereats_url = 'https://www.ubereats.com/feed?diningMode=PICKUP&pl=JTdCJTIyYWRkcmVzcyUyMiUzQSUyMlN0aWxsd2F0ZXIlMjIlMkMlMjJyZWZlcmVuY2UlMjIlM0ElMjJDaElKSTYtWjZfa0pzWWNSbWRFUUlCYmFrWXclMjIlMkMlMjJyZWZlcmVuY2VUeXBlJTIyJTNBJTIyZ29vZ2xlX3BsYWNlcyUyMiUyQyUyMmxhdGl0dWRlJTIyJTNBMzYuMTE1NjA3MSUyQyUyMmxvbmdpdHVkZSUyMiUzQS05Ny4wNTgzNjgxJTdE&ps=1&sf=JTVCJTdCJTIydXVpZCUyMiUzQSUyMjFjN2NmN2VmLTczMGYtNDMxZi05MDcyLTI2YmMzOWY3YzAyMSUyMiUyQyUyMm9wdGlvbnMlMjIlM0ElNUIlN0IlMjJ1dWlkJTIyJTNBJTIyNGM3Y2Y3ZWYtNzMwZi00MzFmLTkwNzItMjZiYzM5ZjdjMDIzJTIyJTdEJTVEJTdEJTJDJTdCJTIydXVpZCUyMiUzQSUyMjJjN2NmN2VmLTczMGYtNDMxZi05MDcyLTQ2YmMzOWY3YzAyMSUyMiUyQyUyMm9wdGlvbnMlMjIlM0ElNUIlN0IlMjJ1dWlkJTIyJTNBJTIyMmM3Y2Y3ZWYtNzMwZi00MzFmLTkwNzItMjZiYzM5ZjdjMDMzJTIyJTdEJTVEJTdEJTVE'
driver.get(ubereats_url)
time.sleep(2)
#q1 = driver.find_elements(By.CLASS_NAME,'b0 cd ca eq er es et eu')
#length = len(q1)
#print(length)


cus_list = ['American','Asian','Bakery','Mexican','Chinese','Fast Food','Coffee and Tea','Sandwich']
length = [18,3,3,5,2,7,19,19]
af= driver.find_element('link text',cus_list[0])
af.click()

#Amercian
WebDriverWait(driver, timeout=5).until(lambda d: d.find_elements(By.XPATH,'/html/body/div[1]/div[1]/div/main/div/div[1]/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div[1]'))
amer = driver.find_elements(By.XPATH,'/html/body/div[1]/div[1]/div/main/div/div[1]/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div[1]')
#/html/body/div[1]/div[1]/div/main/div/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div/div/div[2]/div[1]
amercian = []
for a in amer :
    amercian.append(a.text) 
    
updated_list=amercian.copy()

for i in range(length[0]):
    x = re.search("5 stars", amercian[i])
    if x:
     print("YES! We have a match!")
    else:
     updated_list.remove(amercian[i])

amercian1 = '\n'.join(updated_list).split('\n')
df_Am = pd.DataFrame(amercian1)
q_Am = len(updated_list)
cusine_Am = []
for j in range(q_Am):
    cusine_Am.append(cus_list[0])

df_Am1 = pd.DataFrame(amercian1[0::3])
df_Am2 = pd.DataFrame(amercian1[1::3])
df_Am3 = pd.DataFrame(amercian1[2::3])
df_Am4 = pd.DataFrame(cusine_Am)
finaldf_Am = [df_Am1,df_Am2,df_Am3,df_Am4]
table_Am = pd.concat(finaldf_Am,axis=1,ignore_index = True)
table_Am.columns=['Resturant','rating description','ratings','cusine']
print(table_Am)
driver.back()
time.sleep(3)

af= driver.find_element('link text',cus_list[1])
af.click()

#Asian
WebDriverWait(driver, timeout=5).until(lambda d: d.find_elements(By.XPATH,'/html/body/div[1]/div[1]/div/main/div/div[1]/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div[1]'))
asi = driver.find_elements(By.XPATH,'/html/body/div[1]/div[1]/div/main/div/div[1]/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div[1]')
#/html/body/div[1]/div[1]/div/main/div/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div/div/div[2]/div[1]
asian = []
for a1 in asi :
    asian.append(a1.text) 
    

time.sleep(5)
updated_list1=asian.copy()

for i1 in range(3):
    x = re.search("5 stars", asian[i1])
    if x:
     print("YES! We have a match!")
    else:
     updated_list1.remove(asian[i1])

asian1 = '\n'.join(updated_list1).split('\n')
df_As = pd.DataFrame(asian1)
q_As = len(updated_list1)
cusine_As = []

for j in range(3):
    cusine_As.append(cus_list[1])

df_As1 = pd.DataFrame(asian1[0::3])
df_As2 = pd.DataFrame(asian1[1::3])
df_As3 = pd.DataFrame(asian1[2::3])
df_As4 = pd.DataFrame(cusine_As)
finaldf_As = [df_As1,df_As2,df_As3,df_As4]
table_As = pd.concat(finaldf_As,axis=1,ignore_index = True)
table_As.columns=['Resturant','rating description','ratings','cusine']
print(table_As)
driver.back()
time.sleep(3)

af= driver.find_element('link text',cus_list[2])
af.click()

#Bakery
WebDriverWait(driver, timeout=5).until(lambda d: d.find_elements(By.XPATH,'/html/body/div[1]/div[1]/div/main/div/div[1]/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div[1]'))
bak = driver.find_elements(By.XPATH,'/html/body/div[1]/div[1]/div/main/div/div[1]/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div[1]')
#/html/body/div[1]/div[1]/div/main/div/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div/div/div[2]/div[1]
bakery = []
for a2 in bak :
    bakery.append(a2.text) 
    

time.sleep(5)
updated_list2=bakery.copy()

for i2 in range(3):
    x = re.search("5 stars", bakery[i2])
    if x:
     print("YES! We have a match!")
    else:
     updated_list2.remove(bakery[i2])

bakery1 = '\n'.join(updated_list2).split('\n')
df_Bk = pd.DataFrame(bakery1)
q_Bk = len(updated_list2)
cusine_Bk = []

for j in range(3):
    cusine_Bk.append(cus_list[2])

df_Bk1 = pd.DataFrame(bakery1[0::3])
df_Bk2 = pd.DataFrame(bakery1[1::3])
df_Bk3 = pd.DataFrame(bakery1[2::3])
df_Bk4 = pd.DataFrame(cusine_Bk)
finaldf_Bk = [df_Bk1,df_Bk2,df_Bk3,df_Bk4]
table_Bk = pd.concat(finaldf_Bk,axis=1,ignore_index = True)
table_Bk.columns=['Resturant','rating description','ratings','cusine']
print(table_Bk)
driver.back()
time.sleep(3)
af= driver.find_element('link text',cus_list[3])
af.click()

#Mexican
WebDriverWait(driver, timeout=5).until(lambda d: d.find_elements(By.XPATH,'/html/body/div[1]/div[1]/div/main/div/div[1]/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div[1]'))
mex = driver.find_elements(By.XPATH,'/html/body/div[1]/div[1]/div/main/div/div[1]/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div[1]')
#/html/body/div[1]/div[1]/div/main/div/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div/div/div[2]/div[1]
mexican = []
for a3 in mex :
    mexican.append(a3.text) 
    

time.sleep(5)
updated_list3=mexican.copy()

for i3 in range(5):
    x = re.search("5 stars", mexican[i3])
    if x:
     print("YES! We have a match!")
    else:
     updated_list3.remove(mexican[i3])

mexican1 = '\n'.join(updated_list3).split('\n')
df_Mx = pd.DataFrame(mexican1)
q_Mx = len(updated_list3)
cusine_Mx = []

for j2 in range(q_Mx):
    cusine_Mx.append(cus_list[3])

df_Mx1 = pd.DataFrame(mexican1[0::3])
df_Mx2 = pd.DataFrame(mexican1[1::3])
df_Mx3 = pd.DataFrame(mexican1[2::3])
df_Mx4 = pd.DataFrame(cusine_Mx)
finaldf_Mx = [df_Mx1,df_Mx2,df_Mx3,df_Mx4]
table_Mx = pd.concat(finaldf_Mx,axis=1,ignore_index = True)
table_Mx.columns=['Resturant','rating description','ratings','cusine']
print(table_Mx)
driver.back()
time.sleep(3)

af= driver.find_element('link text',cus_list[4])
af.click()

#Chinese
WebDriverWait(driver, timeout=5).until(lambda d: d.find_elements(By.XPATH,'/html/body/div[1]/div[1]/div/main/div/div[1]/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div[1]'))
chin = driver.find_elements(By.XPATH,'/html/body/div[1]/div[1]/div/main/div/div[1]/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div[1]')
#/html/body/div[1]/div[1]/div/main/div/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div/div/div[2]/div[1]
chinese = []
for a4 in chin :
    chinese.append(a4.text) 
    

time.sleep(5)
updated_list4=chinese.copy()

for i4 in range(2):
    x = re.search("5 stars", chinese[i4])
    if x:
     print("YES! We have a match!")
    else:
     updated_list4.remove(chinese[i4])

chinese1 = '\n'.join(updated_list4).split('\n')
df_Ch = pd.DataFrame(chinese1)
q_Ch= len(updated_list4)
cusine_Ch = []

for j3 in range(2):
    cusine_Ch.append(cus_list[4])

df_Ch1 = pd.DataFrame(chinese1[0::3])
df_Ch2 = pd.DataFrame(chinese1[1::3])
df_Ch3 = pd.DataFrame(chinese1[2::3])
df_Ch4 = pd.DataFrame(cusine_Ch)
finaldf_Ch = [df_Ch1,df_Ch2,df_Ch3,df_Ch4]
table_Ch = pd.concat(finaldf_Ch,axis=1,ignore_index = True)
table_Ch.columns=['Resturant','rating description','ratings','cusine']
print(table_Ch)
driver.back()
time.sleep(3)

af= driver.find_element('link text',cus_list[5])
af.click()

#Fastfood
WebDriverWait(driver, timeout=5).until(lambda d: d.find_elements(By.XPATH,'/html/body/div[1]/div[1]/div/main/div/div[1]/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div[1]'))
ff = driver.find_elements(By.XPATH,'/html/body/div[1]/div[1]/div/main/div/div[1]/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div[1]')
#/html/body/div[1]/div[1]/div/main/div/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div/div/div[2]/div[1]
fastfood = []
for a6 in ff :
    fastfood.append(a6.text) 
    

time.sleep(5)
updated_list6=fastfood.copy()

for i6 in range(7):
    x = re.search("5 stars", fastfood[i6])
    if x:
     print("YES! We have a match!")
    else:
     updated_list6.remove(fastfood[i6])

fastfood1 = '\n'.join(updated_list6).split('\n')
df_FF = pd.DataFrame(fastfood1)
q_FF= len(updated_list6)
cusine_FF = []

for j5 in range(q_FF):
    cusine_FF.append(cus_list[5])

df_FF1 = pd.DataFrame(fastfood1[0::3])
df_FF2 = pd.DataFrame(fastfood1[1::3])
df_FF3 = pd.DataFrame(fastfood1[2::3])
df_FF4 = pd.DataFrame(cusine_FF)
finaldf_FF = [df_FF1,df_FF2,df_FF3,df_FF4]
table_FF = pd.concat(finaldf_FF,axis=1,ignore_index = True)
table_FF.columns=['Resturant','rating description','ratings','cusine']
print(table_FF)
driver.back()
time.sleep(3)

af= driver.find_element('link text',cus_list[6])
af.click()

#Coffe and Tea
WebDriverWait(driver, timeout=5).until(lambda d: d.find_elements(By.XPATH,'/html/body/div[1]/div[1]/div/main/div/div[1]/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div[1]'))
CT = driver.find_elements(By.XPATH,'/html/body/div[1]/div[1]/div/main/div/div[1]/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div[1]')
#/html/body/div[1]/div[1]/div/main/div/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div/div/div[2]/div[1]
CoffeTea = []
for a7 in CT :
    CoffeTea.append(a7.text) 
    

time.sleep(5)
updated_list7=CoffeTea.copy()

for i7 in range(19):
    x = re.search("5 stars", CoffeTea[i7])
    if x:
     print("YES! We have a match!")
    else:
     updated_list7.remove(CoffeTea[i7])

CoffeTea1 = '\n'.join(updated_list7).split('\n')
df_CT = pd.DataFrame(CoffeTea1)
q_CT= len(updated_list6)
cusine_CT = []

for j6 in range(q_CT):
    cusine_CT.append(cus_list[6])

df_CT1 = pd.DataFrame(CoffeTea1[0::3])
df_CT2 = pd.DataFrame(CoffeTea1[1::3])
df_CT3 = pd.DataFrame(CoffeTea1[2::3])
df_CT4 = pd.DataFrame(cusine_CT)
finaldf_CT = [df_CT1,df_CT2,df_CT3,df_CT4]
table_CT = pd.concat(finaldf_CT,axis=1,ignore_index = True)
table_CT.columns=['Resturant','rating description','ratings','cusine']
print(table_CT)
driver.back()
time.sleep(3)

cusine = driver.find_element('link text','Comfort Food')
driver.execute_script("arguments[0].scrollIntoView();",cusine)
time.sleep(3)
af= driver.find_element('link text',cus_list[7])
af.click()


#Sandwitch
WebDriverWait(driver, timeout=5).until(lambda d: d.find_elements(By.XPATH,'/html/body/div[1]/div[1]/div/main/div/div[1]/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div[1]'))
sand = driver.find_elements(By.XPATH,'/html/body/div[1]/div[1]/div/main/div/div[1]/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div[1]')
#/html/body/div[1]/div[1]/div/main/div/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div/div/div[2]/div[1]
sandwitch = []
for a5 in sand :
    sandwitch.append(a5.text) 
    

time.sleep(5)
updated_list5=sandwitch.copy()

for i5 in range(19):
    x = re.search("5 stars", sandwitch[i5])
    if x:
     print("YES! We have a match!")
    else:
     updated_list5.remove(sandwitch[i5])

sandwitch1 = '\n'.join(updated_list5).split('\n')
df_SA = pd.DataFrame(sandwitch1)
q_SA= len(updated_list5)
cusine_SA = []

for j4 in range(16):
    cusine_SA.append(cus_list[7])

df_SA1 = pd.DataFrame(sandwitch1[0::3])
df_SA2 = pd.DataFrame(sandwitch1[1::3])
df_SA3 = pd.DataFrame(sandwitch1[2::3])
df_SA4 = pd.DataFrame(cusine_SA)
finaldf_SA = [df_SA1,df_SA2,df_SA3,df_SA4]
table_SA = pd.concat(finaldf_SA,axis=1,ignore_index = True)
table_SA.columns=['Resturant','rating description','ratings','cusine']
print(table_SA)
driver.back()
time.sleep(3)

final_concat = [table_Am,table_As,table_Bk,table_Mx,table_Ch,table_SA,table_FF,table_CT]
final_merge = pd.concat(final_concat,axis=0,ignore_index=True)
print(final_merge)
final_merge.to_csv(r'/Users/naveenvarma/Desktop/PDS/final/project-deliverable-2-osu-crackers/data/stillwater/stillwater_dataset.csv',sep='\t',encoding='utf-8')

