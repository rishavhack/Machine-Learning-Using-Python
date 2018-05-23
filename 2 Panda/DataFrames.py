
# coding: utf-8

# In[1]:


import numpy as np


# In[3]:


import pandas as pd


# In[4]:


from numpy.random import randn


# In[5]:


np.random.seed(101)


# In[6]:


df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])


# In[8]:


df


# In[11]:


df['W']


# In[12]:


type(df['W'])


# In[13]:


df.W


# In[15]:


df[['W','Z']]


# In[16]:


df['new'] = df['W']+df['Y']


# In[17]:


df


# In[21]:


df.drop('new',axis=1)


# In[25]:


df.drop('new',axis=1,inplace=True) #it dleted the new


# In[26]:


df


# In[27]:


df.drop('E')


# In[29]:


df.drop('E',axis=0)


# In[30]:


df.shape


# In[31]:


df[['Z','X']]


# In[33]:


df.loc['A']


# In[37]:


df.iloc[0] #index of row A


# In[38]:


df.loc['B','Y']


# In[39]:


df.iloc[0,3]


# In[40]:


df.loc[['A','B'],['W','Y']]

