import csv
import Episode

episodes = []

def importDataset():
    with open("friends_episodes.csv", "r") as f:
        reader = csv.reader(f, delimiter=",")
        next(f, None) # Skip first line
        for row in reader: 
            episode_obj = Episode.Episode(row[0], row[1], row[2], row[3], row[5], row[7])
            addToArray(episode_obj)
            
def addToArray(episode):
    episodes.append(episode)

def welcome():
    print('''
      Look up the Friends episode you forgot!                                                                                                                                                                 
    ''')
    importDataset()

def main():
    welcome()

if __name__ == "__main__":
    main()