# we need to use a queue to do the BFS
from collections import deque
import pickle

# defining the BFS method
def BFS(adj_list, start_id, target_id):
    # define a set to avoid duplicate visits
    seen = set()

    # we're also going to use a parent dictionary to reverse engineer the path once the end node is reached
    parent_dict = {start_id: None}
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
                # iterate through the parent list to return the path
                return_path = []
                curr = target_id

                while curr is not None:
                    return_path.append(curr)
                    curr = parent_dict[curr]

                return_path.reverse()
                return return_path, distance

            for edge in adj_list[curr]:
                if edge not in seen:
                    id_queue.append(edge)
                    seen.add(edge)

                    # add the parent to the parent dict
                    parent_dict[edge] = curr
        distance += 1

    # if theres no correct path
    return [], -1



# load the pickle file
try:
    with open("../adjacency_list.pkl", "rb") as file:
        adj_list = pickle.load(file)
    print("Pickle file loaded!")
except:
    print("Pickle file failed to load")

# Testing out the BFS function
print(BFS(adj_list, 1244079, 1453226))



