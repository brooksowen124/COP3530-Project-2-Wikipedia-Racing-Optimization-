from collections import deque
import os
import pickle

# This class contains all relevant attributes and methods for loading
# data from pickle files and performing varying search algorithms

class AdjacencyMap:
    def __init__(self):
        # Load both the adjacency map graph representation and the id mapping dictionary into memory
        # We will later use another class method to define these

        self.adj_list = {}
        self.id_mapping = {}
        self.reverse_id_mapping = {}
        self.rev_adj_list = {}

        self.load_adj_attribute()
        self.load_id_attribute()
        self.build_reverse_graph()
        self.build_reverse_id_attribute()
        


    # Loads the adjacency list attribute from a pickle file
    def load_adj_attribute(self):
        try:
            with open("../adjacency_list.pkl", "rb") as file:
                self.adj_list = pickle.load(file)
            print("Pickle file loaded!")
        except:
            print("Pickle file failed to load")

    # Loads the id map attribute from a pickle file
    def load_id_attribute(self):
        try:
            with open("../id_mapping.pkl", "rb") as file:
                self.id_mapping = pickle.load(file)
            print("Pickle file loaded!")
        except:
            print("Pickle file failed to load")


    # Creates a reverse id map for faster name lookup
    def build_reverse_id_attribute(self):
        for key, value in self.id_mapping.items():
            self.reverse_id_mapping[value] = key

            
    def build_reverse_graph(self):
        rev_adj_list = {}
        for node, neighbors in self.adj_list.items():
            for neighbor in neighbors:
                if neighbor in rev_adj_list:
                    rev_adj_list[neighbor].add(node)
                else:
                    rev_adj_list[neighbor] = {node}
        self.rev_adj_list = rev_adj_list

    def load_reverse_attribute(self, filepath):
        if os.path.exists(filepath):
            with open(filepath, "rb") as file:
                self.rev_adj_list = pickle.load(file)
        else:
            self.build_reverse_graph()
            self.save_dict(self.rev_adj_list, filepath)

    # -------------------------------------
    # ID to Article Name Conversion Methods
    # -------------------------------------

    # Returns the article name of a given ID
    def id_to_name(self, id):
        if id in self.id_mapping:
            return self.id_mapping[id]
        else:
            raise IndexError("ID is out of range!")

    # Returns the ID for a given article name
    def name_to_id(self, name):
        if name in self.reverse_id_mapping:
            return self.reverse_id_mapping[name]
        else:
            raise IndexError("Invalid article name")



    def check_input(self, page_name):
        if page_name in self.reverse_id_mapping:
            return self.reverse_id_mapping[page_name]
        else:  
            return False


    # -------------------
    # Search Algorithms:
    # -------------------

    def BFS(self, start_id, target_id):
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

                for edge in self.adj_list[curr]:
                    if edge not in seen:
                        id_queue.append(edge)
                        seen.add(edge)

                        # add the parent to the parent dict
                        parent_dict[edge] = curr
            distance += 1

        # if theres no correct path
        return [], -1

    def bidirectional_BFS(self, start_id, target_id):
        if start_id == target_id:
            return [start_id], 0

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

        parents_f = {start_id: None}
        parents_b = {target_id: None}
        dist_f = {start_id: 0}
        dist_b = {target_id: 0}
        frontier_f = [start_id]
        frontier_b = [target_id]

        while frontier_f and frontier_b:
            if len(frontier_f) <= len(frontier_b):
                frontier_f, best = expand_level(frontier_f, self.adj_list, parents_f, dist_f, dist_b)
            else:
                frontier_b, best = expand_level(frontier_b, self.rev_adj_list, parents_b, dist_b, dist_f)

            if best is not None:
                meet, total = best
                return_path = []
                curr = meet
                while curr is not None:
                    return_path.append(curr)
                    curr = parents_f[curr]
                return_path.reverse()

                curr = parents_b[meet]
                while curr is not None:
                    return_path.append(curr)
                    curr = parents_b[curr]
                return return_path, total

        return [], -1
