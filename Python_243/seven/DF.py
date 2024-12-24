import pandas as pd
import numpy as np
import sklearn as skl 


df = pd.DataFrame({
  'columnA' : [10,np.nan,50,100],
  'columnB' : ['A','B','B','A'],
  'columnC' : [True,False, True, True]
}

)

print(df.head())
print(df.shape)
print(df.info())
print(df.columns)
print(df.isnull().sum())

df_dropped =df.dropna()
df_filled = df.fillna(0)
print(df_dropped)
print(df_filled)

df.to_csv("my_csv", index=False)

df.read_csv("my_csv")