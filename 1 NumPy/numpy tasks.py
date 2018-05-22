
# coding: utf-8

# In[11]:


import numpy as np


# In[8]:


arr = np.zeros(2)


# In[9]:


arr


# In[10]:


np.zeros(10)


# In[11]:


np.ones(10)


# In[4]:


np.ones(10) * 5


# In[13]:


np.arange(10,51)


# In[14]:


np.arange(10,51,2)


# In[37]:


np.arange(9).reshape(3,3)
np.array([[0,1,2],[3,4,5],[6,7,8]])


# In[8]:


np.reshape(1,1)


# In[13]:


np.eye(3)


# In[14]:


np.random.rand(1)


# In[39]:


np.random.randn(25)


# In[46]:


np.arange(1,101).reshape(10,10) / 100


# In[49]:


np.linspace(0.01,1,100).reshape(10,10)


# In[50]:


np.linspace(0,1,20)


# In[40]:


mat = np.arange(1,26).reshape(5,5)


# In[17]:


mat


# In[19]:


mat[2:,1:]


# In[20]:


mat[3,4]


# In[52]:


mat[:3,1:2] #Important  mat[:3,1]


# In[53]:


mat[4,:] #mat[-1:]


# In[34]:


mat[3:,:]


# In[36]:


mat.sum()


# In[54]:


np.std(mat) #Standard DEviation


# In[55]:


mat.sum(axis=0)

