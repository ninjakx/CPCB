from bs4 import BeautifulSoup
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 
import glob,os
import datetime as dt
import requests 
import pickle
import pandas as pd
from pyvirtualdisplay import Display
'''
try:
    os.remove("example.csv")

except OSError:
    pass
'''

#display = Display(visible=0, size=(800, 600))
#display.start()
chromedriver_loc = '/home/ninjakx/Desktop/Air-Health-master/chromedriver-Linux64' # enter path of chromedriver
driver = webdriver.Chrome(executable_path=chromedriver_loc)
url ="http://www.cpcb.gov.in/CAAQM/frmUserAvgReportCriteria.aspx"

driver.get(url)

# //*[@id="ddlState"]


'''cookies = driver.get_cookies() 

s = requests.Session()
for cookie in cookies:
    s.cookies.set(cookie['name'], cookie['value'])'''


select = Select(driver.find_element_by_id('ddlState'))

# select by visible text
select.select_by_visible_text('Delhi')

time.sleep(8)

select = Select(driver.find_element_by_id('ddlCity'))
select.select_by_visible_text('Delhi')
time.sleep(11)

select = Select(driver.find_element_by_id('ddlStation'))
select.select_by_visible_text('Dwarka')
time.sleep(11)
# //*[@id="btnAdd"]
# //*[@id="lstBoxChannelLeft"]

# //select[@id='numReturnSelect']/option[@value='15000']
your_choice=driver.find_element_by_xpath("//select[@id='lstBoxChannelLeft']/option[@value='484']")
your_choice.click()

driver.find_element_by_xpath('//*[@id="btnAdd"]').click()
time.sleep(11)


your_choice=driver.find_element_by_xpath("//select[@id='lstBoxChannelLeft']/option[@value='874']")
your_choice.click()

driver.find_element_by_xpath('//*[@id="btnAdd"]').click()
time.sleep(11)

your_choice=driver.find_element_by_xpath("//select[@id='lstBoxChannelLeft']/option[@value='1366']")
your_choice.click()

driver.find_element_by_xpath('//*[@id="btnAdd"]').click()
time.sleep(11)

your_choice=driver.find_element_by_xpath("//select[@id='lstBoxChannelLeft']/option[@value='1377']")
your_choice.click()

driver.find_element_by_xpath('//*[@id="btnAdd"]').click()
time.sleep(11)

your_choice=driver.find_element_by_xpath("//select[@id='lstBoxChannelLeft']/option[@value='864']")
your_choice.click()

driver.find_element_by_xpath('//*[@id="btnAdd"]').click()
time.sleep(11)

your_choice=driver.find_element_by_xpath("//select[@id='lstBoxChannelLeft']/option[@value='824']")
your_choice.click()

driver.find_element_by_xpath('//*[@id="btnAdd"]').click()
time.sleep(9)

your_choice=driver.find_element_by_xpath("//select[@id='lstBoxChannelLeft']/option[@value='502']")
your_choice.click()


driver.find_element_by_xpath('//*[@id="btnAdd"]').click()
time.sleep(9)


# //*[@id="txtDateFrom"]
datefield = driver.find_element_by_xpath('//*[@id="txtDateFrom"]')
datefield.click()
datefield.clear()

datefield.send_keys("01/01/2018")

time.sleep(4)

datefield = driver.find_element_by_xpath('//*[@id="txtDateTo"]')
datefield.click()
datefield.clear()
datefield.send_keys("3/02/2018")
#datefield.send_keys(dt.datetime.today().strftime("%d/%m/%Y"))
time.sleep(4)

driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()

time.sleep(15)


html = driver.page_source
soup = BeautifulSoup(html,'html.parser')
time.sleep(5)
dframe = []
#print(soup)
table = soup.find('table',{'width':'100%','border':'1'})
#print(table)
#print(len(str(table)))
#table = (str(table))
#print(table)
#df1 = pd.DataFrame()

#table = soup.findAll('table')
#for tb in table[0]:
date=[]
conc=[]      
d = table.findAll('td',{'width':'6%'})
n = table.findAll('td',{'width':'10%'})
param = table.findAll('td',{'width':'30%'})
param = (param[1].text)[1:]
print(param)

#print(d)
i=-1
for dat in d[1:]:
    i += 1
    #if date!=None:
    dat=dat.text
    c = n[i+1].text
    date.append(dat)
    conc.append(c)
df = pd.DataFrame({'Date': date, param: conc})
#print(df)
dframe.append(df)
#print(no2,date)





'''
df = (pd.read_html(str(table)))[0]
print("a")
df.drop(df.index[0], inplace=True)
print("b")
df.columns = df.iloc[0]
print("c")
name = df['Parameter'].iloc[1]
print("d")
df = df.drop('Parameter', 1)
print("e")
df=df.rename(columns = {'Concentration':name})
print("f")
df = df[1:]
df = df.drop('Remarks', 1)
df = df.drop('Unit', 1)
df = df.drop('Prescribed Standard', 1)
df = df.drop('Exceeding Standard? (Yes/No)', 1)
df = df[df.Date.notnull()]
dframe.append(df)  
print("g")
'''




#print(soup)

# //*[@id="gvReportStation"]/tbody/tr[1]/td/table/tbody/tr/td[2]/a
# //*[@id="gvReportStation"]/tbody/tr[3]/td/table/tbody/tr/td[3]/a
# //*[@id="gvReportStation"]/tbody/tr[1]/td/table/tbody/tr/td[4]/a

# //*[@id="btnNext1"]

# //*[@id="gvReportStation"]/tbody/tr[1]/td/table/tbody/tr/td[3]/a : after 3


# //*[@id="gvReportStation"]/tbody/tr[1]/td/table/tbody/tr/td[1]/a  :after 1 
# //*[@id="gvReportStation"]/tbody/tr[1]/td/table/tbody/tr/td[2]/a : after 2

xpath = ['//*[@id="gvReportStation"]/tbody/tr[1]/td/table/tbody/tr/td[2]/a',
        '//*[@id="gvReportStation"]/tbody/tr[1]/td/table/tbody/tr/td[3]/a',
        '//*[@id="gvReportStation"]/tbody/tr[1]/td/table/tbody/tr/td[4]/a',
        '//*[@id="btnNext1"]',
        '//*[@id="gvReportStation"]/tbody/tr[1]/td/table/tbody/tr/td[1]/a',
        '//*[@id="gvReportStation"]/tbody/tr[1]/td/table/tbody/tr/td[2]/a',
]


ind = -1

print("yes")

while(1):
 try:
    ind += 1
    print(xpath[ind])
    driver.find_element_by_xpath(xpath[ind]).click()
    print('1')
    time.sleep(13)
    #print(soup)
    html = driver.page_source
    print('2')
    soup = BeautifulSoup(html,'html.parser')
    print('3')

    table = soup.find('table',{'width':'100%','border':'1'})
    date=[]
    conc=[]      
    d = table.findAll('td',{'width':'6%'})
    n = table.findAll('td',{'width':'10%'})
    param = table.findAll('td',{'width':'30%'})
    param = (param[1].text)[1:]
    print(param)

    #print(d)
    i=-1
    for dat in d:
        i += 1
        #if date!=None:
        dat=dat.text
        c = n[i].text
        date.append(dat)
        conc.append(c)
    df = pd.DataFrame({'Date': date, param: conc})
    df = df[1:]
    #df.columns = df.iloc[1]
    print(df)
    dframe.append(df) 
    #print(df)


 except:
    break

df = pd.concat([d.set_index('Date') for d in dframe], axis=1).reset_index()
#df = df.sort_values('1')

with open('dwarka-2018.csv', 'w') as fw:
    df.to_csv(fw, sep=';', encoding='utf-8', index=False)

print(df)
driver.quit()
#display.stop()

'''for no2 in n :
            if no2!
                no2 = conc.text
                print(date,no2)'''

        #for tr_i in tr:
 
        #date = tr_i.find('td',{'width':'6%'})
        #conc = tr_i.find('td',{'width':'10%'})
        #if conc == conc:
        #    conc = conc.txt
'''if date!=None:
                date=date.text
                no2 = conc.text
                print(date,no2)'''
'''while(1):
 try:
    ind += 1
    print(xpath[ind])
    driver.find_element_by_xpath(xpath[ind]).click()
    print('1')
    time.sleep(13)
    #print(soup)
    html = driver.page_source
    print('2')
    soup = BeautifulSoup(html,'html.parser')
    print('3')

    table = soup.find('table',{'width':'100%','border':'1'})
    print('4')
    #print(len(str(table)))
    #table = ET.parse(str(table))
    #print(table)
    #df1 = pd.DataFrame()
    #heading = ['NO2','SO2','TEMP','P']
    df = (pd.read_html(str(table)))[0]
    print('5')
    print("len:",len(df))
    if len(df) > 3 :
        #print(len(df))

        df.drop(df.index[0], inplace=True)
        print('6')
        df.columns = df.iloc[0]
        name = df['Parameter'].iloc[1]
        df = df.drop('Parameter', 1)
        df=df.rename(columns = {'Concentration':name})
        df = df[1:]
        df = df.drop('Remarks', 1)
        df = df.drop('Unit', 1)
        df = df.drop('Prescribed Standard', 1)
        df = df.drop('Exceeding Standard? (Yes/No)', 1)
        #df = df[df.Date.notnull()]
        print('7')
        print(name)

        #df['Parameter'] = df['Parameter'].iloc[0]
        #df1 = df[['Parameter']]

        #print(df1)

        #df = df.concat([df1,df], axis=1)
        #print(df)
        #table = ET.fromstring(str(table))
        #df = pd.concat(df, axis=1)

        #print(df)
        dframe.append(df)  
        print('8')
        time.sleep(5)



 except:
    break
print("IIII",ind)
#for pf in dframe:
    #print(pf) 
    #print('9')
df = pd.concat([d.set_index('Date') for d in dframe], axis=1).reset_index()
    #print("hj",pf)
#print(len(pf))
print(df)
with open('dwarka-2010.csv', 'w') as fw:
    df.to_csv('dwarka-2010.csv', sep=';', encoding='utf-8')
'''

#time.sleep(20)


#calls_df = pd.read_html(soup)

#print(calls_df)


"""
#for path in glob.glob('a.txt'):
    #with open(path) as markup:
        soup = BeautifulSoup(markup.read())
    
    table = soup.findAll('table')
    print(len(table))
    #print(table[0])
    index=[]
    for tb in table[0]:
       
        d = tb.findAll('td',{'width':'6%'})
        n = tb.findAll('td',{'width':'10%'})
        i=-1
        for date in d:
            i += 1
            if date!=None:
                date=date.text
                no2 = n[i].text
                print(no2,date)
                index.append(i)
        '''for no2 in n :
            if no2!
                no2 = conc.text
                print(date,no2)'''

        #for tr_i in tr:
 
        #date = tr_i.find('td',{'width':'6%'})
        #conc = tr_i.find('td',{'width':'10%'})
        #if conc == conc:
        #    conc = conc.txt
        '''if date!=None:
                date=date.text
                no2 = conc.text
                print(date,no2)'''

    for tb in table[1:]:
        #print(1)

        t = tb.findAll('td',{'width':'10%','align':'right'})
        for temp in t :
            temp=temp.text
            print(temp)
        '''for i in index:
            temp = t[i].text
            print(temp)
        '''
        #date = (date.text if date!=None else "Nan")
        #conc = (conc.text if conc!=None else "Nan")
        #conc = conc.text
           


    #print(soup)
"""
