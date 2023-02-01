import csv
import Episode
import MaxHeap
import HashMap

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

def getArray():
    return episodes

def makeHash(ls):
    hash_map = HashMap.HashMap(236)

    for episode in ls:
        description = episode.title + " " + episode.summary
        hash_map.assign(episode, description)

    return hash_map

def findInDesc(keyword, hash):
    contains = []

    for pair in hash.array:
        if keyword in pair[1]:
            contains.append(pair[0].title)

    if len(contains) == 0:
        contains = "Sorry, there were no matches. Please try another keyword."

    return contains

def getTop(ls, num):
    sort = []
    max_heap = MaxHeap.MaxHeap()

    for idx in ls:
        max_heap.add(idx)
    
    while max_heap.count > 0:
        max_value = max_heap.retrieve_max()
        sort.append(max_value.title)
        if len(sort) == num:
            break

    return sort

def welcome():
    print('''
      Look up the Friends episode you forgot!                                                                                                                                                                 
    ''')


def main():
    importDataset()
    welcome()
    print(getTop(getArray(), 3)) # add error handling for 236 ep
    hash = makeHash(getArray())
    print(findInDesc("dies", hash))

if __name__ == "__main__":
    main()