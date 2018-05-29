
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[8]:


d={'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]}


# In[9]:


df = pd.DataFrame(d)


# In[10]:


df


# In[13]:


df.dropna() #axis = 0 perfrom on row


# In[14]:


df.dropna(axis=1) #axis = 1 perfrom on column


# In[15]:


df.dropna(thresh=1) #atleat value 1 in row


# In[16]:


df.dropna(thresh=2) #atleat value 2 in row


# In[18]:


df.fillna(value='Rishav')


# In[20]:


df['A'].fillna(value=df['A'].mean())

