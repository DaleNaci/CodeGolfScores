import requests
from bs4 import BeautifulSoup as soup

users = open("example/users.txt", "r").read().split(",")
users.pop(len(users)-1)

points = []

for u in users:
	r = requests.get("https://code-golf.io/users/" + u)
	html = soup(r.text, "html.parser")
	points.append(int(html.table.tr.td.contents[0]))

for i in range(len(points)):
	m = i
	for j in range(i+1, len(points)):
		if points[m] < points[j]:
			m = j
	points[i], points[m] = points[m], points[i]
	users[i], users[m] = users[m], users[i]

for i in range(0, len(points)):
	print(users[i] + ": "),
	print points[i]
