
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt


# In[3]:


get_ipython().magic(u'matplotlib inline')


# In[4]:


import numpy as np


# In[7]:


x = np.linspace(0,5,11) 
y = x**2


# In[8]:


x


# In[9]:


y


# In[12]:


#Functional Method
plt.plot(x,y)
plt.xlabel('X LAble')
plt.ylabel('Y Lable')
plt.title('Title ')


# In[15]:


plt.subplot(1,2,1)  #No of row,No of column
plt.plot(x,y,'r')
plt.subplot(1,2,2)
plt.plot(y,x,'b')


# In[16]:


#Object Orient
fig = plt.figure()


# In[38]:


fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.8,0.8])
axes.plot(x,y)


# In[40]:


fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.8,0.8])
axes.plot(x,y)
axes.set_xlabel('X Label')
axes.set_ylabel('Y label')
axes.set_title('Title')


# In[54]:


fig = plt.figure()
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.2,0.5,0.4,0.3])
axes1.plot(x,y)
axes2.plot(y,x)
axes2.set_title('SMALLER PLOT')
axes1.set_title('LARGER PLOT')

