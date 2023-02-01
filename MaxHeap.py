class MaxHeap:
  def __init__(self):
    self.heap_list = [None]
    self.count = 0

  # HEAP HELPER METHODS

  def parent_idx(self, idx):
    return idx // 2

  def left_child_idx(self, idx):
    return idx * 2

  def right_child_idx(self, idx):
    return idx * 2 + 1

  def child_present(self, idx):
    return self.left_child_idx(idx) <= self.count

  # END OF HEAP HELPER METHODS
  
  def add(self, element):
    self.count += 1
    self.heap_list.append(element)
    self.heapify_up()
    
  def heapify_up(self):
    idx = self.count
    while self.parent_idx(idx) > 0:
      child = self.heap_list[idx]
      parent = self.heap_list[self.parent_idx(idx)]
      if parent.stars < child.stars:
        self.heap_list[idx] = parent
        self.heap_list[self.parent_idx(idx)] = child
      idx = self.parent_idx(idx)
    # Heap restored

  def retrieve_max(self):
    if self.count == 0:
      return None
    max_value = self.heap_list[1]
    self.heap_list[1] = self.heap_list[self.count]
    self.count -= 1
    self.heap_list.pop()
    self.heapify_down()
    return max_value

  def heapify_down(self):
    idx = 1
    while self.child_present(idx):
      larger_child_idx = self.get_larger_child_idx(idx)
      child = self.heap_list[larger_child_idx]
      parent = self.heap_list[idx]
      if parent.stars < child.stars:
        self.heap_list[idx] = child
        self.heap_list[larger_child_idx] = parent
      idx = larger_child_idx
    # Heap restored

  def get_larger_child_idx(self, idx):
    if self.right_child_idx(idx) > self.count:
      return self.left_child_idx(idx)
    else:
      left_child = self.heap_list[self.left_child_idx(idx)]
      right_child = self.heap_list[self.right_child_idx(idx)]
      if left_child.stars > right_child.stars:
        return self.left_child_idx(idx)
      else:
        return self.right_child_idx(idx)