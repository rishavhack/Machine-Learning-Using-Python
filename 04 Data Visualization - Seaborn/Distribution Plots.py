
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


sns.distplot(tips['total_bill'])


# In[6]:


sns.distplot(tips['total_bill'],kde=False)


# In[7]:


sns.distplot(tips['total_bill'],kde=False,bins=30)


# In[8]:


sns.distplot(tips['total_bill'],kde=False,bins=100)


# In[9]:


sns.jointplot(x='total_bill',y='tip',data=tips)


# In[10]:


sns.jointplot(x='total_bill',y='tip',data=tips,kind='hex')


# In[11]:


sns.jointplot(x='total_bill',y='tip',data=tips,kind='reg')


# In[12]:


sns.jointplot(x='total_bill',y='tip',data=tips,kind='kde')


# In[13]:


sns.pairplot(tips)


# In[14]:


sns.pairplot(tips,hue='sex')


# In[15]:


sns.pairplot(tips,hue='sex',palette='coolwarm')


# In[16]:


sns.rugplot(tips['total_bill'])


# In[19]:


sns.distplot(tips['total_bill'],kde=False)

