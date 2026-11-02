import json # we will use the json module to store the dictionary in a json file

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

# since json files don't take sets, we need to loop through adj_dict to turn the sets into lists
for key, value in adj_dict.items():
    adj_dict[key] = list(value)

# now that we have our dictionary, we can save it into a json file
with open("../adjacency_list.json", "w") as adj_list:
    json.dump(adj_dict, adj_list, indent = 4)