import HashMap
import data

def make_hashmap():
    hash_map = HashMap.HashMap(236)

    for episode in data.get_array():

        # Make the description include both the title and summary
        description = episode.title + " " + episode.summary

        hash_map.assign(episode, description)

    return hash_map

def search_description(keyword, hashmap):
    matching_episodes = []

    for pair in hashmap.array:
        if keyword in pair[1]:
            matching_episodes.append(pair[0])

    if len(matching_episodes) == 0:
        return "0"

    return matching_episodes