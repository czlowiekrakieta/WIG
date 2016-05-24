# WIG
crawler I created some time ago in order to extract fundamental data about Warsaw Stock Exchange - a lot of room for improvement, though. naive usage of Random Forest returned accuracy of 99%, but I have yet to find what I missed...

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
- make more features - every vector should contain something about company's past, relative change of every financial indicator at the very least
- do something about splits - find adjusted data or get rid of them on your own
- translate scripts to english
- there's a lot of missing data of stock movement, got to find better source of them
- since bank have few additional features, ordinary script crashed when tried to parse data from pages pertaining to them. fix it and gather bank data. 
