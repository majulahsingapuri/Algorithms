import sys, os, time, random
from collections import deque
from tqdm import tqdm
from utils.readUtils import *
from utils.nodeUtils import *

# $1 graph.txt, $2 hospital.txt $3 ratio of hospitals

def initGraph(filepath):
    graph = {}
    ids = []
    for key, value in readGraph(filepath).items():
        node = SNode(key, value)
        graph[key] = node
        ids.append(key)
    return graph, ids

def initHospitals(filepath, graph, ids):
    hospitalList = readHospital(filepath)
    print('initializing hospitals')
    searchQueue = []
    for id in hospitalList:
    # for id in tqdm(hospitalList):
        node = graph[id]
        node.checkNode = False
        node.distance = 0
        searchQueue.append(node)
    return searchQueue, len(searchQueue)

# handle file outputs
os.system('mkdir -p outputs')
os.system(f'echo > outputs/error.txt')
# clean previous result and write header
os.system('printf \'# nodeid|distance|path\n\' > outputs/result.txt')

# Search
then = time.time()
total = then
graph, ids = initGraph(sys.argv[1])
searchQueue, totalHospitals = initHospitals(sys.argv[2], graph, ids)

timeTaken = f'\'# initialization/preprocessing took: {round(time.time() - then, 2)}\n\''
os.system(f'printf %s >> outputs/result.txt' % timeTaken)
print(timeTaken)
then = time.time()
radius = 0

print('beginning searching with increasing radius\nfor every hospital...')
while len(searchQueue) != 0:
    radius += 1
    print('\telapsed time: %.2f\tradius: %d\r' % (time.time() - then, radius), end = '')
    for _ in searchQueue:
        node = searchQueue.pop(0)
        edges = node.connectedNodes
        try:
            for edge in edges:
                connectedNode = graph[edge]
                if connectedNode.checkNode:
                    connectedNode.checkNode = False
                    connectedNode.breadCrumb = node.id # node that leads to nearest hospital
                    connectedNode.distance = node.distance + 1
                    searchQueue.append(connectedNode) # right of searchQueue
                    graph[edge] = connectedNode # update node in the graph
        except Exception as e:
            error = f'\'Error: {e}, nodeID: {node.id}, edge: {edge}\n\''
            os.system(f'printf %s >> outputs/error.txt' % error)
            print(error)
print()
timeTaken = f'\'# searching took: {round(time.time() - then, 2)}\n\''
os.system(f'printf %s >> outputs/result.txt' % timeTaken)
print(timeTaken)

then = time.time()
print('writing to outputs/result.txt')
with open('outputs/result.txt', 'a') as file:
    lines = ''
    for _, node in tqdm(graph.items()):
        path = []
        line = f'{node.id}|{node.distance}|'
        while node.breadCrumb != None:
            path.append(node.breadCrumb)
            node = graph[node.breadCrumb]
        for id in path:
            line += str(id) + ' '
        line += '\n'
        lines += line
    timeTaken = f'# writing to outputs/result.txt took: {round(time.time() - then, 2)}\n'
    lines += timeTaken
    print(timeTaken)

    timeTaken = f'# total time taken: {round(time.time() - total, 2)}'
    lines += timeTaken
    file.write(lines)
    print(timeTaken)
