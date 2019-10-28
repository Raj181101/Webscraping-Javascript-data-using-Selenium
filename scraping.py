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
        

###################### Second Way Scraping Data and Pagination and Writing Data To Excel Files##############

''' from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests
import xlsxwriter

Details = []
count =0

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome('/home/medeaz/chromedriver',options=options)

def detail(x,name):
	r = requests.get(x) 
	soup = BeautifulSoup(r.content, 'lxml')
	y = soup.findAll('span', attrs = {'itemprop':'address'})
	z = soup.findAll('div', attrs = {'class':'span8'})
	a = soup.findAll('div', attrs = {'class':'content'})
	b = soup.findAll('span', attrs = {'itemprop':'url'})


	
	if y == []:
			Address = "NA"
	else:
			add = y[0].text
			Address = add.rstrip()

	if z == []:
			Mobile_Number = "NA"
	else:
			Mobile_Number = z[1].text

	if b == []:
			website = "NA"
	else:
			website = b[0].text
		#Contact_person = z[1].text



	print('Name  -----   ',name)
	# print('Website  -----   ',website)
	# print('Address  -----   ',add.rstrip())
	# print('Contact_Person  -----  ',Contact_person)
	# print('Mobile_Number  -----   ',Mobile_Number)
	#print()

	#print('Company Desc  -----   ',a[2].text)
	# Details.extend([[name,website,Mobile_Number,Address]])
	#print(Details)
	##### Writing Data To the Excel File #####
	# with xlsxwriter.Workbook('Details1.xlsx') as workbook:
	# 	worksheet = workbook.add_worksheet()
					
	# 	for row_num, data in enumerate(Details):
	# 		#print('Row',row_num,data)
	# 		worksheet.write_row(row_num, 0, data)



cnt = 406

def Links(url):
	driver.get(url)
	ps = driver.find_elements_by_xpath("//a[@class='link']")
	for p in ps:
		x = p.get_attribute("href")
		c=p.text
		detail(x,c)
	else:
		global cnt
		cnt = cnt+1
		print(cnt)
		if(cnt == 493):
			print("All pages completed")
		else:
			url1 = 'https://www.vcsdata.com/companies_hyderabad.html?tot_page=8&company_name=&category=&sort_by=&turn_by=&emp_by=&sec_by=&city=Hyderabad&page='+str(cnt)
			print('All Items Are Completed Successfully')
			Links(url1)


url = 'https://www.vcsdata.com/companies_hyderabad.html?tot_page=8&company_name=&category=&sort_by=&turn_by=&emp_by=&sec_by=&city=Hyderabad&page=406'
Links(url)  '''


