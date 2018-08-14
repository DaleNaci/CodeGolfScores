import csv, requests
from bs4 import BeautifulSoup

def score_dict(names, problems):#Where names is a list containing usernames and problems is a list conatining the code golf problems you want to check
	users = {}
	for name in names:
		users[name] = 0
	for prob in problems:
		html=''
		scores={}
		try:
			r = requests.get('https://code-golf.io/scores/' + prob + '/python')
      			html = BeautifulSoup(r.text, 'html.parser')
    		except:
      			print('Uwu We made a fucky wucky! A wittle fucko boingo! The code monkeys at our headquarters are working VEWY HARD to fix this!')
		for row in html.find_all('tr'):
      			scores[row.td.a.contents[0].chlidren[0]] = row.find_all('td')[2].contents[0].children[0]
    		for name in names:
      			bad_chars='()'
      		try:
        		users[name] += int(("".join(c for c in score[name] if c not in bad_chars) - ' points'))
      		except:
        		pass
	return users
