from urllib.request import urlopen
import pandas as pd
from parseraport import wyciagnijDane


strona = "http://wyborcza.biz"
indeksy = []
for i in range(1991, 2015):
	for j in range(1,5):
		l = str(i)
		l += "Q" + str(j)
		indeksy.append(l)

f = open("wlasnosci.txt", "r")
wlasnosci = []
for linia in f:
	wlasnosci.append(linia[:-1])

sp = pd.read_csv("adresy.csv")
adresy = sp['Adres']
nazwy = sp['Nazwa']
print(adresy[0])
ilosc = len(adresy)

koncowki = []
wyjatki = []


def stworzCsv(nr_spolki=0):
	

	for nrSpolki in range(0, 56):
		df = pd.DataFrame(index = indeksy, columns=(x for x in range(len(wlasnosci))))
		dod = adresy[nrSpolki][1:-1].replace(".", ",Q,skons,,1.")
		page = strona + dod
		ind = 1
		print(page)
		d = str(urlopen(page).read())
		while len(d.split("&laquo;"))>1:

			kw, dane = wyciagnijDane(page)
			for kwartal in kw:
				try:
					df.loc[kwartal] = dane[kwartal]
				except:
					#wyjatki.append(nrSpolki, ind)
					print("zlapalem wyjatek")
			
			s = str(ind)
			s1 = str(ind+1)
			page = page.replace( "Q,skons,,"+s, "Q,skons,,"+s1 )
			try:
				d = str(urlopen(page).read())
			except:
				print("powtarzam sciaganie")
				try:
					d = str(urlopen(page).read())
				except Exception as error:
					#plik.close()
					print(str(error))
					break
			print( page )
			ind += 1
		#koncowki.append(ind)
		
		df.to_csv("/home/lukasz/Dokumenty/python gieldowy/WIG/dane/" + str(nazwy[nrSpolki])+".csv")
	return

stworzCsv()


