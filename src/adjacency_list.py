import pickle # we will use the pickle module to store the dictionary in a pickle file

adj_dict = {}

# iterate through the edge list to add values to the dictionary
with open("../wiki-topcats.txt", "r") as edge_list:
    for line in edge_list:
        id = int(line.split()[0])
        edge = int(line.split()[1])

        # check if there is already a set at the given id
        if id in adj_dict:
            adj_dict[id].add(edge)
        else:
            adj_dict[id] = {edge}

# now that we have our dictionary, we can save it into a pickle file
with open("../adjacency_list.pkl", "wb") as adj_list:
    pickle.dump(adj_dict, adj_list)