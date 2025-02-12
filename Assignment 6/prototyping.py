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

# In[ ]:


#your code here



# ### 2) You should always check how many null values there are in your data as well as the data types of the data you're working with. Often you will come across data that looks correct but isn't the right data type. 
# 
# ### Check the number of null values for every column and check the data types as well

# In[ ]:


#your code here


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

# In[ ]:


#your code here


# ### 4) Check the number of unique values in the bed, bath and state columns. 
# 
# ### You should get 49, 42 and 19 respectively
# 
# ### Print the uniques values for bed, bath and state. What do you notice about the unique values ?

# In[ ]:


#your code here


# ### 5) We want to see which state has the largest number of properties for sale. 
# 
# ### Print a count of the number of properties in each state/territory. 
# 
# ### We want to make sure that we're getting unique listings, so drop any duplicate rows and print the count of the number of properties. What do you notice about the number of properties in each state ?

# In[ ]:


#your code here


# ### 6) We now want to look for patterns in our data, find the 5 dates when the most houses were sold. What do you notice ?

# In[ ]:


#your code here


# ### 7) Now we want to create a simple but effective summary of the properties that are for sale. 
# 
# ### Let's create a summary table that contains the average home size and price, every state and each city within a state. 
# 
# 

# In[ ]:


#your code here









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


# In[ ]:





# In[ ]:




