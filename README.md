# WIG
ENGLISH VERSION BELOW

POLSKI

repozytorium to zawiera crawlera, którego zadaniem było grzebanie w plikach udostępnianych przez Gazetę Wyborczą i wyciągnięcie stamtąd cennych danych fundamentalnych dotyczących spółek giełdowych. jako twór nowicjusza zawiera ono sporo niedoróbek albo zwyczajnych błędów, których planuję się pozbyć

im dłużej przyglądam się tym skryptom, tym większy bałagan tam znajduję. spowodowane jest to zapewne tym, że po pierwsze, pisząc to byłem ( i w zasadzie wciąż jestem ) nowicjuszem w dziedzine analizy danych, a po drugie, moje połączenie internetowe lubi się zrywać ot tak, bez powodu, zatem chciałem jak najszybciej mieć pliki na dysku, żeby móc nad nimi pracować.

Kolejność skryptów:
- parseraport.py wyciąga dane z zadanego adresu - jest napisany pod formatowanie użyte przez Gazetę Wyborczą
- spolka.py używa wyżej wymienionego skryptu, aby skomasować dane do ramki danych z biblioteki pandas i umieścić je w pliku CSV, po jednym na każdą spółkę
- konwersja.py umieszcza notowania archiwalne w plikach CSV
- ekstrakcja.py skraca pliki CSV - spolka.py byla tak skonstruowana, że każdy plik CSV zaczynał się od roku 1991. był to oczywisty absurd, któremu trzeba było zaradzić
- klasowanie.py sprawdza, czy po trzech miesiącach od dnia, którego dotyczą dane, spółka przebiła rynek, czy też nie
- jedenplik_przeszlosc.py umieszcza dane, razem ze zmianą względem wartości zaobserwowanej trzy miesiące wcześniej, w jednym dużym pliku wielkości 19 tysięcy wierszy
- wskazniki.py wyciaga dane fundamentalne i liczy wartości głównych wskaźników finansowych: C/Z, C/WK, zwrot na aktywach, zwrot na sprzedaży, wskaźnik ogólnego zadłużenia, zadłużenie długoterminowe, zwrot z kapitału własnego


Notatki:
- wrzucić wszystkie skrypty do jednego pliku
- przeprowadzić bardziej zaawansowaną analizę eksploracyjną danych
- stworzyć więcej własności*
- zrobić coś z faktem, że ruchy akcji nie zawierają informacji o splitach
- przetłumaczyć skrypty na angielski
- brakuje sporo notowań, znaleźć dokładniejsze źródło
- banki mają kilka dodatkowych własności dotyczących ich powiązań z Bankiem Centralnym. w związku z tym "spolka.py" wysypywała się, próbując zebrać ich dane do pliku. odłożyłem naprawienie tego problemu na później.

*podstawowa analiza danych pokazała, że niestety histogramy własności niewiele się różnią dla spółek przebijających rynek i tych, którym się to zadanie nie powiodło. może trzeba pogrzebać wśród wskaźników znanych w świecie finansów i na tej podstawie stworzyć jakieś własności.


ENGLISH 


crawler I created some time ago in order to extract fundamental data about Warsaw Stock Exchange - there's a lot of room for improvement, though. 

now that I look through scripts, there's huge mess down there. I am still learning, so I was coding very carefully, step by step, script by script, anxious not to screw everything up - sometimes at the cost of later readability. Also, I have terrible Internet connection, prone to breaking for no apparent reason, so I was greedy to download everything I can and then, iteratively, polish my precious data.

Order of scripts:
- parseraport.py contains script that extracts data from given url, crafted for formatting wyborcza.pl uses
- spolka.py uses above script to extract fundamental data about companies and put them into CSV files, one per company
- konwersja.py turns stock movements data into CSV file
- ekstrakcja.py truncates data - until now, every single file started from 1991 year, even if company wasn't founded yet, let alone listed on stock market
- klasowanie.py calculates whether company outperformed or underperformed market in three months time from now
- jedenplik_przeszlosc.py gathers all the fundamental data, along with their relative change to value observed three months earlier, in one single, 19k row csv file

Notes to self:
- bind all scripts to one single file
- perform more sophisticated analysis of dataset
- create more features*
- do something about splits - find adjusted data or get rid of them on your own
- translate scripts to english
- there's a lot of missing data of stock movement, got to find better source of them
- since banks have few additional features, ordinary script crashed when tried to parse data from pages pertaining to them. fix it and gather bank data. 



*basic exploratory analysis has shown that histograms of features from 0-class and 1-class aren't very different, which is very sad conclusion. maybe I got to delve more into company's past, or use indicator very well known in finance world
