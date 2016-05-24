import pandas as pd

df = pd.read_csv("/home/lukasz/Dokumenty/python gieldowy/WIG/adresy.csv")
nazwy = df['Nazwa']
sp = pd.read_csv("/home/lukasz/Dokumenty/python gieldowy/WIG/daneFundPrzeszlosc/" + str(nazwy[0]) + ".csv")
headers = list(sp)
#print( headers )

wszystko = pd.DataFrame(data = {x: [] for x in headers[1:] })
#print( wszystko )
plik = open("crash.txt", "w")

for spolka in nazwy:
	sp = pd.read_csv("/home/lukasz/Dokumenty/python gieldowy/WIG/daneFundPrzeszlosc/" + str(spolka) + ".csv")
	sp.set_index(['Unnamed: 0'])
	klasy = sp['ZKlasa']
	ind = 0

	try:
		while len(klasy) > 0 and klasy[ind] != 0 and klasy[ind] != 1:
			ind += 1
	except:
		plik.write( str(spolka) + '\n' )
		print( spolka )
		print( "cos sie popsulo" )
		pass
	
	sp = sp[headers[1:]][ind:]
	print(str(spolka) + " " +  str(ind) + "\n" )
	wszystko = pd.concat( [ wszystko, sp], axis = 0 )
	

wszystko.to_csv("/home/lukasz/Dokumenty/python gieldowy/WIG/wszystko_przeszlosc.csv")

	
