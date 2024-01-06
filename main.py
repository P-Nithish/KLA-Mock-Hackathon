import json
import networkx as nx

with open('Input data/level0.json') as file:
    data = json.load(file)

neighbourhoods = data['neighbourhoods']

distances = []

for key in neighbourhoods:
    distance = neighbourhoods[key]['distances']
    distances.append(distance)

for i in range(len(distances)):
    zero = distances[i].index(0)
    distances[i] = distances[i][:zero] + ['Inf'] + distances[i][zero + 1:]

graph = []

for i in range(len(distances)):
    graph.append({'visited': 0, 'neighbours': distances[i]})

start = 13
visited = 1
path = [start]
min_dist = float('inf')

while visited < len(distances):
    min_neighbour = None
    min_dist = float('inf')

    graph[start]['visited'] = 1

    for i, distance in enumerate(graph[start]['neighbours']):
        if graph[i]['visited'] == 0 and distance != 'Inf' and distance < min_dist:
            min_dist = distance
            min_neighbour = i

    if min_neighbour is not None:
        path.append(min_neighbour)
        start = min_neighbour
        visited += 1
    else:
        start = path[visited - 1]

output = {"v0": {"path": ["r0"] + [f"n{index}" for index in path] + ["r0"]}}

#with open('level0_output.json', 'w') as output_file:
#    json.dump(output, output_file)







import networkx as nx
with open('Input data/level1a.json') as file:
    data = json.load(file)

neighbourhoods = data['neighbourhoods']

order_quantity=[]

for key in neighbourhoods:
    order = neighbourhoods[key]['order_quantity']
    order_quantity.append(order)
print(order_quantity)


vehicle_capacity = neighbourhoods['v0']['capacity']
print(vehicle_capacity)
'''
neighborhood_capacities = [int(qty) if qty != "INF" else float('inf') for qty in order_quantities]

# Create a graph
G = nx.Graph()

# Add nodes (neighborhoods) and the restaurant
G.add_node("r0")  # Restaurant
for i in range(len(distances)):
    G.add_node(f"n{i}")

# Add edges with weights (distances)
for i in range(len(distances)):
    G.add_edge("r0", f"n{i}", weight=distances[i][0])  # Edge from restaurant to neighborhood
    for j in range(len(distances[i])):
        G.add_edge(f"n{i}", f"n{j}", weight=distances[i][j])  # Edge between neighborhoods

# Function to find the minimum paths satisfying the constraints
def find_paths():
    paths = []
    remaining_orders = neighborhood_capacities.copy()
    current_capacity = vehicle_capacity
    
    while any(order > 0 for order in remaining_orders):
        path = ["r0"]
        current_capacity = vehicle_capacity
        
        for i, order in enumerate(remaining_orders):
            if order > 0 and current_capacity >= order:
                path.append(f"n{i}")
                current_capacity -= order
                remaining_orders[i] = 0 if order != float('inf') else float('inf')
        
        path.append("r0")
        paths.append(path)
    
    return paths

# Find the minimum paths to satisfy orders
minimum_paths = find_paths()

# Format the output
output = {"v0": {f"path{i+1}": path for i, path in enumerate(minimum_paths)}}
print(output)


'''