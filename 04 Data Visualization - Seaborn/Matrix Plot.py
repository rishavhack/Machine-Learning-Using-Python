
# coding: utf-8

# In[1]:


import seaborn as sns


# In[2]:


get_ipython().magic(u'matplotlib inline')


# In[3]:


tips = sns.load_datasetataset('tips')


# In[4]:


flights = sns.load_datasettaset('flights')


# In[5]:


tips.head()


# In[8]:


flights.head()


# In[10]:


tc = tips.corr()


# In[12]:


tc


# In[11]:


sns.heatmap(tc)


# In[13]:


sns.heatmap(tc,annot=True)


# In[14]:


sns.heatmap(tc,annot=True,cmap='coolwarm')


# In[15]:


flights.pivot_table(index='month',columns='year',values='passengers')


# In[17]:


fp = flights.pivot_table(index='month',columns='year',values='passengers')


# In[18]:


sns.heatmap(fp)


# In[19]:


sns.heatmap(fp,cmap='magma')


# In[20]:


sns.heatmap(fp,cmap='magma',linecolor='white',linewidths=1)


# In[21]:


sns.heatmap(fp,cmap='coolwarm',linecolor='white',linewidths=1)


# In[22]:


sns.clustermap(fp)


# In[23]:


sns.clustermap(fp,cmap='coolwarm')


# In[24]:


sns.clustermap(fp,standard_scale=1)

