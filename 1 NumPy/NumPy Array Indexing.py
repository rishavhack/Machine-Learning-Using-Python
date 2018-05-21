
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


arr = np.arange(0,11)


# In[3]:


arr


# In[4]:


arr[8]


# In[5]:


arr[1:5]


# In[6]:


arr[:6]


# In[7]:


arr[5:]


# In[8]:


arr[0:5]=88


# In[9]:


arr


# In[10]:


arr=np.arange(0,11)


# In[12]:


slice_0f_arr = arr[0:6]


# In[14]:


slice_0f_arr


# In[15]:


slice_0f_arr[:]=99


# In[16]:


slice_0f_arr


# In[17]:


arr


# In[18]:


arr_copy = arr.copy()


# In[19]:


arr


# In[21]:


arr_copy[:]=100


# In[22]:


arr


# In[23]:


arr_copy


# In[26]:


arr_2d=np.array([[5,10,12],[23,34,23],[23,345,56]])


# In[27]:


arr_2d


# In[28]:


arr_2d[0][0]


# In[29]:


arr_2d[0][2]=88


# In[30]:


arr_2d


# In[33]:


arr_2d[2,1]


# In[34]:


arr_2d[:2,1:]


# In[35]:


arr_2d[:2]


# In[36]:


arr  = np.arange(1,11)


# In[37]:


arr


# In[39]:


arr > 5 #get boolean value


# In[40]:


bool_arr = arr >5


# In[41]:


bool_arr


# In[42]:


arr[bool_arr]


# In[43]:


arr[arr>5]


# In[44]:


arr[arr<3]


# In[45]:


arr_2d = np.arange(50).reshape(5,10)


# In[46]:


arr_2d


# In[47]:


arr_2d[1:3]


# In[48]:


arr_2d[1:3,3:5]

