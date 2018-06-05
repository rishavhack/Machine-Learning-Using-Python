
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../../Pierian_Data_Logo.png' /></a>
# ___
# # Ecommerce Purchases Exercise
# 
# In this Exercise you will be given some Fake Data about some purchases done through Amazon! Just go ahead and follow the directions and try your best to answer the questions and complete the tasks. Feel free to reference the solutions. Most of the tasks can be solved in different ways. For the most part, the questions get progressively harder.
# 
# Please excuse anything that doesn't make "Real-World" sense in the dataframe, all the data is fake and made-up.
# 
# Also note that all of these questions can be answered with one line of code.
# ____
# ** Import pandas and read in the Ecommerce Purchases csv file and set it to a DataFrame called ecom. **

# In[1]:


import pandas as pd


# In[2]:


Ecom = pd.read_csv("Ecommerce Purchases");


# **Check the head of the DataFrame.**

# In[13]:


Ecom


# ** How many rows and columns are there? **

# In[4]:


Ecom.info() #len(ecom.columns)  #len(ecom.index)


# ** What is the average Purchase Price? **

# In[5]:


Ecom['Purchase Price'].mean()


# ** What were the highest and lowest purchase prices? **

# In[6]:


Ecom['Purchase Price'].max()


# In[7]:


Ecom['Purchase Price'].min()


# ** How many people have English 'en' as their Language of choice on the website? **

# In[11]:


Ecom[Ecom['Language']=='en'].count()


# ** How many people have the job title of "Lawyer" ? **
# 

# In[17]:


Ecom[Ecom['Job'] == 'Lawyer'].count()


# ** How many people made the purchase during the AM and how many people made the purchase during PM ? **
# 
# **(Hint: Check out [value_counts()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.value_counts.html) ) **

# In[20]:


Ecom['AM or PM'].value_counts()


# ** What are the 5 most common Job Titles? **

# In[25]:


Ecom['Job'].value_counts().head(5)


# ** Someone made a purchase that came from Lot: "90 WT" , what was the Purchase Price for this transaction? **

# In[26]:


Ecom[Ecom['Lot'] == '90 WT']['Purchase Price']


# ** What is the email of the person with the following Credit Card Number: 4926535242672853 **

# In[27]:


Ecom[Ecom['Credit Card'] == 4926535242672853]['Email']


# ** How many people have American Express as their Credit Card Provider *and* made a purchase above $95 ?**

# In[37]:


Ecom[(Ecom['CC Provider'] == 'American Express') & (Ecom['Purchase Price'] > 95)].count()


# ** Hard: How many people have a credit card that expires in 2025? **

# In[45]:


#Ecom['CC Exp Date'].iloc[0][3:]
Ecom[Ecom['CC Exp Date'].apply(lambda exp : exp[3:] == '25')].count()


# ** Hard: What are the top 5 most popular email providers/hosts (e.g. gmail.com, yahoo.com, etc...) **

# In[50]:


Ecom['Email'].apply(lambda email : email.split('@')[1]).value_counts().head(5)


# # Great Job!
