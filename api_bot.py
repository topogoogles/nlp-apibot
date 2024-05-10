import string
import nltk
import requests

from googlesearch import search
from lxml import html
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem import WordNetLemmatizer


# helper function to generate text corpus from html elements
def generate_corpus(all_p_elements):
    corpus = ""
    for p_element in all_p_elements:
        corpus += "\n" + "".join(p_element.findAll(text=True))
    return corpus


def get_bot_response(user_input):
    # default bot response
    bot_response = "I'm sorry, I don't think I can help you with that :("
    try:
        # use the google search api to fetch top 3 search results
        google_search_results = list(search(user_input, stop=3, pause=1))

        # use the requests api to fetch the top result webpage
        webpage = requests.get(google_search_results[0])
        webpage_tree = html.fromstring(webpage.content)
        webpage_soup = BeautifulSoup(webpage.content, "lxml")

        # extract all <p> elements from webpage soup object
        all_p_list = webpage_soup.findAll("p")

        # generate corpus from all <p> elements
        google_search_corpus = generate_corpus(all_p_list)

    except:
        # return the default response if corpus is empty
        if len(google_search_corpus) == 0:
            return bot_response
