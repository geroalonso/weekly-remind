from apscheduler.schedulers.blocking import BlockingScheduler
import time
import smtplib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import os 



sched = BlockingScheduler()
'interval', minutes=3
# @sched.scheduled_job('cron', day_of_week='mon', hour=17)
@sched.scheduled_job('interval', minutes=3)
def scheduled_job():
	url = "https://buildium.na2.echosign.com/public/login"
	driver = webdriver.Chrome(ChromeDriverManager().install()) #set the search engine
	driver.implicitly_wait(10) #set implicit wait
	driver.get(url) #open the browser
	print('driver selected')
	adobe_password = "Iberic1409!!!"
	print('environment variable created')
	login = driver.find_element_by_id("userEmail")
	print('element found')
	password = driver.find_element_by_id("userPassword")
	print('password element found')
	login.send_keys("admin@ibericmalls.com")
	password.send_keys(adobe_password)
	print('keys succesfully sent')
	sign_in = driver.find_element_by_id("login")
	sign_in.click()
	print('you have already logged in')
	manage = driver.find_element_by_xpath("//a[contains(text(), 'Manage')]")
	manage.click()
	pending_count = int(driver.find_element_by_id("1-OUT_FOR_SIGNATURE-count").text)
	print('success')


	docs_list = []
	for i in range(pending_count):
		agreement_name = driver.find_elements_by_xpath("//table[@class = 'agreement-info']//div[@class= 'title']")[i].text
		docs_list.append(agreement_name)
	subject = "PENDIENTES LEASES"	
	body = "Documentos pendientes de firma: " + ", ".join(docs_list)
	msg = f"Subject: {subject}\n\n{body}"
	print('success 2')
	print(msg)	
	with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
		smtp.ehlo()
		smtp.starttls()
		smtp.ehlo()
		gmail_password = str(os.environ.get(EMAIL_PASSWORD))
		smtp.login("board@ibericmalls.com", gmail_password)
		smtp.sendmail("board@ibericmalls.com", "commercial@ibericmalls.com", msg)
		print("Reminder Sent")
    

sched.start()

