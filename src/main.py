# we need to use a queue to do the BFS
from collections import deque

# defining the BFS method
def BFS(adj_list, start_id, target_id):
    # define a set to avoid duplicate visits
    seen = set()
    seen.add(start_id)

    # define a distance variable to keep track of the distance between start and end
    distance = 0

    id_queue = deque(start_id)

    while id_queue:
        curr = id_queue.popleft()

        for edge in adj_list[curr]:
            if edge not in seen:
                id_queue.append(edge)
                seen.append(edge)


