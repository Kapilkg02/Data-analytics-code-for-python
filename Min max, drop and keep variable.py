# importing dataset
import pandas as pd
new_data = pd.read_excel("D:\Car_sales.xlsx", sheet_name="car")
#max and min, sum,std, mean, percent
new_data.columns
sales = new_data.Sales_in_thousands.sum()
sales
new_data.Sales_in_thousands.max()
new_data.Sales_in_thousands.min()

# drop and keep the columns
new_data.columns
drop_data = new_data.drop(["Price_in_thousands", 'Curb_weight', 'Fuel_capacity'],axis =1)
drop_data.columns
#or can be done in this way
drop_data = new_data.drop(columns=["Price_in_thousands", 'Curb_weight', 'Fuel_capacity'])
drop_data.columns

#keep the columns
keep_data = new_data[['Model', 'Sales_in_thousands', '__year_resale_value',   'Vehicle_type', 'Engine_size',]]
keep_data.columns