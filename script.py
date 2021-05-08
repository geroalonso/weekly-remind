import requests
import json
from datetime import datetime, timedelta
import csv
import smtplib, ssl
import os
from os import environ
from apscheduler.schedulers.blocking import BlockingScheduler





sched = BlockingScheduler()


@sched.scheduled_job('cron', hour=20)
def timed_job():
	url = "https://rest.tsheets.com/api/v1/timesheets"

	querystring = {
	   "start_date": str(datetime.today()),
	}

	payload = ""
	headers = {
	   'Authorization': "Bearer S.7__6114cfc1a82ed9afc75a0d4785da6b9b4d624a6a",
	  }

	response = requests.request("GET", url, data=payload, headers=headers, params=querystring)


	array  = response.text 



	data  = json.loads(array)
	print(data['results']['timesheets'])
	message = ''
	for key, val in data['results']['timesheets'].items():
		if val['user_id'] == 865293:
			val['user_id'] = 'LUIS ALFONSO RUIZ'
		elif val['user_id'] == 3043477:
			val['user_id'] = 'ALVARO GUINAND'
		elif val['user_id'] == 2993555:
			val['user_id'] = 'CORY SMITH'
		else:
			val['user_id'] == 3045093
			val['user_id'] = 'JAIRO ORTIZ CAMPO'

		inicio = val['start'].split('T')[1].split('-')[0]
		fin = val['end'].split('T')[1].split('-')[0]
		horas_trabajadas = round(val['duration']/3600, 2)

		message =  message + val['user_id'] + ' arrived today at work at  ' + inicio + ' and left at ' + fin + ' having worked for '+ str(horas_trabajadas) + ' hours \n'
		
	print(message)

	port = 465  # For SSL
	smtp_server = "smtp.gmail.com"
	sender_email = "leasingibericmalls@gmail.com"  # Enter your address
	email = 'geronimoalonso@icloud.com'
	password = 'guwHer-zuwsi7-rusres'
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
		server.login(sender_email, password)
		server.sendmail(sender_email, email, message)

	 
	port = 465  # For SSL
	smtp_server = "smtp.gmail.com"
	sender_email = "leasingibericmalls@gmail.com"  # Enter your address
	email = 'admin@ibericmalls.com'
	password = 'guwHer-zuwsi7-rusres'
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
		server.login(sender_email, password)
		server.sendmail(sender_email, email, message)


sched.start()



# from apscheduler.schedulers.blocking import BlockingScheduler
# import time
# import smtplib
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
# from webdriver_manager.chrome import ChromeDriverManager




# sched = BlockingScheduler()
# 'interval', minutes=3
# # @sched.scheduled_job('cron', day_of_week='mon', hour=17)
# @sched.scheduled_job('interval', minutes=3)
# def scheduled_job():
# 	url = "https://buildium.na2.echosign.com/public/login"
# 	driver = webdriver.Chrome(ChromeDriverManager().install()) #set the search engine
# 	driver.implicitly_wait(10) #set implicit wait
# 	driver.get(url) #open the browser
# 	print('driver selected')
# 	adobe_password = ""
# 	print('environment variable created')
# 	login = driver.find_element_by_id("userEmail")
# 	print('element found')
# 	password = driver.find_element_by_id("userPassword")
# 	print('password element found')
# 	login.send_keys("admin@ibericmalls.com")
# 	password.send_keys(adobe_password)
# 	print('keys succesfully sent')
# 	sign_in = driver.find_element_by_id("login")
# 	sign_in.click()
# 	print('you have already logged in')
# 	manage = driver.find_element_by_xpath("//a[contains(text(), 'Manage')]")
# 	manage.click()
# 	pending_count = int(driver.find_element_by_id("1-OUT_FOR_SIGNATURE-count").text)
# 	print('success')


# 	docs_list = []
# 	for i in range(pending_count):
# 		agreement_name = driver.find_elements_by_xpath("//table[@class = 'agreement-info']//div[@class= 'title']")[i].text
# 		docs_list.append(agreement_name)
# 	subject = "PENDIENTES LEASES"	
# 	body = "Documentos pendientes de firma: " + ", ".join(docs_list)
# 	msg = f"Subject: {subject}\n\n{body}"
# 	print('success 2')
# 	print(msg)	
# 	with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
# 		smtp.ehlo()
# 		smtp.starttls()
# 		smtp.ehlo()
# 		gmail_password = ''
# 		smtp.login("board@ibericmalls.com", gmail_password)
# 		smtp.sendmail("board@ibericmalls.com", "commercial@ibericmalls.com", msg)
# 		print("Reminder Sent")
    

# sched.start()

