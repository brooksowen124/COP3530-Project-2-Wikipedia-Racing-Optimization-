import pickle


# -------------------------------------------------------------------------
# THIS FILE WAS ONLY USED TO GENERATE THE PICKLE FILES USED IN THIS PROJECT
# -------------------------------------------------------------------------

# Creates the adjacency list dictionary from the text file
def load_graph(filepath):
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
def load_id_map(filepath):
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
def save_dict(dict, outputpath):
    with open(outputpath, "wb") as file:
        pickle.dump(dict, file)



# RUNNING THIS FILE TAKES THE ADJACENCY LIST AND IDS TEXT FILES AND CONVERTS THEM TO PICKLE FILES
if __name__ == "__main__":
    adj = load_graph("../wiki-topcats.txt")
    ids = load_id_map("../wiki-topcats-page-names.txt")

    save_dict(adj, "../adjacency_list.pkl")
    save_dict(ids, "../id_mapping.pkl")

