{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "README.md",
      "version": "0.3.2",
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Kakarottox/Product-analysis/blob/master/README.md\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "UlR8otwMcTQY",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "G1H0Ow5jcXCR",
        "colab_type": "text"
      },
      "source": [
        ""
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Koag4jL8cXDp",
        "colab_type": "text"
      },
      "source": [
        "Products price forecasting\n",
        "\n",
        "\n",
        "\n",
        "This project consists of two parts:\n",
        "\n",
        "for the first part, we need the following libraries to be imported so that we can extract information from twitter:\n",
        "\n",
        "import tweepy\n",
        "import textblob\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "import re\n",
        "\n",
        "after getting access from twitter, we can run the following codes to start extracting information to forecast. \n",
        "\n",
        "consumer_key = \"G9DF5GheWj41pF2EOdL5voOfw\"\n",
        "consumer_secret = \"PtHiSqoPErNafoSHWqTka6o4ccthug19u4NgQ4r9L6onFWngJ2\"\n",
        "access_token = \"857530568-TbuDaZIq8waUZU2k5jwTVP8HAWeJQfNkOqEQ9FpL\"\n",
        "access_token_secret = \"Uqvnibxc34fuLjWOYMg9cN6LkwRJmcHc7lzYUMmPlBWkQ\"\n",
        "auth = tweepy.OAuthHandler(consumer_key,consumer_secret)\n",
        "auth.set_access_token(access_token,access_token_secret)\n",
        "api = tweepy.API(auth)\n",
        "\n",
        "\n",
        "As for the second part, we need the following  libraries to be imported:\n",
        "\n",
        "import bs4 as bs\n",
        "import textblob\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "import re\n",
        "import urllib.request   \n",
        "\n",
        "After importing, running the following codes will extract information from the chosen website to be able to forecast the information.\n",
        "\n",
        "source = urllib.request.urlopen('https://www.reuters.com/article/us-global-coffee-poll/coffee-prices-seen-rising-nearly-25-percent-by-year-end-reuters-poll-idUSKCN1Q11JD').read()\n",
        "soup = bs.BeautifulSoup(source,'lxml')\n",
        " title of the page\n",
        "print(soup.title)\n",
        "\n",
        "Both codes are required to extract information from multiple websites, avoiding biased information as well as more accurate forecasting. "
      ]
    }
  ]
}