import pandas as pd


df = pd.read_csv("/home/lukasz/Dokumenty/python gieldowy/WIG/adresy.csv")
nazwy = df['Nazwa']
plik = open("zapisy.txt", "w")
for spolka in nazwy:
	print( spolka )
	sp = pd.read_csv("dane/" + str(spolka) + ".csv")
	sp = sp.set_index(['Unnamed: 0'])
	kol = list( sp )[:17]
	minInd = len( sp[kol[0]] )
	wysokosc = len( sp[kol[0]] )
	wzorzec = str(sp[kol[-1]][0])
	
	for kolumna in kol:
		l = sp[kolumna]
		k = 0
		for wartosc in range(wysokosc):
			if str(l[wartosc]) != wzorzec:
				#print( l[wartosc], wzorzec )
				k = wartosc
				#print( k )
				break
		if k != 0 and k < minInd:
			minInd = k
	try:
		plik.write( str(minInd) + " " +  str(list(sp.index)[minInd]) )
	except:
		pass
	df = sp[kol][minInd:]
	df.to_csv("daneFundSkr/" + str(spolka) + ".csv")
	
		

plik.close()
	
	
	
