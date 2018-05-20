
# coding: utf-8

# In[1]:


my_list=[1,2,3]


# In[2]:


import numpy as np


# In[4]:


arr = np.array(my_list)

arr
# In[5]:


arr


# In[1]:


my_mat = [[1,2,3],[2,3,4],[5,6,7],[8,9,7]]


# In[2]:


my_mat


# In[5]:


import numpy as np
np.array(my_mat)


# In[6]:


np.arange(0,10)


# In[7]:


np.arange(0,11)


# In[8]:


np.arange(0,11,2)


# In[9]:


np.zeros(3)


# In[12]:


np.zeros((2,3))


# In[13]:


np.ones((2,4))


# In[14]:


np.linspace(0,5,10)


# In[16]:


np.linspace(0,5,5)


# In[17]:


np.eye(4) #identical array


# In[18]:


np.random.rand(5)


# In[19]:


np.random.rand(5,5)


# In[20]:


np.random.randn(2)


# In[21]:


np.random.randn(4,4)


# In[22]:


np.random.randint(1,100)


# In[23]:


np.random.randint(1,100,10)


# In[24]:


arr = np.arange(25)


# In[25]:


arr


# In[26]:


ranarr = np.random.randint(0,50,10)


# In[27]:


ranarr


# In[28]:


arr.reshape(5,5)


# In[29]:


#arr.reshape(5,10) #its create array 12:30 video m dekho..No.Of row === no of column


# In[30]:


ranarr.max()


# In[31]:


ranarr.min()


# In[32]:


ranarr.min()


# In[33]:


ranarr


# In[34]:


ranarr.argmax() #Postion of maximun number


# In[35]:


ranarr.argmin()


# In[36]:


arr.shape


# In[38]:


arr = arr.reshape(5,5)

arr
# In[39]:


arr.shape


# In[40]:


arr.dtype


# In[41]:


from numpy.random import randint


# In[42]:


randint(2,10)

