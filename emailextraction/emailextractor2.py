import re

def extractEmail(url):
#initiate requests object to access website data
	import requests
	response = requests.get(url)
#initiate BeautifulSoup object to parse the data
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(response.text,'html.parser')
#Define regext from extracting email addresses
	emailRegex = r"[a-zA-Z0-9\.\_+-]+@[a-zA-Z0-9\.\-+_]+\.[a-zA-Z]+"
#use the regex to find matches in the text
	emails = re.findall(emailRegex,str(soup))
#return list of email addresses
	return emails
#Example usage

url = input("input url here: \n")

emails = extractEmail(url)
print(emails)
