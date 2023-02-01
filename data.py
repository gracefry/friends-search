import csv
import Episode

episodes = []

def import_dataset():
    with open("friends_episodes.csv", "r") as f:
        reader = csv.reader(f, delimiter=",")
        next(f, None) # Skip first line
        for row in reader: 
            episode_obj = Episode.Episode(row[0], row[1], row[2], row[3], row[5], row[7])
            append_array(episode_obj)

def append_array(episode):
    episodes.append(episode)

def get_array():
    return episodes

def display_episodes(episodes):
    print('''
    Matches:
    ''')

    print(f"| {'#':^3} | {'YEAR':^6} | {'EPISODE':^7} | {'TITLE':^50} | {'RATING':^5} |")
    print("-" * 88)

    i = 1

    for episode in episodes:
        year = episode.year
        season = episode.season
        ep = episode.ep
        title = episode.title
        rating = episode.stars

        print("| {:<3} | {:<6} | S{:<2} E{:<2} | {:<50} | {:<3} ★ |".format(i, year, season, ep, title, rating))

        i += 1

    print("-" * 88)