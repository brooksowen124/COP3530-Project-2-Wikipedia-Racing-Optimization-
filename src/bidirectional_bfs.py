import os
import pickle


def build_reverse(adj_list):
    rev_adj_list = {}
    for node, neighbors in adj_list.items():
        for neighbor in neighbors:
            if neighbor in rev_adj_list:
                rev_adj_list[neighbor].add(node)
            else:
                rev_adj_list[neighbor] = {node}
    return rev_adj_list


def expand_level(frontier, graph, parents, dist, other_dist):
    next_frontier = []
    best = None
    for curr in frontier:
        for neighbor in graph.get(curr, ()):
            if neighbor not in parents:
                parents[neighbor] = curr
                dist[neighbor] = dist[curr] + 1
                next_frontier.append(neighbor)
                if neighbor in other_dist:
                    total = dist[neighbor] + other_dist[neighbor]
                    if best is None or total < best[1]:
                        best = (neighbor, total)
    return next_frontier, best


def build_path(meet, parents_f, parents_b):
    front = []
    curr = meet
    while curr is not None:
        front.append(curr)
        curr = parents_f[curr]
    front.reverse()

    curr = parents_b[meet]
    while curr is not None:
        front.append(curr)
        curr = parents_b[curr]
    return front


def bidirectional_BFS(adj_list, rev_adj_list, start_id, target_id):
    if start_id == target_id:
        return [start_id], 0

    parents_f = {start_id: None}
    parents_b = {target_id: None}
    dist_f = {start_id: 0}
    dist_b = {target_id: 0}
    frontier_f = [start_id]
    frontier_b = [target_id]

    while frontier_f and frontier_b:
        if len(frontier_f) <= len(frontier_b):
            frontier_f, best = expand_level(frontier_f, adj_list, parents_f, dist_f, dist_b)
        else:
            frontier_b, best = expand_level(frontier_b, rev_adj_list, parents_b, dist_b, dist_f)

        if best is not None:
            meet, total = best
            return build_path(meet, parents_f, parents_b), total

    return [], -1


def load_reverse(adj_list, rev_path="../reverse_adjacency_list.pkl"):
    if os.path.exists(rev_path):
        with open(rev_path, "rb") as file:
            return pickle.load(file)
    rev_adj_list = build_reverse(adj_list)
    with open(rev_path, "wb") as file:
        pickle.dump(rev_adj_list, file)
    return rev_adj_list


if __name__ == "__main__":
    with open("../adjacency_list.pkl", "rb") as file:
        adj_list = pickle.load(file)
    print("Adjacency list loaded")
    rev_adj_list = load_reverse(adj_list)
    print("Reverse adjacency list ready")
    print(bidirectional_BFS(adj_list, rev_adj_list, 1244079, 1453226))
