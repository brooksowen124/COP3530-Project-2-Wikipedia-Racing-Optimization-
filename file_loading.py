import pickle # we will use the pickle module to store the dictionary in a pickle file


# define the function for creating the adjacency list from the .txt file
def create_adj_dict(filepath):
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

# define the function for creating an id to article name mapping
def create_id_mapping(filepath):
    id_mapping = {}

    with open(filepath, "r") as file:
        for line in file:
            # skip lines with only one value
            if len(line.strip().split(" ", 1)) < 2:
                continue
            id, name = line.strip().split(" ", 1)
            id_mapping[int(id)] = name
    return id_mapping

# define the function for saving a dictionary as a pickle file
def save_dict(dict, outputpath):
    # Save adj dict into a pickle file
    with open(outputpath, "wb") as file:
        pickle.dump(dict, file)


# RUNNING THIS FILE TAKES THE ADJACENCY LIST AND IDS TEXT FILES AND CONVERTS THEM TO PICKLE FILES
adj_dict = create_adj_dict("../wiki-topcats.txt")
id_mapping = create_id_mapping("../wiki-topcats-page-names.txt")

save_dict(adj_dict, "../adjacency_list.pkl")
save_dict(id_mapping, "../id_mapping.pkl")