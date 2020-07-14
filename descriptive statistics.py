import pandas as pd
new_data = pd.read_excel("D:\Car_sales.xlsx", sheet_name="car")

#proc means like function
new_data.describe()
# new_data.Sales_in_thousands.describe()
# new_data.Price_in_thousands.describe()
# or
new_data[["Price_in_thousands"]].describe()
new_data[["Sales_in_thousands","Price_in_thousands"]].describe()

new_data[["Price_in_thousands"]].describe()
# check the difference
new_data["Price_in_thousands"].describe()