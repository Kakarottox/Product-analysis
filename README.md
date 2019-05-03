# Products price forecasting



This project consists of two parts:

for the first part, we need the following libraries to be imported so that we can extract information from twitter:

import tweepy
import textblob
import matplotlib.pyplot as plt
import seaborn as sns
import re

after getting access from twitter, we can run the following codes to start extracting information to forecast. 

consumer_key = "G9DF5GheWj41pF2EOdL5voOfw"
consumer_secret = "PtHiSqoPErNafoSHWqTka6o4ccthug19u4NgQ4r9L6onFWngJ2"
access_token = "857530568-TbuDaZIq8waUZU2k5jwTVP8HAWeJQfNkOqEQ9FpL"
access_token_secret = "Uqvnibxc34fuLjWOYMg9cN6LkwRJmcHc7lzYUMmPlBWkQ"
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)


As for the second part, we need the following  libraries to be imported:

import bs4 as bs
import textblob
import matplotlib.pyplot as plt
import seaborn as sns
import re
import urllib.request   

After importing, running the following codes will extract information from the chosen website to be able to forecast the information.

source = urllib.request.urlopen('https://www.reuters.com/article/us-global-coffee-poll/coffee-prices-seen-rising-nearly-25-percent-by-year-end-reuters-poll-idUSKCN1Q11JD').read()
soup = bs.BeautifulSoup(source,'lxml')
 title of the page
print(soup.title)

Both codes are required to extract information from multiple websites, avoiding biased information as well as more accurate forecasting. 
