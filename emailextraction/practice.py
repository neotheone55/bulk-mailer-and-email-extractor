import re
import time
def playAgain():
	again = input("Try again? yes/no: \n")
	again = again.lower()
	if again == "yes":
		return True
	else:
		return False 
def line():
	print("-----------------------------")
def n():
	print("\n")
def extractor():
	try:
		def extractedEmails(url):
			import requests
			response = requests.get(url)
			from bs4 import BeautifulSoup
			soup = BeautifulSoup(response.text, 'html.parser')
			emailRegex = r"[a-zA-Z0-9\.\+-_]+@[a-zA-Z0-9\.\+-_]+\.[a-zA-Z]+"
			emailList = re.findall(emailRegex,str(soup))
			return emailList
		url = input("Enter url link here: \n")
		time.sleep(0.5)
		print("Hold on a second...")
		time.sleep(1)
		emails = extractedEmails(url)
		print("Extracted Emails: \n")
		for key in emails:
			time.sleep(0.5)
			print(key)
			n()
	except Exception as i:
		print("Something went wrong!!")
		time.sleep(0.5)
		print("Here is what went wrong...")
		line()
		print(i)
		line()
extractor()
while playAgain():
	extractor()
