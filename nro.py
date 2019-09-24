# inspiration for webscraping from 
# https://towardsdatascience.com/web-scraping-using-selenium-and-beautifulsoup-99195cd70a58

import requests, urllib.request, time, webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup

def stitch_department(fragments):
	department_name = fragments[0]
	for i in range(1, len(fragments)):
		if not fragments[i][0].isalpha():
			return department_name, fragments[i:]
		elif fragments[i] == 'All':
			return department_name, fragments[i]
		else:
			department_name += ' ' + fragments[i]
	return department_name, []

department_names = {}

dep_csv = open('dartmouth_departments_csv.txt', 'r')

# build dictionary of department names to department codes/abbreviations
csv_line = dep_csv.readline()
while csv_line:
	tokens = csv_line.strip().split(',')
	department_names[tokens[1]] = tokens[0]
	csv_line = dep_csv.readline()

# retrieve data from the site
nro_url = 'https://www.dartmouth.edu/~reg/201909_nro.html'
response = requests.get(nro_url)

# turn site data into parseable object
nro_soup = BeautifulSoup(response.text, 'html.parser')

# get the text of the div that contains information we want
lines = list(nro_soup.find('div', class_ = 'b6').stripped_strings)

# always introduces the nro out of bounds lists
NRO_INTRO_TEXT = 'NON-RECORDING OPTION OUT-OF-BOUNDS'

intro_index = lines.index(NRO_INTRO_TEXT)

# start second line after intro text 
# (there is always a line about courses abroad)
nro_oob_classes = {}
for line in lines[intro_index + 2:]:
	line = line.strip().replace(':', '').replace(',','')
	fragments = line.split()
	department, classes = stitch_department(fragments)
	nro_oob_classes[department] = classes

timetable_url = 'https://oracle-www.dartmouth.edu/dart/groucho/timetable.main'
driver = webdriver.Chrome(executable_path='/Users/briantomasco/Desktop/CS/CS98/hackathing1/chromedriver')
driver.get(timetable_url)
driver.implicitly_wait(100)

# click through to get to table of courses
# source: https://stackoverflow.com/questions/34396515/how-to-find-a-radio-button-element-by-value-using-selenium
driver.find_element_by_xpath('//input[@name="searchtype" and @value="Subject Area(s)"]').click()
driver.find_element_by_id('term1').click()
driver.find_element_by_id('allsubjects').click()
driver.find_element_by_xpath('//input[@type="submit" and @value="Search for Courses"]').click()

# parse the course table
# help found here: https://stackoverflow.com/questions/23377533/python-beautifulsoup-parsing-table
course_soup = BeautifulSoup(driver.page_source, 'html.parser')
course_table_div = course_soup.find('div', {'class': 'data-table'})
course_table = course_table_div.find('table')
course_table_body = course_table.find('tbody')

# get the individual rows
course_table_rows = list(course_table_body.find_all('tr'))
header_indices = {}
headers = list(course_table_rows[0].find_all('th'))
for i in range(0, len(headers)):
	header = headers[i].text.strip()
	header_indices[header] = i

# hold sum of all class enrollees
student_classes = 0
# hold sum of all class enrollees in oob classes
student_classes_oob = 0

for row in course_table_rows[1:]:
	cols = row.find_all('td')
	cols = [ele.text.strip() for ele in cols]
	enrollees = int(cols[header_indices['Enrl']])
	student_classes += enrollees
	subject_code = cols[header_indices['Subj']]
	if subject_code not in department_names:
		continue
	class_department = department_names[subject_code]
	class_number = cols[header_indices['Num']]
	if class_department not in nro_oob_classes:
		continue
	department_oob = nro_oob_classes[class_department]
	if nro_oob_classes[class_department] == 'All' or class_number in nro_oob_classes[class_department]:
		student_classes_oob += enrollees

print(float(student_classes_oob)/float(student_classes))



