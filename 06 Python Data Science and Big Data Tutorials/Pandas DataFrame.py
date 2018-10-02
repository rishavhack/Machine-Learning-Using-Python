
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


df = pd.DataFrame()


# In[4]:


print df


# In[5]:


df1 = pd.DataFrame([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]])


# In[6]:


df1


# In[7]:


df1.head()


# In[8]:


df1.to_csv('export.csv')


# In[9]:


df1.head(2)


# In[10]:


df1.tail(2)


# In[11]:


df1.shape


# In[12]:


df1.iloc[0,1]


# In[13]:


df1.iloc[0:2,0:3]


# In[14]:


df1


# In[15]:


df1 = pd.DataFrame([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]],columns=['A','B','C','D'])


# In[16]:


df1


# In[17]:


dff = pd.read_csv('data.csv')


# In[18]:


dff.head()


# In[19]:


dff['SYMBOL'].dtype


# In[20]:


dff[' PREV_CLOSE'].dtype


# In[21]:


print(dff[' SERIES'].astype('category'))


# In[23]:


df1.to_csv('exportIndexFalse.csv',index=False)


# In[25]:


df1 = pd.DataFrame([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]],columns=['A','B','C','D'])


# In[26]:


df1


# In[27]:


df2 = pd.DataFrame([[11,12,13,14],[15,16,17,18],[19,20,21,22],[23,24,25,26],[27,28,29,30]],columns=['W','X','Y','Z'])


# In[28]:


df2


# In[34]:


df3 = pd.merge(df1,df2,right_on="X",left_on="D")


# In[35]:


df3

