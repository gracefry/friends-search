import csv
import Episode
import MaxHeap

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

def getTop10(ls):
    sort = []
    max_heap = MaxHeap.MaxHeap()

    for idx in ls:
        max_heap.add(idx)
    
    while max_heap.count > 0:
        max_value = max_heap.retrieve_max()
        sort.insert(0, max_value.title)
        if len(sort) == 10:
            break

    return sort

def welcome():
    print('''
      Look up the Friends episode you forgot!                                                                                                                                                                 
    ''')


def main():
    importDataset()
    welcome()

    print(getTop10(getArray()))

if __name__ == "__main__":
    main()