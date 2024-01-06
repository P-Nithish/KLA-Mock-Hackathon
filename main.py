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

# Format the output
output = {"v0": {f"path{i+1}": path for i, path in enumerate(minimum_paths)}}
print(output)


'''
