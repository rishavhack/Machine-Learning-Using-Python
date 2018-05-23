
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[3]:


labels=['a','b','c']
my_data=[10,20,30]
arr = np.array(my_data)
d={'a':10,'b':20,'c':30}


# In[8]:


pd.Series(data = my_data)


# In[9]:


pd.Series(data=my_data,index=labels)


# In[10]:


pd.Series(my_data,labels)


# In[11]:


pd.Series(arr)


# In[12]:


pd.Series(arr,labels)


# In[13]:


d


# In[14]:


pd.Series(d)


# In[15]:


pd.Series(data=labels)


# In[17]:


pd.Series(data=[sum,len])


# In[19]:


ser1 = pd.Series([1,2,3,4],["USA",'Germany','India','Nepal'])


# In[20]:


ser1


# In[21]:


ser2  = pd.Series([1,2,5,4],['USA','Germany','Itlay','Japan'])


# In[22]:


ser2


# In[31]:


ser1['India']


# In[28]:


ser3 = pd.Series(data=labels)


# In[29]:


ser3


# In[33]:


ser1+ser2  #integer convert into float

