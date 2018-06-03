
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[3]:


df = pd.DataFrame({'col1':[1,2,3,4],
    'col2':[444,555,666,444],
    'col3':['abc','def','ghi','xyz']})
df.head()


# In[4]:


df['col2'].unique()


# In[5]:


len(df['col2'].unique())


# In[6]:


df['col2'].nunique() #Same  as link


# In[7]:


df['col2'].value_counts() #NO. of unique value


# In[8]:


df


# In[9]:


df[df['col1']>2]


# In[10]:


df['col1']>2


# In[11]:


df[(df['col1']>2) & (df['col2']==444)]


# In[12]:


def time2(x):
    return x*2


# In[13]:


df['col1'].apply(time2)


# In[14]:


df['col3'].apply(len)


# In[15]:


df['col2'].apply(lambda x : x*2)


# In[16]:


df


# In[17]:


df.drop('col1',axis=1)


# In[18]:


df


# In[21]:


df.columns


# In[22]:


df.index


# In[23]:


df


# In[24]:


df.sort_values('col2')


# In[25]:


df.sort_values(by='col2')


# In[26]:


df.isnull()


# In[31]:


data = {'A':['foo','foo','foo','bar','bar','bar'],
       'B':['one','one','two','two','one','one'],
        'C':['x','y','x','y','x','y'],
        'D':[1,3,2,5,4,1]
       }


# In[33]:


df = pd.DataFrame(data)


# In[34]:


df


# In[36]:


df.pivot_table(values='D',index=['A','B'],columns=['C'])

