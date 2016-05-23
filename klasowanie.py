import pandas as pd

df = pd.read_csv("/home/lukasz/Dokumenty/python gieldowy/WIG/adresy.csv")
nazwy = df['Nazwa']

mapa = {}
kwartaly = []
for i in range(1991,2017):
	for j in range(1,5):
		l = str(i) + "Q" + str(j)
		kwartaly.append(l)
		mapa[l] = int(l.replace("Q1", "0331").replace("Q2", "0630").replace("Q3", "0931").replace("Q4", "1231"))

	
#print( mapa, mapaInv )
WIG = pd.read_csv("archiwumCSV/WIG.csv")
WIG = WIG.set_index(['Unnamed: 0'])
WIG = WIG[ ['<CLOSE>'] ]


for spolka in nazwy:
	print( spolka )
	plik = open("roznice/roznica_" + str(spolka) + ".txt", "w")
	sp = pd.read_csv("daneFundSkr/" + str(spolka) + ".csv")
	sp = sp.set_index(['Unnamed: 0'] )
	indeks = list( sp.index )
	if len(indeks)>0 and indeks[-1][-4:] == "null":
		while "null" in indeks[-1]:
			del indeks[-1]
		sp = sp[list(sp)][indeks[0]:indeks[-1]]
		#print( sp )
	ceny = pd.read_csv("archiwumCSV/" + str(spolka) + ".csv")
	ceny = ceny.set_index(['Unnamed: 0'] )
	ceny = ceny[ ['<CLOSE>', '<VOL>'] ]
	nowosci = {'Roznica': [], 'ZKlasa': [], 'Wolumen': []}
	
	cenaStart = list(ceny.index)[0]
	u = str(cenaStart)[:4] + "Q" + str( int( int(str(cenaStart)[4:6]) - 1 )//3 + 1   )
	if len(indeks) > 0 and u > indeks[0]:
		while len(indeks)>0 and indeks[0] < u:
			del indeks[0]

	for kwartal in range(len(indeks)):
		delta = 0
		try:
			gdzieKw = kwartaly.index( indeks[kwartal] )
		except:
			sp = sp[list(sp)][indeks[0]:indeks[kwartal]]
			indeks = indeks[0:kwartal]
			break
		#print( mapa[kwartaly[gdzieKw]] )
		#print( ceny.index )
		while mapa[kwartaly[gdzieKw]] - delta not in ceny.index:
			delta += 1
		spolkaTeraz = ceny['<CLOSE>'].loc[ mapa[kwartaly[gdzieKw]] - delta ]
		WIGTeraz = WIG['<CLOSE>'].loc[ mapa[kwartaly[gdzieKw]] - delta ]
		nowosci['Wolumen'].append( ceny['<VOL>'].loc[ mapa[kwartaly[gdzieKw]] - delta ]/float(1000) )
		
		delta = 0
		while mapa[kwartaly[gdzieKw+1]] - delta not in ceny.index:
			delta += 1
		spolkaPrz = ceny['<CLOSE>'].loc[ mapa[kwartaly[gdzieKw+1]] - delta ]
		WIGPrz = WIG['<CLOSE>'].loc[ mapa[kwartaly[gdzieKw+1]] - delta ]
		dA = (spolkaPrz - spolkaTeraz)/spolkaTeraz*100
		dW = (WIGPrz - WIGTeraz)/WIGTeraz*100
		nowosci['Roznica'].append( dA - dW )
		if dA > dW:
			nowosci['ZKlasa'].append(1)
		else:
			nowosci['ZKlasa'].append(0)
		
		plik.write( str( dA - dW ) + '\n')
	
	plik.close()
	df = pd.DataFrame( index = indeks, data = nowosci )
	sp = pd.concat( [sp, df], axis = 1 )
	sp.to_csv("daneFundSkrKlasy/" + str(spolka) + ".csv")
	#print( nowosci )
	
			
			 
	

