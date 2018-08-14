import requests
from bs4 import BeautifulSoup

def score_dict(names, problems):#Where names is a list containing usernames and problems is a list conatining the code golf problems you want to check
	users = {}
	for prob in problems:
		html=''
		scores={}
		try:
			r = requests.get('https://code-golf.io/scores/' + prob[0] + '/python')
			html = BeautifulSoup(r.text, 'html.parser')
		except:
			print('Error')
	for row in html.find_all('tr'):
		scores[row.td.a.contents[0].children[0]] = row.find_all('td')[2].contents[0].children[0]
	for name in names:
		bad_chars='()'
		try:
			users[name] += int(("".join(c for c in score[name] if c not in bad_chars) - ' points'))
		except:
			pass
	return users