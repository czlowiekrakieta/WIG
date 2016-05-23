import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("wszystko.csv")
feature = list(df)


for feat in range(1, len(feature)-1):
	

	z = df[ [feature[feat], 'ZKlasa'] ]
	x_1 = df[ df['ZKlasa']==1 ][ feature[feat] ]
	x_2 = df[ df['ZKlasa']==0 ][ feature[feat] ]
		
	sr_1 = x_1.mean()
	sr_2 = x_2.mean()
	
	x_1 = x_1.fillna(sr_1)
	x_2 = x_2.fillna(sr_2)


	q_1 = np.percentile( x_1, [25, 50, 75] )
	q_2 = np.percentile( x_2, [25, 50, 75] )
	k = 2
	u_1 = x_1[ x_1 > q_1[1] - k*( q_1[2]-q_1[0] ) ]
	u_2 = x_2[ x_2 > q_2[1] - k*( q_2[2]-q_1[0] ) ]
	x_1 = u_1[ u_1 < q_1[1] + k*( q_1[2]-q_1[0] ) ]
	x_2 = u_2[ u_2 < q_2[1] + k*( q_2[2]-q_2[0] ) ]

	
	plt.subplot(211)
	plt.title( str(feature[feat]))
	plt.hist( x_1, bins = 10 )
	plt.subplot(212)
	plt.hist( x_2, bins = 10 )
	plt.show()
	przedzialy_1 = np.linspace( min(x_1), max(x_1), num=10, endpoint=True )
	przedzialy_2 = np.linspace( min(x_2), max(x_2), num=10, endpoint=True )
	ilosc_1 = []
	ilosc_2 = []
	for i in range(len(przedzialy_1)-1):
		u_1 = x_1[ x_1 > przedzialy_1[i] ]
		u_2 = x_2[ x_2 > przedzialy_2[i] ]
		ilosc_1.append( len( u_1[ u_1 < przedzialy_1[i+1] ]  ))
		ilosc_2.append( len( u_2[ u_2 < przedzialy_2[i+1] ]  ))
		

	print( feat )
	print( ilosc_1 )
	print( ilosc_2 )
	print( '\n' )
		
	
