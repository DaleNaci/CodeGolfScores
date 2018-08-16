import requests
from bs4 import BeautifulSoup

class ConnectionError(Exception):
	def __init__(self):
		self.message = 'Connection failed'
		super().__init__(self)


def score_dict(names):#Where names is a list containing usernames
	users = {}
	for name in names:
		html = ''
		try:
			r = requests.get('https://code-golf.io/users/' + name)
			if not r.status_code == 200:
				raise ConnectionError
			html = BeautifulSoup(r.text, 'html.parser')
		except e:
			print(e)
		users[name] = int(html.main.table.tr.td.contents[0])
	return users
