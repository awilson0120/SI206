# Use https://www.si.umich.edu/programs/bachelor-science-
# information/bsi-admissions as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

from bs4 import BeautifulSoup
import requests
import re

base_url = "https://www.si.umich.edu/programs/bachelor-science-information/bsi-admissions"
r = requests.get(base_url)
soup = BeautifulSoup(r.text, 'lxml')
for text in soup.findAll(text=re.compile("student")):
	fixed_text = text.replace("students", "AMAZING students")
	fixed_text = text.replace("student", "AMAZING student")
	text.replaceWith(fixed_text)
for i in soup.find_all("iframe"):
	i['src'] = "https://scontent-ort2-1.xx.fbcdn.net/v/t1.0-9/12246781_982246411837152_7095256904851592848_n.jpg?oh=76c994a6d1759a95fa6324be27010b8c&oe=588EF7E5"
for i in soup.find_all('img'):
	i['src'] = "media/logo.png"

f= open('index.html', 'w')
f.write(soup.prettify())

# Deliverables
# Make sure the new page is uploaded to your GitHub account.
