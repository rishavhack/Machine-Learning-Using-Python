
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# In[2]:


get_ipython().magic(u'matplotlib inline')


# In[6]:


import numpy as np
x = np.linspace(0,5,11)
y = x ** 2


# In[7]:


x


# In[8]:


y


# In[11]:


#Function Method
plt.plot(x,y)
#plt.show()


# In[12]:


plt.plot(x,y,'r-')


# In[13]:


plt.plot(x,y)
plt.xlabel('X Lable')
plt.ylabel('Y Lable')
plt.title('Title')


# In[14]:


plt.subplot(1,2,1)
plt.plot(x,y,'r')

plt.subplot(1,2,2)
plt.plot(y,x,'b')


# In[15]:


#Object orient
fig = plt.figure()


# In[16]:


fig = plt.figure()

axes = fig.add_axes([0.1,0.1,0.8,0.8])


# In[17]:


fig = plt.figure()

axes = fig.add_axes([0.1,0.1,0.8,0.8])

axes.plot(x,y)


# In[18]:


fig = plt.figure()

axes = fig.add_axes([0.1,0.1,0.8,0.8])

axes.plot(x,y)
axes.set_xlabel('X Label')
axes.set_ylabel('Y Label')
axes.set_title('Set Title')


# In[19]:


fig = plt.figure()
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.2,0.5,0.4,0.3])


# In[20]:


fig = plt.figure()
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.2,0.15,0.4,0.3])
 


# In[22]:


fig = plt.figure()
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.5,0.5,0.4,0.3])


# In[23]:


fig = plt.figure()
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.2,0.5,0.4,0.3])

axes1.plot(x,y)
axes2.plot(y,x)


# In[24]:


fig = plt.figure()
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.2,0.5,0.4,0.3])
axes1.set_title('Larger Plot')
axes1.plot(x,y)
axes2.plot(y,x)
axes2.set_title('Smaller plot')

