from urllib.request import urlopen
import pandas as pd
import re


def wyciagnijDane(url):
	d = urlopen(url)

	content = str(d.read())

	p = content.split('<table class="biz_table" cellspacing="0">')[1].split('</table')[0].split("<tr")

	u = p[1].split("</th>")
	#print( len(u) )
	kwartaly = {}
	klKwart = []
	for i in range(1,5):
		klKwart.append(u[i].split("<span>")[1].split(" ")[0] )
	
	for item in klKwart:
		kwartaly.setdefault( item, [] )
	
	#print( klKwart )
	#print( kwartaly )
	
	for i in range(2, len(p)):
		z = p[i].split('<td class="right">')
		for j in range(1, len(z)-1):
			u = z[j].split(">")[1].split("</")[0][:-1].replace("\\xa0", "")
			
			if "," in u:
				u = u.replace(",", ".")
			if u[0] == "(":
				u = -float( u.strip("(").strip(")") ) 
			elif u[0] == "-":
				u = "NaN"
			else:
				u = float(u)
			
			kwartaly[ klKwart[j-1] ].append(u)
			
	return klKwart, kwartaly




