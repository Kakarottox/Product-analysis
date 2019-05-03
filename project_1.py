#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tweepy # accessing the Twitter API.
import textblob # processing textual data.
import matplotlib.pyplot as plt # To visualize the data
import seaborn as sns # To visualize data
import re # A regular expression


# In[2]:


# write your comments

consumer_key = "G9DF5GheWj41pF2EOdL5voOfw" # all of the following codes used to acces twitter.
consumer_secret = "PtHiSqoPErNafoSHWqTka6o4ccthug19u4NgQ4r9L6onFWngJ2"
access_token = "857530568-TbuDaZIq8waUZU2k5jwTVP8HAWeJQfNkOqEQ9FpL"
access_token_secret = "Uqvnibxc34fuLjWOYMg9cN6LkwRJmcHc7lzYUMmPlBWkQ"
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)


# In[3]:


help(tweepy.API) # explanation for all codes


# In[4]:


tweet = api.search(q="Coffee price", count = 100) # Used to look for a specific word


# In[5]:


tweet_data = ""
sentiment=[]
for tw in tweet:
    tw = tw.text
    tw = re.sub('RT','',tw) # removing RT
    tw = re.sub('[@]+[a-zA-Z:_]+','',tw) # removing twitter handle
    tw = re.sub('[h]+[t]+[t]+[p]+[a-z0-9A-Z./:]+','',tw) # removing url
    print(tw)
    tweet_data = tweet_data+' '+tw
    tw = textblob.TextBlob(tw)
    if tw.sentiment.polarity>0.1:
        print("positive")
        sentiment.append("positive")
    elif tw.sentiment.polarity<-0.1:
        print("negative")
        sentiment.append("negative")
    else:
        print("Neutral")
        sentiment.append("neutral")
    print(" ")


# In[6]:


sns.countplot(sentiment)
plt.savefig('static/plot.jpg')
plt.show()


# In[7]:


# pip install wordcloud
import wordcloud
wd = wordcloud.WordCloud(max_words=10).generate_from_text(tweet_data)


# In[8]:


plt.imshow(wd) # to visualize the data
plt.savefig('static/wordcloud.jpg')
plt.show()


# In[ ]:




