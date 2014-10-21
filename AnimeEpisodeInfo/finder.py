import requests
from BeautifulSoup import BeautifulSoup

"""
Wikipedia has it so its Wikipedia.org/wiki/List_of_name_of_anime_episodes
"""

en_website_prefix_to_url = "http://en.wikipedia.org/wiki/List_of_"

def find_episode_table(web_page_source):
    source = BeautifulSoup(web_page_source)
    return source.find("div",attrs={"id":  "content"})

def get_page_source(anime_name):
    formatted_anime_name = format_name(anime_name)
    target_url = en_website_prefix_to_url + formatted_anime_name + "_episodes"
    return requests.get(target_url).content

def format_name(title):
    list_of_words_in_title = title.split(" ")

    formatted_string = ""
    for word in list_of_words_in_title:
        formatted_string += word + "_"

    return formatted_string

if __name__ == "__main__":
    test_anime = raw_input()
    page_response =  get_page_source(test_anime)    
    print find_episode_table(page_response)
