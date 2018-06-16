
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


# In[5]:


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y)


# In[6]:


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y,color='orange')  #RGB Also work


# In[7]:


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y,color='orange',linewidth=20)  #0.5 is default linewidth


# In[8]:


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y,color='orange',linewidth=3,alpha=0.1)   #Aplpha For transparence 


# In[9]:


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y,color='orange',lw=3,alpha=0.5)  #linewidth==lw


# In[11]:


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y,color='orange',lw=3,alpha=0.8,linestyle='-.')


# In[13]:


fig = plt.figure()                      #linestyle===ls
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y,color='orange',lw=3,alpha=0.8,linestyle='steps') #Linestyle, -- ,. etc


# In[14]:


x


# In[16]:


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y,color='orange',lw=3,ls='-',marker='o')  #marker == +,*,1,


# In[20]:


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y,color='orange',lw=3,ls='-',marker='*',markersize=20)  #marker == +,*,1,


# In[22]:


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y,color='orange',lw=1,ls='-',marker='2',markersize=20)  #marker == +,*,1,


# In[26]:


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y,color='purple',lw=1,ls='-',marker='o',markersize=20,
       markerfacecolor='yellow',markeredgewidth=3,markeredgecolor='green')


# In[31]:


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y,color='purple',lw=3,ls='--')
ax.set_xlim([0,1])
ax.set_ylim([0,2])

