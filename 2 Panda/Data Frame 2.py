
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[4]:


from numpy.random import randn


# In[5]:


df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])


# In[6]:


df


# In[7]:


df > 0 #conditional


# In[8]:


booldf = df>0


# In[9]:


booldf


# In[10]:


df[booldf]


# In[11]:


df[df>0]


# In[12]:


df


# In[13]:


df['W']>0


# In[15]:


df['W']


# In[16]:


df[df['W']>0]


# In[17]:


df[df['Z']<0]


# In[18]:


df


# In[21]:


result = df[df['W']<0]


# In[22]:


result


# In[28]:


df[df['W']>0][['X','W']]


# In[41]:


boolser = df['W']<0
result = df[boolser]
my_col = ['X','Y']
result[my_col]    #Same as df[df['W']>0][['X','W']]


# In[42]:


df[(df['W']>0)  & (df['Y']>1)]  #Use and here create error


# In[43]:


df[(df['W']<0) | (df['Y']>1)]   #use or create error


# In[44]:


df


# In[45]:


df.reset_index()#if we want change into df the in bracket we have to write inplace=True


# In[48]:


newInd = 'CA NY WY OR CO'.split()


# In[49]:


df['Stated'] = newInd


# In[50]:


df


# In[52]:


df.set_index('Stated')


# In[53]:


df

