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

start =11
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

with open('level0_output.json', 'w') as output_file:
    json.dump(output, output_file)

#-------


with open('Input data/level1a.json') as file:
    data = json.load(file)
neighbourhoods = data['neighbourhoods']
distances = [neighbourhoods[key]['distances'] for key in neighbourhoods]
order_quantity = [neighbourhoods[key]['order_quantity'] for key in neighbourhoods]
vehicle_capacity = data['vehicles']['v0']['capacity']

neighborhood_capacities = [int(qty) if qty != "INF" else float('inf') for qty in order_quantity]

routes = []
current_route = ["r0"]  
print(neighborhood_capacities,vehicle_capacity)
graph = []

for i in range(len(distances)):
    graph.append({'visited': 0, 'neighbours': distances[i]})

start =11
visited = 1
path = [start]
min_dist = float('inf')
list1=[]
cap1=110
while visited < len(distances):
    min_neighbour = None
    min_dist = float('inf')

    graph[start]['visited'] = 1

    for i, distance in enumerate(graph[start]['neighbours']):
        if graph[i]['visited'] == 0 and distance != 'Inf' and distance < min_dist:
            min_dist = distance
            min_neighbour = i
            #print(min_neighbour)


    if min_neighbour is not None:
        if cap1+neighborhood_capacities[min_neighbour]>=600:
            list1.append(path)
            print("----------",cap1,neighborhood_capacities[min_neighbour])
            path=[]
            cap1=0
        else:
            cap1+=neighborhood_capacities[min_neighbour]
            path.append(min_neighbour)
            print
            print(cap1,neighborhood_capacities[min_neighbour],min_neighbour)
            start = min_neighbour
            visited += 1
    else:
        start = path[visited - 1]
list1.append(path)
output1 = {"v0": {"path1": ["r0"] + [f"n{index}" for index in list1[0]] + ["r0"], "path2": ["r0"] + [f"n{index}" for index in list1[1]] + ["r0"], "path3": ["r0"] + [f"n{index}" for index in list1[2]] + ["r0"]}}#, "path4": ["r0"] + [f"n{index}" for index in list1[3]] + ["r0"]}}
print(list1)
print(output1)
#print(min_neighbour)
