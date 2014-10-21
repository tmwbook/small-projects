import requests
from BeautifulSoup import BeautifulSoup

"""
Wikipedia has it so its Wikipedia.org/wiki/List_of_name_of_anime_episodes
"""

en_website_prefix_to_url = "http://en.wikipedia.org/wiki/List_of_"

def get_page_source(anime_name):
    formatted_anime_name = format_name(anime_name)
    target_url = en_website_prefix_to_url + formatted_anime_name
    return requests.get(target_url)

def format_name(title):
    list_of_words_in_title = title.split(" ")

    formatted_string = ""
    for word in list_of_words_in_title:
        formatted_string += word + "_"

    return formatted_string
