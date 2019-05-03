#!/usr/bin/env python
# coding: utf-8

# In[1]:


import bs4 as bs
import textblob
import matplotlib.pyplot as plt
import seaborn as sns
import re
import urllib.request    


# In[2]:


source = urllib.request.urlopen('https://www.reuters.com/article/us-global-coffee-poll/coffee-prices-seen-rising-nearly-25-percent-by-year-end-reuters-poll-idUSKCN1Q11JD').read()
soup = bs.BeautifulSoup(source,'lxml')
# title of the page
print(soup.title)


# In[3]:


# get attributes:
print(soup.title.name)


# In[4]:


# get values:
print(soup.title.string)


# In[5]:


# beginning navigation:
print(soup.title.parent.name)


# In[6]:


for Pr in soup.find_all('p'):
    # print(paragraph.string)
    Pr = str(Pr.text)
    print(Pr)


# In[7]:


Paragraph_data = ""
sentiment=[]
for Pr in soup.find_all('p'):
    Pr = Pr.text
    Pr = re.sub('[h]+[t]+[t]+[p]+[a-z0-9A-Z./:]+','',Pr) # removing url
    print(Pr)
    Paragraph_data = Paragraph_data+' '+Pr
    Pr = textblob.TextBlob(Pr)
    if Pr.sentiment.polarity>0.01:
        print("positive")
        sentiment.append("positive")
    elif Pr.sentiment.polarity<-0.01:
        print("negative")
        sentiment.append("negative")
    else:
        print("Neutral")
        sentiment.append("neutral")
    print(" ")


# In[8]:


sns.countplot(sentiment)
plt.savefig('static/plot4.jpg')
plt.show()


# In[9]:


# pip install wordcloud
import wordcloud
wd = wordcloud.WordCloud(max_words=10).generate_from_text(Paragraph_data)


# In[10]:


plt.imshow(wd)
plt.savefig('static/wordcloud4.jpg')
plt.show()


# # my code

# fnfhn

# In[ ]:




