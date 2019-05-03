#!/usr/bin/env python
# coding: utf-8

# In[1]:


import bs4 as bs # pulling data out of HTML and XML files
import textblob #These codes are the same codes explained previously
import matplotlib.pyplot as plt
import seaborn as sns
import re
import urllib.request # defines functions and classes which help in opening URLs 


# In[2]:


source = urllib.request.urlopen('https://www.reuters.com/article/us-global-coffee-poll/coffee-prices-seen-rising-nearly-25-percent-by-year-end-reuters-poll-idUSKCN1Q11JD').read()
# imports the document written from a website and reads it
soup = bs.BeautifulSoup(source,'lxml') # Analyzing documents
# title of the page
print(soup.title) # Title of the home page from the same URL


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
    print(Pr) # print text and strings from the URL


# In[7]:


Paragraph_data = ""
sentiment=[] # remove anything without a true value by using codes below
for Pr in soup.find_all('p'):
    Pr = Pr.text
    Pr = re.sub('[h]+[t]+[t]+[p]+[a-z0-9A-Z./:]+','',Pr) # removing url
    print(Pr)
    Paragraph_data = Paragraph_data+' '+Pr # collect the text using dictionary from textblob 
    Pr = textblob.TextBlob(Pr) 
    if Pr.sentiment.polarity>0.01:
        print("positive") 
        sentiment.append("positive") # shows positive meaning >0.1
    elif Pr.sentiment.polarity<-0.01:
        print("negative")
        sentiment.append("negative") # negative meaning <-0.1
    else:
        print("Neutral")
        sentiment.append("neutral") # neutral meaning 0.0
    print(" ")


# In[8]:


sns.countplot(sentiment) #  collect data and create a histogram
plt.savefig('static/plot4.jpg')
plt.show() # visualization of the data gathered


# In[9]:


# pip install wordcloud
import wordcloud
wd = wordcloud.WordCloud(max_words=10).generate_from_text(Paragraph_data)


# In[10]:


plt.imshow(wd)
plt.savefig('static/wordcloud4.jpg')
plt.show() # show the WordCloud after collecting the data from the chosen URL.

