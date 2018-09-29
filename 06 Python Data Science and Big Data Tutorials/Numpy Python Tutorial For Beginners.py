
# coding: utf-8

# ## Basic function

# In[1]:


import numpy as np


# In[2]:


arr = np.arange(1000000)


# In[3]:


pythonList = list(range(1000000))


# In[4]:


pythonList


# In[5]:


arr


# In[6]:


#Now Check the speed of two list
get_ipython().magic(u'time for _ in range(10):    [item*3 for item in pythonList]')


# In[7]:


get_ipython().magic(u'time for _ in range(10):    arr = arr*3')


# In[8]:


array1 = np.array([[3,4,5,6],[3,5,7,8]])


# In[9]:


array1


# In[10]:


array1.shape


# In[11]:


array1.dtype


# In[12]:


array2 = np.array([[3,4,5,6],[0.8,5,7,8.0]])


# In[13]:


array2


# In[14]:


array2.dtype


# In[15]:


array2 = np.array([[3,4,5,6],[0.8,5,7,8.0]],dtype="int32")


# In[16]:


array2


# In[17]:


np.zeros(4)


# In[18]:


np.zeros((4,8)) #Argument should be tuple


# In[19]:


np.ones(6)


# In[20]:


np.ones(6).dtype


# In[21]:


np.empty((4,6))  #This is garbage value 


# In[22]:


array1 * array1 # This is not matrix multiplication this is Element multiplication


# In[23]:


array1 + array1 


# In[24]:


array1 / array1 


# In[25]:


array1**array1 


# In[26]:


1/array1


# In[27]:


ar1 = np.array([[1,2,3],[4,5,6]])


# In[28]:


ar1


# In[29]:


ar1.sum(axis=1) #add All row value->1+2+3


# In[30]:


ar1.sum(axis=0)


# In[31]:


b = np.array([[7,8,9],[2,8,0]])


# In[32]:


ar1.dot(b.transpose()) #a - 2 *3 and b = 2*3,So matrix multiplication will not happen 
#So apply b.transpose()


# In[33]:


len(dir(np)) #it will give number of function define in numpy


# In[34]:


np.cross(ar1,b)


# In[35]:


np.sort(b)


# In[36]:


np.sort(b,axis=0)


# In[37]:


np.sort(b,axis=0,kind='mergesort') #You can write algo name in kind


# In[38]:


np.sort(b,axis=0,kind='quicksort')


# In[39]:


arr2 = np.arange(6)


# In[40]:


arr2


# In[50]:


c = np.array([1,23,4,88,56,4,243,45,6,45,454,56,8,8,66,88,55,8])


# In[43]:


c.shape


# In[46]:


c.reshape(6,3)


# In[48]:


c.reshape(2,9)


# In[51]:


c


# In[52]:


np.argsort(c) #index


# In[54]:


np.argmax(c)


# In[55]:


np.argmin(c)


# In[56]:


d = c.reshape(2,9)


# In[57]:


np.argsort(d,axis=0)


# In[58]:


np.argsort(d,axis=1)

