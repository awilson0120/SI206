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
soup = BeautifulSoup(r.text)
for i in soup.find_all(text=True):
	if "student" in i:
		i = i.split(" ")
		for word in i:
			if word == 'students':
				word = "AMAZING students"
for i in soup.find_all("iframe"):
	i['src'] = "https://scontent-ort2-1.xx.fbcdn.net/l/t31.0-8/12961377_1070535396341586_8029777897783604764_o.jpg"

print(soup)





# for line in text:
# 	line = line.rstrip()
# 	if "student" in line:
# 		for word in line.split(" "):
# 			if word == "student":
# 				word == "AMAZING student"
# 			if word == "students":
# 				word = "AMAZING students"
# 		print(line)




# soup(text=re.compile("student"))
# for instance in s:
# 	for word in instance:
# 		if word == "student":
# 			word.replace("student", "AMAZING student")



# Deliverables
# Make sure the new page is uploaded to your GitHub account.
