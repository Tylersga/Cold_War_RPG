#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Russian:
    def __init__(self, n, f, p):
        self.name = n
        self.faction = f
        self.personality = p
    
    def introduce_self(self):
        print("My name is " + self.name)


# In[2]:


r1 = Russian("Dimitri", "Communist", "Heroic")
r2 = Russian("Linda", "Communist", "honest")


# In[3]:


r1.introduce_self()
r2.introduce_self()


# In[4]:


class American:
    def introduce_self(self):
        print("My name is " + self.name)
        
    def __init__(self, n, f, p, s):
        self.name = n
        self.faction = f
        self.personality = p
        self.is_spy = s
        
    def is_spy(self):
        self.is_spy = True
        
    def is_not_spy(self):
        self.is_spy = False


# In[5]:


a1 = American("John", "Capitalist", "rude", False)
a2 = American("Gertrude", "Communist", "nice", True)


# In[6]:


a2.american_target = a1


# In[7]:


a2.american_target.introduce_self()


# In[ ]:




