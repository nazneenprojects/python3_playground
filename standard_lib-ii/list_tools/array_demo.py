from array import array

a = array('H', [123, 344, 4555, 334])
var_addition = sum(a)

print(var_addition)

print(a[1:3])


from collections import deque
d = deque(["task1", "task2", "task3"])
d.append("task4")
print("Working on", d.popleft())

"""  ..............BFS.................
unsearched = deque([starting_node])
def breadth_first_search(unsearched):
    node = unsearched.popleft()
    for m in gen_moves(node):
        if is_goal(m):
            return m
        unsearched.append(m)
"""


import bisect
scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
bisect.insort(scores, (300, 'ruby'))                                    # Keep sorted

print(scores)


from heapq import heapify , heappop , heappush
data = [1,2,3,40, -1,455, 0, 223, 12]
heapify(data)                      # rearrange the list into heap order
print([heappop(data) for i in range(3)])
heappush(data, -5)                 # add a new entry
print([heappop(data) for i in range(6)])  # fetch the three smallest entries
