from collections import deque
import pickle

# This class contains all relevant attributes and methods for loading
# data from pickle files and performing varying search algorithms

class AdjacencyMap:
    def __init__(self):
        # Initialize both the adjacency map graph representation and the id mapping dictionary
        # We will later use another class method to define these

        self.adj_list = {}
        self.id_mapping = {}

    # ----------------------------------
    # FILE LOADING/PREPARATION FUNCTIONS:
    # ----------------------------------

    # Creates the adjacency list from the text file
    def load_graph(self, filepath):
        adj_dict = {}

        # iterate through the edge list to add values to the dictionary
        with open(filepath, "r") as edge_list:
            for line in edge_list:
                id = int(line.split()[0])
                edge = int(line.split()[1])

                # check if there is already a set at the given id
                if id in adj_dict:
                    adj_dict[id].add(edge)
                else:
                    adj_dict[id] = {edge}
        return adj_dict

    # Creates the id mapping from the text file
    def load_id_map(self, filepath):
        id_mapping = {}

        with open(filepath, "r") as file:
            for line in file:
                # skip lines with only one value
                if len(line.strip().split(" ", 1)) < 2:
                    continue
                id, name = line.strip().split(" ", 1)
                id_mapping[int(id)] = name
        return id_mapping

    # Saves a dictionary to a pickle file
    def save_dict(self, dict, outputpath):
        with open(outputpath, "wb") as file:
            pickle.dump(dict, file)

    # Loads the adjacency list attribute from a pickle file
    def load_adj_attribute(self, filepath):
        try:
            with open(filepath, "rb") as file:
                self.adj_list = pickle.load(file)
            print("Pickle file loaded!")
        except:
            print("Pickle file failed to load")

    # Loads the id map attribute from a pickle file
    def load_id_attribute(self, filepath):
        try:
            with open(filepath, "rb") as file:
                self.id_mapping = pickle.load(file)
            print("Pickle file loaded!")
        except:
            print("Pickle file failed to load")

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
        for key, value in self.id_mapping.items():
            if value == name:
                return key
        raise IndexError("Invalid article name")


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
