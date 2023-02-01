import MaxHeap

def get_top(episodes, num):
    sort = []
    max_heap = MaxHeap.MaxHeap()

    for episode in episodes:
        max_heap.add(episode)
    
    while max_heap.count > 0:
        max_value = max_heap.retrieve_max()
        sort.append(max_value)
        if len(sort) == num:
            break

    return sort