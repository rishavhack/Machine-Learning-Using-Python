
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt


# In[3]:


get_ipython().magic(u'matplotlib inline')


# In[4]:


import numpy as np


# In[6]:


x  = np.arange(0,100)
y = x*2
z = x**2


# In[9]:


fig = plt.figure()
ax= fig.add_axes([0,0,1,1])
ax.plot(x,y)
ax.set_xlabel('X')
ax.set_ylabel('y')
ax.set_title('title')


# In[10]:


#Create a figure object and put two axes on it,ax1 and ax2. Located at [0,0,1,1]
#and [0.2,0.5,0.2,0.2] respectively

#Q2. Now plot (x,y) both axes. And call your figyre object to show it


# In[15]:


fig = plt.figure()
 

ax1 = fig.add_axes([0,0,1,1]) 
ax2 =  fig.add_axes([0.2,.5,.2,.2])


#Q2.
ax1.plot(x,y)
ax2.plot(x,y)


# In[16]:


#Exercise 3 
#Create the plot below by adding two axes to figure object at [0,0,1,1]
#and [0.2,0.5,.4,.4]

#Q2. Now use x,y and z arrays to recreate the plot below.Notice the xlimits and
#y limits on the inserted plot


# In[21]:


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax2 = fig.add_axes([.2,.5,.4,.4]) 

#Q2
ax.plot(x,z)
ax.set_xlabel('X')
ax.set_ylabel('Z')

#Insert box
ax2.plot(x,y)
ax2.set_title('Zoom')
ax2.set_xlabel('X')
ax2.set_ylabel('y')
ax2.set_xlim([20,22])
ax2.set_ylim([30,50])


# In[22]:


#Exercise 4
#Use olt.subplots(nrows=1,ncols=2) to create the plot below


# In[23]:


fig,axes = plt.subplots(1,2)


# In[24]:


#Now plot(x,y) and (x,z) on the axes. Play around with the linewidth and style


# In[25]:


fig,axes = plt.subplots(1,2)

axes[0].plot(x,y,color='blue',lw=3,ls='--')
axes[1].plot(x,z,color='red',lw=3)


# In[26]:


#resize the plot by adding the figsize() argument


# In[28]:


fig,axes = plt.subplots(1,2,figsize=(12,2))

axes[0].plot(x,y,color='blue',lw=3,ls='-')
axes[1].plot(x,z,color='red',lw=3,ls='--')

