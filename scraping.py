from selenium import webdriver
from bs4 import BeautifulSoup
import requests 



def raj(x,name):
    r = requests.get(x) 
    soup = BeautifulSoup(r.content, 'lxml')
    y = soup.findAll('span', attrs = {'itemprop':'address'})
    z = soup.findAll('div', attrs = {'class':'span8'})
    a = soup.findAll('div', attrs = {'class':'content'})
    name=name
    try:
        print('Name  -----   ',name)
        add = y[0].text
        print('Address  -----   ',add.rstrip())
        print('Contact_Person  -----  ',z[1].text)
        print('Mobile_Number  -----   ',z[3].text)
        print('Company Desc  -----   ',a[2].text)
        print()
        print()
    except:
        pass

cnt = 1

def Mains(url):
    driver = webdriver.Chrome()
    driver.get(url)
    ps = driver.find_elements_by_xpath("//a[@class='link']")
    
    for p in ps:
        x = p.get_attribute("href")
        c=p.text
        raj(x,c)

    else:
        global cnt
        cnt = cnt+1
        print(cnt)
        url1 = 'https://www.vcsdata.com/companies_hyderabad.html?tot_page=8&company_name=&category=&sort_by=&turn_by=&emp_by=&sec_by=&city=Hyderabad&page='+str(cnt)
        print('All Items Are Completed Successfully')
        #print(url1)
        Mains(url1)

url = 'https://www.vcsdata.com/companies_hyderabad.html?tot_page=8&company_name=&category=&sort_by=&turn_by=&emp_by=&sec_by=&city=Hyderabad&page=1'
Mains(url)
        





