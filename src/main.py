# we need to use a queue to do the BFS
from collections import deque
import pickle

# defining the BFS method
def BFS(adj_list, start_id, target_id):
    # define a set to avoid duplicate visits
    seen = set()
    seen.add(start_id)

    # define a distance variable to keep track of the distance between start and end
    distance = 0

    id_queue = deque([start_id])

    while id_queue:
        # we can keep track of the distance by breaking the loop into levels
        level_size = len(id_queue)
        for i in range(level_size):

            curr = id_queue.popleft()
            if curr == target_id:
                return distance

            for edge in adj_list[curr]:
                if edge not in seen:
                    id_queue.append(edge)
                    seen.add(edge)
        distance += 1

    # if theres no correct path
    return -1



# load the pickle file
try:
    with open("../adjacency_list.pkl", "rb") as file:
        adj_list = pickle.load(file)
except:
    print("Pickle file failed to load")

# Testing out the BFS function
print(BFS(adj_list, 67, 6767))


