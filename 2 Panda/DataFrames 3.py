
# coding: utf-8

# In[5]:


import numpy as np
import pandas as pd
from numpy.random import randn


# In[6]:


outside=['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)


# In[7]:


df = pd.DataFrame(randn(6,2),hier_index,['A','B'])


# In[8]:


df


# In[9]:


df.loc['G1']


# In[12]:


df.loc['G1'].loc[1]


# In[16]:


#df.index.names --- >FrozenList([None, None])
df.index.names=['Groups','Num']


# In[17]:


df


# In[20]:


df.loc['G2'].loc[2]['B']


# In[22]:


df.xs('G1')


# In[24]:


df.xs(1,level='Num')

