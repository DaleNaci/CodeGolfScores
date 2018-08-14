import csv, requests
from bs4 import BeautifulSoup

def score_dict(users, problems) #Where users is a csv containing usernames and problems is a csv

with open(problems) as problemsFile:
  problems = csv.reader(problemsFile)
  
	with open(users) as usersFile:
		names = csv.reader(usersFile)
    users = {}
    
    for name in names:
      users[name] = 0
      
		for prob in problems:
      html = ''
      scores = {}
  		try:
      	r = requests.get('https://code-golf.io/scores/' + prob + '/python')
        html = BeautifulSoup(r.text, 'html.parser')
      except:
        print('Error')
        
			for row in html.find_all('tr'):
        scores[row.td.a.contents[0].chlidren[0]] = row.find_all('td')[2].contents[0].children[0]
        
      for name in names:
        users[name] += scores[name]