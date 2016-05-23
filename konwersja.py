import pandas as pd

df = pd.read_csv("adresy.csv")
nazwy = df['Nazwa']
nazwy.append('WIG')
bledy = []
for i in nazwy:
	try:
		plik = open("archiwum/" + str(i) + ".mst", "r")
		linia = plik.readline()
		d = linia.split(",")[1:]
		d[-1] = d[-1][:-1]
		print( d )
		slown = {}
		for item in d:
			slown.setdefault(item, [] )
			
		#print( slown )
		#print(d)
		for line in plik:
			linia = line[:-1].split(",")[1:]
			for j in range(len(d)):
				slown[d[j]].append(linia[j])
	except:
		bledy.append(i)
	
	#print(d[-1], slown[d[-1]])
	dane = pd.DataFrame(index = slown[d[0]], data = {d[j]: slown[d[j]] for j in range(1,len(d))})
	dane.to_csv("archiwumCSV/" + str(i) + ".csv")

print(bledy)
	

