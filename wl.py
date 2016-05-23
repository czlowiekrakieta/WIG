import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier as RFC
from sklearn.naive_bayes import GaussianNB as GNB

res = pd.read_csv("wszystko.csv")

#res = df.sort(['Roznica'], axis=0)
res = res.fillna( res.mean() )

lab = list(res[ 'ZKlasa' ])
res.drop( ['Roznica', 'ZKlasa'], axis=1)



n = len(res)


rfc = RFC()
rfc.fit(res[:int(n/2)], lab[:int(n/2)])

pred = rfc.predict( res[int(n/2):] )

print("sprawnosc drzew decyzyjnych: ", np.mean( pred==lab[int(n/2):] ))

gnb = GNB()
gnb.fit( res[:int(n/2)], lab[:int(n/2)] )

pred = gnb.predict( res[int(n/2):] )

print("sprawnosc naiwnego bayes: ",  np.mean( pred==lab[int(n/2):] ) )









