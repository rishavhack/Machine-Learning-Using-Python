
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[3]:


data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
        'Person':['Sam','Charlie','Amy','VAnessa','Carl','Sarah'],
        'Sales':[200,120,340,124,243,350]
       }


# In[4]:


df = pd.DataFrame(data)


# In[5]:


df


# In[9]:


byComp = df.groupby('Company')


# In[10]:


byComp


# In[11]:


byComp.mean()  #Automatically ignore non number column


# In[12]:


byComp.sum()


# In[13]:


byComp.std()


# In[14]:


byComp.sum().loc['FB']


# In[15]:


df.groupby('Company').sum().loc['FB']


# In[16]:


df.groupby('Company').count()


# In[18]:


df.groupby('Company').max()


# In[19]:


df.groupby('Company').min()


# In[20]:


df.groupby('Company').describe()


# In[22]:


df.groupby('Company').describe().transpose()


# In[23]:


df.groupby('Company').describe().transpose()['FB']

