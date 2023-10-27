
#Extracting emails from text

import re

def extractEmails(text):
#Extracts all valid email addresses from the input text
#Define the email regex pattern
	emailPattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
#Then use re to find all matches of the email pattern in the text
	emailList = re.findall(emailPattern, text)
	return emailList
#Example: 
text = """
John's email is john.doe@gmail.com
Alice's email is alice@example.com
the IT Department can be reached at itdeot@example.org
"""

emails = extractEmails(text)
print("Extracted emails: ")
for email in emails:
	print(email)
