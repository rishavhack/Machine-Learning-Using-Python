
# coding: utf-8

# In[1]:


import seaborn as sns


# In[2]:


get_ipython().magic(u'matplotlib inline')


# In[3]:


tips = sns.load_dataset('tips')


# In[4]:


tips.head()


# In[5]:


sns.lmplot(x='total_bill',y='tip',data=tips)


# In[6]:


sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex')


# In[9]:


sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex',markers=['o','v'])


# In[10]:


sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex',markers=['o','v'],
          scatter_kws={'s':100})


# In[11]:


sns.lmplot(x='total_bill',y='tip',data=tips)


# In[12]:


sns.lmplot(x='total_bill',y='tip',data=tips,col='sex')


# In[13]:


sns.lmplot(x='total_bill',y='tip',data=tips,col='sex',row='time')


# In[14]:


sns.lmplot(x='total_bill',y='tip',data=tips,col='day',row='time',hue='sex')


# In[15]:


sns.lmplot(x='total_bill',y='tip',data=tips,col='day',hue='sex')


# In[17]:


sns.lmplot(x='total_bill',y='tip',data=tips,col='day',hue='sex',
           aspect=0.6,size=8)

