import numpy as np
import pandas as pd

WIG = pd.read_csv("archiwumCSV/WIG.csv")
WIG = WIG.set_index(['Unnamed: 0'])
WIG = WIG['<CLOSE>']


df = pd.read_csv("/home/lukasz/Dokumenty/python gieldowy/WIG/adresy.csv")
nazwy = df['Nazwa']

mapa = {}
kwartaly = []
for i in range(1991,2017):
	for j in range(1,5):
		l = str(i) + "Q" + str(j)
		kwartaly.append(l)
		mapa[l] = int(l.replace("Q1", "0331").replace("Q2", "0630").replace("Q3", "0931").replace("Q4", "1231"))

ostatnie = []

slownik_kwartalny = []
slownik_kwartalny_przyszlosc = []

for ind in range(1,len(kwartaly[1:-3])):
	delta = 0
	kw = kwartaly[ind]
	while mapa[kw] - delta not in WIG.index:
		delta += 1

	slownik_kwartalny.append(mapa[kw]-delta)
	delta = 0
	kw = kwartaly[ind+1]
	while mapa[kw] - delta not in WIG.index:
		delta +=1
	slownik_kwartalny_przyszlosc.append(mapa[kw] - delta)

plik = open("crash_klasowanie_po_wskaznikach.txt", "w")

for sp in nazwy:
	try:
		df = pd.read_csv("daneWskazniki/" + str(sp) + ".csv")
	except:
		continue
	df.set_index(["Unnamed: 0"], inplace=True)
	daty = list(df.index )
	z = len(df)
	if z > 0:
		try:
			ind = kwartaly.index( daty[0] ) #jesli wiemy, jaki ma indeks w kwartaly, to wiemy, jak mi indeks w slownikach - mianowicie ind - 1 dla obu
			ceny = pd.read_csv("archiwumCSV/" + str(sp) + ".csv")
			ceny = ceny.set_index(['Unnamed: 0'] )
			ceny = ceny['<CLOSE>']
		
			#trzeba sprawdzic, kiedy zaczyna sie indeksowanie spolki, pozniej przekonwertowac to na date dzienna, a nastepnie wziac ceny od tego miejsca az to ostatniego. mozna to zrobic za pomoca funkcji .index - sprawdzic, jaki indeks w slowniku ma odpowiadajaca kwartalowi data dzienna, pozniej przeskoczyc o z miejsca dalej i sciagnac ceny korzystajac z wlasnosci tablicy numpy. 
			print( sp )
			przyrost_spolki = (np.asarray(ceny.loc[ slownik_kwartalny_przyszlosc[ind-1:ind-1+z] ]) - np.asarray(ceny.loc[ slownik_kwartalny[ind-1:ind-1+z] ]))/np.asarray(ceny.loc[ slownik_kwartalny[ind-1:ind-1+z] ])
			przyrost_wigu = (np.asarray(WIG.loc[ slownik_kwartalny_przyszlosc[ind-1:ind-1+z] ]) - np.asarray(WIG.loc[ slownik_kwartalny[ind-1:ind-1+z] ]))/np.asarray(WIG.loc[ slownik_kwartalny[ind-1:ind-1+z] ])
			klasy = np.ones( przyrost_spolki.shape )*( przyrost_spolki > przyrost_wigu )
			df_prim = pd.DataFrame( index = daty, data = {"ZKlasy": klasy} )
			df = pd.concat( [df, df_prim], axis=1 )
		
			df.to_csv("daneWskazniki/" + str(sp) + ".csv")
		except:
			plik.write( str(sp) + "\n")
			print("cos nie tak")

plik.close()



	
