
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# In[2]:


get_ipython().magic(u'matplotlib inline')


# In[3]:


import numpy as np


# In[4]:


x = np.linspace(0,5,11) 
y = x**2


# In[8]:


fig,axes = plt.subplots(nrows=1,ncols=2)
#axes.plot(x,y)


# In[9]:


fig,axes = plt.subplots(nrows=3,ncols=3)
#axes.plot(x,y)


# In[11]:


fig,axes = plt.subplots(nrows=3,ncols=3)
#axes.plot(x,y)
plt.tight_layout()


# In[12]:


axes


# In[13]:


fig,axes = plt.subplots(nrows=1,ncols=2)
#axes.plot(x,y)
for current_ax in axes:
    current_ax.plot(x,y)


# In[17]:


fig,axes = plt.subplots(nrows=1,ncols=2)
#axes.plot(x,y)
axes[0].plot(x,y)
axes[0].set_title('First')
axes[1].plot(y,x)
axes[1].set_title('Second')

plt.tight_layout()


# In[18]:


#FIGURE SIZE AND DPI


# In[21]:


fig = plt.figure(figsize=(8,2))

ax = fig.add_axes([0,0,1,1])
ax.plot(x,y)


# In[22]:


fig,axes = plt.subplots(nrows=2,ncols=1,figsize=(3,2))

axes[0].plot(x,y)

axes[1].plot(y,x)

plt.tight_layout()


# In[5]:


fig,axes = plt.subplots(nrows=2,ncols=1,figsize=(8,2))

axes[0].plot(x,y)

axes[1].plot(y,x)

plt.tight_layout()


# In[6]:


fig.savefig('myPicture.png')


# In[7]:


fig.savefig('myPicture.png',dpi=20)


# In[9]:


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y)
ax.set_title('Title')
ax.set_ylabel('Y')
ax.set_xlabel('X')


# In[10]:


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y)
ax.plot(y,x)


# In[12]:


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,x**2)
ax.plot(x,x**3)


# In[14]:


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,x**2,label="X Square")
ax.plot(x,x**3,label="X Cube") 

ax.legend()


# In[15]:


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,x**2,label="X Square")
ax.plot(x,x**3,label="X Cube") 

ax.legend(loc=10)   # loc =1 to 10


# In[16]:


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,x**2,label="X Square")
ax.plot(x,x**3,label="X Cube") 

ax.legend(loc=(0.1,0.1))   # loc =1 to 10

