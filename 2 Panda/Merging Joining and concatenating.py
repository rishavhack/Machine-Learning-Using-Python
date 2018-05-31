
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[8]:


df1 = pd.DataFrame({'A':['A0','A1','A2','A3'],
                    'B':['B0','B1','B2','B3'],
                    'C':['C0','C1','C2','C3'],
                    'D':['D0','D1','D2','D3']},
                  index=[0,1,2,3])


# In[9]:


df2 = pd.DataFrame({'A':['A4','A5','A6','A7'],
                    'B':['B4','B5','B6','B7'],
                    'C':['C4','C5','C6','C7'],
                    'D':['D4','D5','D6','D7']},
                  index=[4,5,6,7])


# In[10]:


df3 = pd.DataFrame({'A':['A8','A9','A10','A11'],
                    'B':['B8','B9','B10','B11'],
                    'C':['C8','C9','C10','C11'],
                    'D':['D8','D9','D10','D11']},
                  index=[8,9,10,11])


# In[11]:


df1


# In[12]:


df2


# In[13]:


df3


# In[14]:


pd.concat([df1,df2,df3])


# In[15]:


pd.concat([df1,df2,df3],axis=1)


# In[18]:


left = pd.DataFrame({'key':['K0','K1','K2','K3'],
                    'A':['A0','A1','A2','A3'],
                    'B':['B0','B1','B2','B3']})


# In[19]:


right = pd.DataFrame({'key':['K0','K1','K2','K3'],
                    'C':['C0','C1','C2','C3'],
                    'D':['D0','D1','D2','D3']})


# In[20]:


left


# In[21]:


right


# In[22]:


pd.merge(left,right,how='inner',on='key')  #By default inner


# In[27]:


left = pd.DataFrame({'key1':['K0','K0','K1','K2'],
                     'key2':['K0','K1','K0','K1'],
                    'A':['A0','A1','A2','A3'],
                    'B':['B0','B1','B2','B3']})

right = pd.DataFrame({'key1':['K0','K1','K1','K2'],
                     'key2':['K0','K0','K0','K0'],
                    'C':['C0','C1','C2','C3'],
                    'D':['D0','D1','D2','D3']})


# In[28]:


left


# In[29]:


right


# In[30]:


pd.merge(left,right,on=['key1','key2'])


# In[31]:


pd.merge(left,right,how='outer', on=['key1','key2'])


# In[32]:


pd.merge(left,right,how='right', on=['key1','key2'])


# In[34]:


pd.merge(left,right,how='left', on=['key1','key2'])

