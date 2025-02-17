#!/usr/bin/env python
# coding: utf-8

# # Week 6 Assignment - Pandas
# 

# In[1]:


import pandas as pd
import numpy as np


# ### 1) Load the data into a pandas dataframe (you may get a warning, you can get rid of it by setting low_memory=False). 
# 
# ### Print the first 10 rows and print a random sampling of the rows in the dataframe.

# In[12]:


#Load CSV File Into Dataframe
df = pd.read_csv("data/realtor-data.csv", low_memory=False)

#Print First 10 Rows
print(df.head(10))

#Print Random Sample of Rows
print(df.sample(n=5))


# ### 2) You should always check how many null values there are in your data as well as the data types of the data you're working with. Often you will come across data that looks correct but isn't the right data type. 
# 
# ### Check the number of null values for every column and check the data types as well

# In[3]:


#Check and Print For Null Values
null_counts = df.isnull().sum()
print("Null Counts:")
print(null_counts[null_counts > 0])

#Check and Print Data Types
data_types = df.dtypes
data_type_counts = df.dtypes.value_counts()
print("Data Type Counts:")
print(data_type_counts)


# ### 3) We have 3 columns that looked right when checking the data but aren't the right data type and we'll correct it. 
# 
# ### Cast the columns bed, bath and price to float. Values that cannot be casted to float, like "hello" should be turned into NaN. 
# 
# ### Check the data types again to make sure the conversion was successfull.
# 
# 
# 
# ### Get a count of the number of NaNs in bed, bath and price columns. 
# 
# ### You should get 216535, 194215 and 110 respectively
# 
# 

# In[4]:


#Cast Bed, Bath, and Price to Floats - Or As NaN
df['bed'] = pd.to_numeric(df['bed'], errors='coerce')
df['bath'] = pd.to_numeric(df['bath'], errors='coerce')
df['price'] = pd.to_numeric(df['price'], errors='coerce')

#Check and Print Data Types Again
print("New Data Types:")
print(df[['bed', 'bath', 'price']].dtypes)

#Count and Print NaNs in Bed, Bath, and Price
nan_counts = df[['bed', 'bath', 'price']].isnull().sum()
print("NaN Counts:")
print(nan_counts)


# ### 4) Check the number of unique values in the bed, bath and state columns. 
# 
# ### You should get 49, 42 and 19 respectively
# 
# ### Print the uniques values for bed, bath and state. What do you notice about the unique values ?

# In[5]:


#Check and Print the Number of Unique Values in Bed, Bath, and State
unique_counts = df[['bed', 'bath', 'state']].nunique()
print("Unique values:")

print(unique_counts)
print("\nUnique values in 'Bedrooms':", df['bed'].unique())
print("\nUnique values in 'Bathrooms':", df['bath'].unique())
print("\nUnique values in 'States':", df['state'].unique())

#What do you notice about the unique values?



# ### 5) We want to see which state has the largest number of properties for sale. 
# 
# ### Print a count of the number of properties in each state/territory. 
# 
# ### We want to make sure that we're getting unique listings, so drop any duplicate rows and print the count of the number of properties. What do you notice about the number of properties in each state ?

# In[6]:


#Drop Duplicate Rows for Unique Listings
df_unique = df.drop_duplicates()

#Count and Print of Number of Properties in Each State/Territory
state_counts = df_unique['state'].value_counts()
print("Number of Properties in Each State/Territory:")
print(state_counts)


# ### 6) We now want to look for patterns in our data, find the 5 dates when the most houses were sold. What do you notice ?

# In[ ]:


#Sanitize Date Sold Column Data
df['prev_sold_date'] = pd.to_datetime(df['prev_sold_date'], errors='coerce')

#Count Sales By Date and Find Top 5 Dates
sales_by_date = df_unique['prev_sold_date'].value_counts()
top_5_dates = sales_by_date.head(5)
print("Top 5 Dates For Mosy Houses Sold:")
print(top_5_dates)

#What do you notice?


# ### 7) Now we want to create a simple but effective summary of the properties that are for sale. 
# 
# ### Let's create a summary table that contains the average home size and price, every state and each city within a state. 
# 
# 

# In[10]:


#Sanitize the Data for Price and Home Size
df['price'] = pd.to_numeric(df['price'], errors='coerce')
df['home_size'] = pd.to_numeric(df['house_size'], errors='coerce')

#Summary of Properties For Sale
summary_table = df_unique.groupby(['state', 'city']).agg(
    avg_home_size=('house_size', 'mean'),
    avg_price=('price', 'mean')
).reset_index()

#Printed Table
summary_table


#Your output should be this:
# 		                          house_size	price
# state	            city		
# Connecticut	    Andover	     1653.750000	2.539500e+05
#                   Ansonia	     1848.172414	2.917902e+05
#                   Ashford	     1638.888889	1.959045e+05
#                   Avon	     2929.878788	5.824611e+05
#                   Barkhamsted	 2703.538462	3.383238e+05
# ...	...	...	...
# Virgin Islands	Saint Thomas 3435.025641	1.185128e+06
# Virginia	        Cape Charles	     NaN	7.130000e+05
#                   Chincoteague	     NaN	1.620000e+05
# West Virginia	    Wyoming	     1860.000000	6.250000e+04
# Wyoming	        Cody	     1935.000000	5.350000e+05

