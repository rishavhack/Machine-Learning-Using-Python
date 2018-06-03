
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


sal = pd.read_csv('Salaries.csv');


# In[3]:


sal


# In[6]:


sal['BasePay']


# In[7]:


#Use the .info() method to find out how many entries there are.
sal.info()


# In[8]:


#What is the Average BasePAy?
sal['BasePay'].mean()


# In[9]:


#What is the highest amouhnt of OverTimePay in th edataSet?
sal['OvertimePay'].max()


# In[15]:


# What is the job title of JOSEPH DRISCOLL? NOTE:Use all caps,otherwise you may 
#get an answer that does't match up(there is also a lowercase Joseph Driscol)
sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle']


# In[19]:


#How much does JOSEPH DRISCOLL make (including benefits)
sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits']


# In[21]:


#What is the name of highest paid person(including Benifts)
sal[sal['TotalPayBenefits']==[sal['TotalPayBenefits'].max()]]['EmployeeName']


# In[25]:


#same question as above
sal.loc[sal['TotalPayBenefits'].idxmax()] #we can also use argmax()


# In[24]:


#What is the name of lowest paid person(includeing Benefits)?Do you notice something
#strange about how much he or she is paid?
sal[sal['TotalPayBenefits']==sal['TotalPayBenefits'].min()]['EmployeeName']


# In[28]:


#same question as above
sal.iloc[sal['TotalPayBenefits'].argmin()]


# In[31]:


#What was the average (mean) basepay of all employee per year?(2001-2014)?
sal.groupby('Year').mean()
sal.groupby('Year').mean()['BasePay']


# In[35]:


#how many unique job titles are there?
sal['JobTitle'].unique()
len(sal['JobTitle'].unique())
sal['JobTitle'].nunique()


# In[36]:


#what are the top 5 most common jobs?
sal['JobTitle'].value_counts().head(5)


# In[39]:


#How many job title were represented by only one person in 2013?(e.g Job Titles)
#With only one occurence in 2013?)
sum(sal[sal['Year']==2013]['JobTitle'].value_counts() == 1)


# In[46]:


#How many people have the word Chief in their job title
def chief_string(title):
    if 'chief' in title.lower().split():
        return True
    else:
         return False


# In[52]:


sum(sal['JobTitle'].apply(lambda x:chief_string(x)))


# In[53]:


#Is there a correlation between length of the job title string and salary?
sal['title_len']=sal['JobTitle'].apply(len)


# In[54]:


sal[['JobTitle','title_len']]


# In[55]:


sal[['JobTitle','title_len']].corr()


# In[57]:


sal[['TotalPayBenefits','title_len']].corr()

