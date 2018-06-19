
# coding: utf-8

# In[1]:


import seaborn as sns


# In[2]:


get_ipython().magic(u'matplotlib inline')


# In[5]:


tips = sns.load_dataset('tips')


# In[6]:


tips.head()


# In[5]:


sns.barplot(x='sex',y='total_bill',data=tips)


# In[3]:


import numpy as np


# In[7]:


sns.barplot(x='sex',y='total_bill',data=tips,estimator=np.std)


# In[8]:


sns.countplot(x='sex',data=tips)


# In[9]:


sns.boxplot(x='day',y='total_bill',data=tips)


# In[10]:


sns.boxplot(x='day',y='total_bill',data=tips,hue='smoker')


# In[11]:


sns.violinplot(x='day',y='total_bill',data=tips)


# In[7]:


sns.violinplot(x='day',y='total_bill',data=tips,hue='sex')


# In[8]:


sns.violinplot(x='day',y='total_bill',data=tips,hue='sex',split=True)


# In[10]:


sns.stripplot(x='day',y='total_bill',data=tips)


# In[11]:


sns.stripplot(x='day',y='total_bill',data=tips,jitter=True)


# In[12]:


sns.stripplot(x='day',y='total_bill',data=tips,jitter=True,hue='sex')


# In[13]:


sns.stripplot(x='day',y='total_bill',data=tips,jitter=True,hue='sex',split=True)


# In[16]:


sns.swarmplot(x='day',y='total_bill',data=tips)


# In[18]:


sns.violinplot(x='day',y='total_bill',data=tips)
sns.swarmplot(x='day',y='total_bill',data=tips,color='black')


# In[19]:


sns.factorplot(x='day',y='total_bill',data=tips,kind='bar')


# In[20]:


sns.factorplot(x='day',y='total_bill',data=tips,kind='violin')

