import sys, os, time, random, copy
from collections import deque
from tqdm import tqdm
from utils.readUtils import *
from utils.nodeUtils import *

# $1 graph.txt, $2 hospital.txt $3 ratio of hospitals $4 topK
K = int(sys.argv[3])

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
        # distance
        node.breadCrumbs[id] = 0
        searchQueue.append(node)
    return searchQueue, len(searchQueue)

# handle file outputs
os.system('mkdir -p outputs')
os.system(f'echo > outputs/error.txt')
# clean previous result and write header
os.system('printf \'# nodeid|distance|hospitalid\n\' > outputs/result.txt')

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
    print('\t%d\telapsed time: %.2f\tradius: %d\r' % (len(searchQueue), time.time() - then, radius), end = '')
    for _ in searchQueue:
        node = searchQueue.pop(0)
        edges = node.connectedNodes
        for edge in edges:
            connectedNode = graph[edge]
            if connectedNode.checkNode:
                for hospital in node.breadCrumbs.keys():
                    if len(connectedNode.breadCrumbs) == K:
                        connectedNode.checkNode = False
                    elif hospital not in connectedNode.breadCrumbs.keys():
                        connectedNode.breadCrumbs[hospital] = node.breadCrumbs[hospital] + 1
                        searchQueue.append(connectedNode)
                        graph[edge] = connectedNode
print()
timeTaken = f'\'# searching took: {round(time.time() - then, 2)}\n\''
os.system(f'printf %s >> outputs/result.txt' % timeTaken)
print(timeTaken)

then = time.time()
print('writing to outputs/result.txt')
with open('outputs/result.txt', 'a') as file:
    lines = ''
    for _, node in tqdm(graph.items()):
        for hospital, distance in node.breadCrumbs.items():
            line = f'{node.id}|{distance}|{hospital}\n'
            lines += line
    timeTaken = f'# writing to outputs/result.txt took: {round(time.time() - then, 2)}\n'
    lines += timeTaken
    print(timeTaken)

    timeTaken = f'# total time taken: {round(time.time() - total, 2)}'
    lines += timeTaken
    file.write(lines)
    print(timeTaken)
