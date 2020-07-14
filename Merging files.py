#mergin in pandas
df1 = pd.read_excel("D:\Python Video\Test 2.xlsx", sheet_name = "Sheet1")
df2 = pd.read_excel("D:\Python Video\Test 2.xlsx", sheet_name = "Sheet2")
df3 = pd.read_excel("D:\Python Video\Test 2.xlsx", sheet_name = "Sheet3")

#merging dataset
df0 = pd.merge(df1,df2,how="left",on = 'customer_id')
df0
df_left = pd.merge(df2,df3, how = "left" , on ='customer_id')
df_right = pd.merge(df2,df3, how = "right" , on ='customer_id')
df_outer = pd.merge(df2,df3, how = "outer" , on ='customer_id')
df_inner = pd.merge(df2,df3, how = "inner" , on ='customer_id')
df_inner

#appending the datasets
df_right.dtypes
df_all = pd.concat([df_left,df_right]) # appending row of dataset
df_all

df_all2 = pd.concat([df1,df2], axis =1) # appending columns of dataset
df_all2