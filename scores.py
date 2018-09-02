import requests
from bs4 import BeautifulSoup as soup

class ConnectionError(Exception):
	def __init__(self):
		self.message = 'Connection failed'
		super().__init__(self)

r = requests.get('https://code-golf.io/scores')
if not r.status_code == 200:
	raise ConnectionError

# html = soup(r.text, 'html.parser')


# outer = html.main.table.tr

# print(outer.td.findNext('td').a.contents[0])
# print(outer.td.findNext('td').findNext('td').contents[0])

# print(outer.td.findNext('td').a.contents[0])
# print(outer.td.findNext('td').findNext('td').contents[0])

# for i in range(1):
# 	outer = html.main.table.tr
# 	for j in range(i):
		
html = soup(r.text, 'html.parser')
table = html.findAll("table")[0]
rows = table.findAll('tr')
for tr in rows:
	print(tr.get_text(strip=True))




# OLD

# # USER = ENTIRE "tr" SECTION
# userList = html.find_all("tr")

# print(userList[0].text)
# #print(userList[0].text)

# #for user in userList:
