import requests,bs4
from selenium import webdriver

#Getting the browser
#browser = webdriver.Firefox()

#Signin to linkedin
#browser.get('https://www.linkedin.com')
#usernameElem = browser.find_element_by_css_selector('input[name="session_key"]')
#usernameElem.send_keys('jayeshgar@gmail.com')
#passwordElem = browser.find_element_by_css_selector('input[name="session_password"]')
#passwordElem.send_keys('Namo2018')
#passwordElem.submit()


for page in range(1,10):
	res = requests.get('https://www.linkedin.com/jobs/search/?geoId=102510332&keywords=machine%20learning&location=Pune%2C%20Maharashtra%2C%20India', params={'page': page})
	res.raise_for_status() #Will through an exception if response is not proper

	#Open the file to write the content
	#It has to be in binary mode to take care of unicode characters
	#playFile = open('LinkedinPuneJobs.html','wb')
	#Write content to file
	#for context in res.iter_content(10000):
	#	playFile.write(context)

	#playFile.close()

	playFile = open('joblist.txt','a+')
	nostarchSoup = bs4.BeautifulSoup(res.text,features='lxml')
	jobs = nostarchSoup.select('ul[class="jobs-search__results-list"] li > a')
	for job in jobs:
		playFile.write(job.get('href'))
		playFile.write("\n")
	playFile.close()