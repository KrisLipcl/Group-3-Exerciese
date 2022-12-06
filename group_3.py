# -*- coding: utf-8 -*-
"""Group 3

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Q9wxUFkPkpvFuVQpF8bv6GJpOutzd6BT

#Group 3: Hongen Wen, Peichao Li, Ruihong Sun, Ruizhuo Zhai, Zhe Su

#Code 1: Describtion on the ratings of cigerettes at different price ranges based on the year
"""

import pandas as pd

import row64



def YearlyGroupAve(idf, inDateC, inGroupC, inSumC):

 mName =df.columns[inDateC]

 idf[mName] = pd.to_datetime(idf[mName])

 gName =df.columns[inGroupC]

 cName =df.columns[inSumC]

 idf = idf.groupby([pd.Grouper(key=mName, freq='Y'), gName]).mean()

 idf = idf.reset_index();

 idf[mName] = idf[mName].to_numpy().astype('datetime64[M]')

 idf = pd.pivot_table(idf, index=gName, columns=mName, values=cName).reset_index()

 cList = [idf.columns[0]]

 for i,cName in enumerate(idf.columns):

  if(i>0):

   cList.append(cName.strftime('%m-%d-%Y'))

 idf.columns = cList

 idf = idf.fillna(0)

 idf = idf.round(2)

 return idf



#IMPORT("C:\Users\rdbullar\Desktop\smokerdata.csv")

dfIn = row64.get_dataframe("Dataframe3")

df=dfIn.copy(deep=True)

df=YearlyGroupAve(df,4,11,8)

"""#Code 2: Data cleaning and look for the null"""



import pandas as pd
import row64

def NullSummary(inDf):
 print("------------ NULL Value Summary ------------")
 print(inDf.isnull().sum())

#IMPORT("C:\Users\rdbullar\Desktop\smokerdata.csv")
dfIn = row64.get_dataframe("Dataframe3")
df=dfIn.copy(deep=True)
NullSummary(df)

"""#Code 3: Visualization - word cloud based on the brands"""

import matplotlib.colors as cl

import matplotlib.pyplot as plt

import pandas as pd

import row64



from wordcloud import WordCloud



def MakeWordCloud(inDf, inInd, inWhite):

 colors = ['#014D9A','#016BB5','#4AA0CE','#7ACBDD']

 text = ' '.join( inDf[inDf.columns[inInd]].tolist() )

 cRGB = [cl.to_rgb(col) for col in colors]

 cmap = cl.LinearSegmentedColormap.from_list("", cRGB)

 if(inWhite):

  wCloud = WordCloud(background_color='white',width=1500,height=1000,colormap=cmap).generate(text)

 else:

  wCloud = WordCloud(width=1500,height=1000,colormap=cmap).generate(text)

 plt.imshow(wCloud, interpolation='bilinear')

 plt.axis("off")



#IMPORT("C:\Users\rdbullar\Desktop\smokerdata.csv")

dfIn = row64.get_dataframe("Dataframe3")

df=dfIn.copy(deep=True)

MakeWordCloud(df,1,True)

"""#Code 4: Frequency report

"""

import pandas as pd
import row64
import sidetable

def FreqReport(inDf,inColI):
 cName = inDf.columns[inColI]
 inDf = inDf.stb.freq([cName])
 return inDf

#IMPORT("C:\Users\wenho\Downloads\smokerdata.csv")
dfIn=row64.get_dataframe("Dataframe4")
df=dfIn.copy(deep=True)
df=FreqReport(df,8)

"""#Code 5: Data summary"""

import pandas as pd
import row64

#IMPORT("C:\Users\wenho\Downloads\smokerdata.csv")
dfIn=row64.get_dataframe("Dataframe4")
df=dfIn.copy(deep=True)
df=df.describe(include='all').reset_index()