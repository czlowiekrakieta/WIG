import numpy as np
import pandas as pd

mapa = {}
kwartaly = []
for i in range(1991,2017):
	for j in range(1,5):
		l = str(i) + "Q" + str(j)
		kwartaly.append(l)
		mapa[l] = int(l.replace("Q1", "0331").replace("Q2", "0630").replace("Q3", "0931").replace("Q4", "1231"))


WIG = pd.read_csv("archiwumCSV/WIG.csv")
WIG = WIG.set_index(['Unnamed: 0'])
WIG = WIG[ ['<CLOSE>'] ]


wl = []
df = pd.read_csv("wszystko.csv")
df.set_index(['Unnamed: 0'], inplace=True)

with open("wlasnosci.txt", "r") as f:
	for line in f:
		wl.append( str(line)[:-1] )

wl = wl[:17]
ind = [x for x in range(len(wl))]

sl = {}

for i in range(len(wl)):
	sl[wl[i]] = ind[i]

nazwy = list(pd.read_csv("adresy.csv")["Nazwa"])
plik = open("crash_wskazniki.txt", "w")
for spolka in nazwy:

	print( spolka )
	try:
	
		ceny = pd.read_csv("archiwumCSV/" + str(spolka) + ".csv")
		ceny = ceny.set_index(['Unnamed: 0'] )
		ceny = ceny['<CLOSE>']
		
	
		sp = pd.read_csv("daneFundSkrKlasy/" + spolka + ".csv")
		sp.set_index(['Unnamed: 0'], inplace=True)
		indeks = list(sp.index)


		slownik = {}
	
		slownik["WOZ"] = sp[ str( sl["Zobowiązania i rezerwy na zobowiązania"] ) ]/sp[str(sl["Aktywa razem"])]
		slownik["ZD"] = sp[ str( sl["Zobowiązania długoterminowe"] ) ]/sp[str(sl["Kapitał własny"])]
		slownik["RS"] = sp[ str( sl["Zysk (strata) netto"] ) ]/sp[str(sl["Przychody netto"])]
		slownik["RA"] = sp[ str( sl["Zysk (strata) netto"] ) ]/sp[str(sl["Aktywa razem"])]
		slownik["ZKW"] = sp[ str( sl["Zysk (strata) netto"] ) ]/sp[str(sl["Kapitał własny"])]

		#trzeba przeleciec po wszystkich kwartałach, dla których spółka jest określona i je skorygować, jeśli nie ma w pliku z cenami
		#print( slownik )
		z = []
		liczba_pominiec = 0
		for kwartal in range(len(indeks)):
			delta = 0	
			#print( mapa[ indeks[kwartal] ] )
		
			if mapa[ indeks[kwartal] ] < ceny.index[0]:
				liczba_pominiec += 1
				continue
			while mapa[ indeks[kwartal] ]  - delta not in ceny.index:
				 delta += 1
			#print( mapa[indeks[kwartal]]-delta )
			z.append( mapa[indeks[kwartal]]-delta )

	
		slownik["CZ"] = np.asarray(ceny.loc[z])/( np.asarray(sp[str( sl[ "Zysk (strata) na jedną akcję (zł)"])])[liczba_pominiec:] )
		slownik["CWK"] = np.asarray(ceny.loc[z])/(np.asarray(sp[str( sl[ "Wartość księgowa na jedną akcję (zł)"])])[liczba_pominiec:] )

		
		#print( ceny.loc[z] )
		#print("ZNJA",  sp[str( sl[ "Zysk (strata) na jedną akcję (zł)"])] )
		zapis = pd.DataFrame( index = sp.index[liczba_pominiec:], data = slownik )
		zapis.to_csv("daneWskazniki/" + str(spolka) + ".csv")

	except:
		plik.write( str(spolka) + "\n" )
		continue

plik.close()
	
