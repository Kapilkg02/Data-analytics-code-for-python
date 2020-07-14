import pandas as pd
new_data = pd.read_excel("D:\Car_sales.xlsx", sheet_name="car")

#finding the missing cell in varibales
new_data.Price_in_thousands.isnull()
new_data.Price_in_thousands.isnull().sum()
new_data.isnull().sum()

#filling null=missing values with 0 , mean or anything
newone1 = new_data
a = new_data.Price_in_thousands.mean() #replacing with mean
newone1.Price_in_thousands.fillna(a,inplace=True)
#or
newone1.__year_resale_value.fillna(newone1.__year_resale_value.mean(),inplace =True) # overwriting same dataset;
newone1.isnull().sum()

# using dictionary for  filling nan value
n1 = pd.read_excel("D:\Python Video\datasets_3483_5614_Car_sales.xlsx" , sheet_name ="sale" )
# using dictionary for  filling nan value
a = {"Model": "No idea","Sales_in_thousands": 0, "date": "2002-08-05","Engine_size": 0.1 }
n2 = n1.fillna(a)
n2

# carry forward previous ccell value or next ccell value where Nan is there
n4 = n1.fillna(method = "ffill") # previous cell value paste inplace nan
n4 = n1.fillna(method = "bfill") # next cel value paste in place of nan
n4