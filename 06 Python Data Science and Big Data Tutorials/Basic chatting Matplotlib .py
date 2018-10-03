
# coding: utf-8

# In[1]:


get_ipython().magic(u'matplotlib inline')


# In[2]:


from matplotlib import pyplot as plt


# In[7]:


plt.plot([1,2,3],[2,5,7])
plt.show()


# In[9]:


plt.plot([1,2,3],[2,5,7])
plt.title("Rishav")
plt.ylabel("This is Y")
plt.xlabel("This is X")
plt.show()


# In[10]:


x = [8,6,2]
y = [23,45,88]
x2 = [56,47,33]
y2 = [5,8,9]
plt.plot(x,y)
plt.plot(x2,y2)
plt.show()


# In[12]:


from matplotlib import style 
style.use('ggplot')
x = [8,6,2]
y = [3,5,8]
x2 = [6,7,3]
y2 = [5,8,9]
plt.plot(x,y)
plt.plot(x2,y2)
plt.show()


# In[13]:


style.use('ggplot')
x = [8,6,2]
y = [3,5,8]
x2 = [6,7,3]
y2 = [5,8,9]
plt.plot(x,y,label = "first")
plt.plot(x2,y2 , label="second")
plt.legend()
plt.show()


# In[14]:


style.use('ggplot')
x = [8,6,2]
y = [3,5,8]
x2 = [6,7,3]
y2 = [5,8,9]
plt.plot(x,y,label = "first",linewidth=4)
plt.plot(x2,y2 , label="second")
plt.legend()
plt.show()


# In[16]:


style.use('ggplot')
x = [8,6,2]
y = [3,5,8]
x2 = [6,7,3]
y2 = [5,8,9]
plt.scatter(x,y,label = "first",linewidth=4)
plt.hist(x2,y2 , label="second")
plt.legend()
plt.show()

