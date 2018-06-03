
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


pwd


# In[5]:


pd.read_csv('example.csv')


# In[6]:


df = pd.read_csv('example.csv')


# In[7]:


df


# In[8]:


df.to_csv('My_output')


# In[9]:


pd.read_csv('My_output')


# In[10]:


df.to_csv('My_output1',index=False)


# In[11]:


pd.read_csv('My_output1')


# In[12]:


#pip install xlrd    to use in cmd


# In[13]:


pd.read_excel('Excel_Sample.xlsx',sheetname='Sheet1')  #pip install xlrd


# In[14]:


df.to_excel('Excel_Sample2.xlsx',sheete_name='NewSheet') ##pip install xlrd  to create 
   new xlsx


# In[15]:


data=pd.read_html('https://www.fdic.gov/bank/individual/failed/banklist.html')


# In[16]:


from sqlalchemy import create_engine

