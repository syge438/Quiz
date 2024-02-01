#!/usr/bin/env python
# coding: utf-8

# ## Quiz Instructions
# Answer the following quiz questions.
# 
# As a researcher, you are tasked to do use ETL and EDA skills on a movie dataset to
# extract certain insights.
# 
# Using Pandas, use the "movie_dataset.csv" found in the "Week 1" section of Canvas.
# Note, some column names have spaces which is not ideal. Some columns have
# 
# missing values and it would be best to either fill or drop where appropriate those
# 
# missing values to prevent a bias. Load and clean the data, make reasonable
# assumptions.
# 
# Once this has been done, answer the Quiz questions below.

# ### Question 1 1 pts
# 
# What is the highest rated movie in the dataset?

# In[1]:


import pandas as pd


# In[21]:


data = pd.read_csv("Data/movie_dataset1.csv")


# In[22]:


data.info()


# In[104]:


data.head()


# In[24]:


data = data[~data['Title'].isna()]


# In[25]:


moviename_rating = data[['Title', 'Rating']]
moviename_rating = moviename_rating.dropna()
moviename_rating


# In[26]:


moviename_rating.sort_values(by = 'Rating', ascending=False)


# In[27]:


moviename_rating.sort_values(by = 'Rating', ascending=False).head(1)


# ### Question 2 1 pts
# 
# What is the average revenue of all movies in the dataset?
# 
# Note, since the answer will be effected by how you dealt with missing values a range
# has been provided.

# In[29]:


data[['Title', 'Revenue (Millions)']]


# In[31]:


data['Revenue (Millions)'].describe()


# In[36]:


data['Revenue (Millions)'] = data['Revenue (Millions)'].fillna(data['Revenue (Millions)'].mean()) #fill missing values with mean/average


# In[35]:


data[['Title', 'Revenue (Millions)']]


# In[37]:


data['Revenue (Millions)'].mean()


# In[39]:


#Answer is : Between 70 and 100 Million


# ### Question 3 1 pts
# 
# What is the average revenue of movies from 2015 to 2017 in the dataset?
# 
# Note, since the answer will be effected by how you dealt with missing values a range
# has been provided.

# In[42]:


data[(data['Year'] >= 2015) & (data['Year'] <= 2017)]['Revenue (Millions)'].mean()


# In[ ]:


#Answer is : Between 50 and 80 Million


# ### Question 4 1 pts
# 
# How many movies were released in the year 2016?

# In[44]:


data[data['Year'] == 2016]['Title'].nunique()


# ### Question 5 1 pts
# 
# How many movies were directed by Christopher Nolan?

# In[46]:


data[data['Director'] == 'Christopher Nolan']['Title'].nunique()


# ### Question 6 1 pts
# 
# How many movies in the dataset have a rating of at least 8.0?

# In[48]:


data[data['Rating'] >= 8]['Title'].nunique()


# ### Question 7 1 pts
# 
# What is the median rating of movies directed by Christopher Nolan?

# In[50]:


data[data['Director'] == 'Christopher Nolan']['Rating'].describe()


# ### Question 8 1 pts
# 
# Find the year with the highest average rating?

# In[57]:


data.groupby(['Year']).agg({"Rating": "mean"}).sort_values(by = 'Rating', ascending=False)


# ### Question 9 1 pts
# 
# What is the percentage increase in number of movies made between 2006 and
# 2016?

# In[65]:


n_movies_2006 = data[data['Year'] == 2006]['Title'].nunique()


# In[66]:


n_movies_2016 = data[data['Year'] == 2016]['Title'].nunique()


# In[64]:


n_movies_2006


# In[67]:


n_movies_2016


# In[70]:


((n_movies_2016 - n_movies_2006)/n_movies_2006)*100


# ### Question 10 3 pts
# 
# Find the most common actor in all the movies?
# 
# Note, the "Actors" column has multiple actors names. You must find a way to search
# for the most common actor in all the movies.

# In[99]:


actors = pd.DataFrame({"Actor": " ".join(data['Actors'].unique()).split(",")})


# In[100]:


actors['Actor'] = actors['Actor'].str.strip() #remove trailing and leading spaces


# In[101]:


actors


# In[103]:


actors['Actor'].value_counts()


# ### Question 12 10 pts
# 
# Do a correlation of the numerical features, what insights can you deduce? Mention at
# least 5 insights.

# In[107]:


data[['Year','Runtime (Minutes)', 'Rating', 'Votes', 'Revenue (Millions)','Metascore']]


# In[108]:


data[['Year','Runtime (Minutes)', 'Rating', 'Votes', 'Revenue (Millions)','Metascore']].corr()


# 1. Rating and Metascore have highest correlation of 63.19%
# 2. Revenue (Millions) and Votes have high positive correlation of 60.79%, meaning more votes you have the likelihood of generating more revenue
# 3. Year and Runtime (Minutes) have negative correlation of 16.49%, meaning lastest movies are shorter in length compared to the previous years
# 5. Year and Rating have negative correlation, suggesting that the quality of production is getting worse with time
# 5. Year and Votes have biggest negative correlation of 41.19%, suggesting that people enjoy watching older movies

# ### And what advice can you give directors to produce better movies?
# advice producers to make movies longer than 150 minutes to have rating between 8 and 9 to generate revenue between 80 to 500 million -- see graphs below

# In[123]:


data.groupby(['Rating']).agg({"Runtime (Minutes)": "mean"}).plot()


# In[122]:


data.groupby(['Rating']).agg({"Revenue (Millions)": "mean"}).plot()


# In[ ]:





# In[ ]:




