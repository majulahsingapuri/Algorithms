import sys, collections
from tqdm import tqdm

def readGraph(filepath):
    with open(filepath, 'r') as file:
        print('reading graph')
        lines = file.readlines()
    data = {}
    for line in tqdm(lines):
        if line.startswith('#'):
            continue
        if ' ' not in line:
            id, connectedNode = [int(x) for x in line.split('\t')]
        else:
            id, connectedNode = [int(x) for x in line.split(' ')]
        try: # append to array
            data[id].append(connectedNode)
        except: # if array doesnt exist, init and add connectedNode
            data[id] = [connectedNode]

    print('sorting')
    data = collections.OrderedDict(sorted(data.items()))

    return data

def readHospital(filepath):
    with open(filepath, 'r') as file:
        print('reading hospital')
        return [int(x) for x in file.readlines() if not x.startswith('#')]
