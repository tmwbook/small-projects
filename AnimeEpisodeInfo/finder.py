import requests
from BeautifulSoup import BeautifulSoup

"""
Wikipedia has it so its Wikipedia.org/wiki/List_of_name_of_anime_episodes
"""

en_website_prefix_to_url = "http://en.wikipedia.org/wiki/List_of_"


def find_episode_tables(web_page_source):
    source = BeautifulSoup(web_page_source)
    return source.findAll("table", attrs={"class":  "wikitable"})


def get_all_episodes_in_season(episode_tables):
    all_seasons = {}
    i = 1
    for _ in episode_tables:
        all_seasons[i] = []
        i += 1
    i = 1
    for season in episode_tables:
        titles = season.findAll("td", attrs={"class": "summary"})
        descriptions = season.findAll("td", attrs={"class": "description"})
        num_of_episodes = len(titles)
        for j in range(0, num_of_episodes):
            episode = [titles[j]]
            try:
                description = descriptions[j]
            except IndexError:
                description = "N/A"
            finally:
                episode.append(description)
            all_seasons[i].append(episode)
        i += 1
    return all_seasons


def get_episode_info(all_seasons, season, episode_num):
    return extract_titles(all_seasons[season][episode_num - 1])


def extract_titles(title_code):
    eng_title = str(title_code[0]).split(">")[1].split("<")[0]
    romaji_title = title_code[0].find("i").getText()
    ja_title = title_code[0].find("span",
                                  attrs={"class": "t_nihongo_kanji"}).getText()
    return [eng_title, romaji_title, ja_title]


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
    page_response = get_page_source(test_anime)
    all_seasons = get_all_episodes_in_season(find_episode_tables(page_response))
    print get_episode_info(all_seasons, 1, 1)[2] #testing for title name
