import numpy
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
#from graphing import graph

df = pd.read_csv(r'CATdata.txt', '\t', skip_blank_lines = True)
df.columns = ['Date', 'Time','Data']
df = df.dropna(how = 'any')
df['new_time'] = pd.to_datetime(df['Time'], format='%H:%M:%S.%f')
#x = df[df['Data'[2:5]] == 'F004']
#df.loc['Data' == 'F004']
#df = pd.DataFrame(df.Data.str.split(' ',1).tolist(),
                                  # columns = ['flips','row'])
#df['Col2'] = df['Data'].str.split('_').str[:1]
#df['Col3'] = df['Data'].str.split(Data[2:5]).str[1]
df['PGNValue'] = df['Data'].str[2:6]
df['SPNLength'] = df['Data'].str[8:]
#df['SPNValue'] = df[df['Data']]
#df['Value'] = df['SPNLength'].str[12:16]

#df[]
enginespeed_df = df[df['PGNValue'] == 'F004']

enginespeed_df['Enginespeed'] = enginespeed_df['SPNLength'].str[8:10] + enginespeed_df['SPNLength'].str[6:8]

enginespeed_df['Enginespeed'] = enginespeed_df.dropna(enginespeed_df['Enginespeed'] <= 'FF', inplace = True)
enginespeed_df['Enginespeed'] = enginespeed_df.dropna(enginespeed_df['Enginespeed'] <= '', inplace = True)
#enginespeed_df['SPNLength'] = df.dropna('SPNLength' < 2 ) 



#enginespeed_df['Actualdata'] = enginespeed_df['Enginespeed'].apply(lambda x:int(x, 16))
#enginespeed_df['Actualdata'] = enginespeed_df['Actualdata'].apply(lambda x: x*0.125)
#enginespeed_df = df[df['SPNValue'] == '00BE']



#enginespeed_df.plot(x='new_time', y='Actualdata') # last 3 columns are invalid values?







#if empty add 0 function (1984 - 1992)

#%%

# opens the test file from CAT and puts each entries into a list
dataFile = open('CATdata.txt', 'r')
dataList = dataFile.readlines()
#print(dataList)
# gets rid of all new line charactes
dataList = [x.strip() for x in dataList]
dataFile.close()

# splits each entry, saved in a list
#This piece of code saves each sensor reading(including time) as a single term in a list. Why it looks so messy
splitList = []
j = 0
dataList = [x.split('\t') for x in dataList]
for item in dataList:
    #j = j+1
    if item == ['']:
        continue
    splitList.append(item)
    #print(j)
#print(len(splitList))
#print(j)

enginespeed = []
i = 0
for data in splitList:
    i=i+1
    #print(i, "data is", data)
    #if data[2][2:6] == 'F004':
	    #print(data)
    #else:
		#enginespeed.append(data)  # this is the line where it stops working!
#print(enginespeed)

#print(enginespeed)
#TEST CODE UNTIL HERE ON SAVNI'S LAPTOP
#print(j)


