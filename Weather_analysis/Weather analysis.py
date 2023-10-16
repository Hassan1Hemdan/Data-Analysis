#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv(r"C:\Users\Hassan Hemdan\Downloads\file.csv")


# In[3]:


data


# In[5]:


data.head()


# In[6]:


data.shape


# In[7]:


data.index


# In[10]:


data.columns


# In[11]:


data.dtypes


# In[14]:


data["Weather"].unique()


# In[15]:


data.nunique()


# In[17]:


data.count()


# In[18]:


data["Weather"].value_counts()


# In[19]:


data.info()


# In[20]:


data.head(2)


# In[21]:


data.nunique()


# In[25]:


data["Wind Speed_km/h"].nunique()


# In[26]:


data["Wind Speed_km/h"].unique()


# In[27]:


data.head(2)


# In[28]:


data.Weather.value_counts()


# In[33]:


data.Weather == "Clear"


# In[34]:


data[data.Weather == "Clear"]


# In[35]:


data.groupby("Weather").get_group("Clear")


# In[37]:


data[data["Wind Speed_km/h"] == 4]


# In[38]:


data.isnull()


# In[39]:


data.isnull().sum()


# In[40]:


data.notnull().sum()


# In[41]:


data.rename(columns = {"Weather" : "Weather Conditions"})


# In[42]:


data.head(2)


# In[43]:


data.rename(columns = {"Weather" : "Weather Conditions"}, inplace = True)


# In[44]:


data.head(2)


# In[45]:


data.Visibility_km.mean()


# In[46]:


data.Press_kPa.std()


# In[47]:


data["Rel Hum_%"].var()


# In[49]:


data["Weather Conditions"].value_counts()


# In[50]:


data[data["Weather Conditions"] == "Snow"]


# In[51]:


data[data["Weather Conditions"].str.contains("snow")]


# In[52]:


data[data["Weather Conditions"].str.contains("Snow")]


# In[53]:


data[(data["Wind Speed_km/h"] > 24) & (data["Visibility_km"] == 25)]


# In[54]:


(data["Wind Speed_km/h"] > 24) & (data["Visibility_km"] == 25)


# In[62]:


data.groupby("Weather Conditions").min()


# In[64]:


data.groupby("Weather Conditions").max()


# In[65]:


data[data["Weather Conditions"] == "Fog"]


# In[69]:


data[(data["Weather Conditions"] == "Clear") | (data["Visibility_km"] > 40)]


# In[70]:


data[(data["Weather Conditions"] == "Clear") & (data["Rel Hum_%"] > 50) | (data["Visibility_km"] > 40)]

