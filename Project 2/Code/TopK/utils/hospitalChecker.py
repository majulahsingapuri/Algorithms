import sys

# $1 path of hospital file $2 path of results
hospitalPath = sys.argv[1]
resultPath = sys.argv[2]

with open (hospitalPath, 'r') as file:
    hospitalList = [int(x) for x in file.readlines() if not x.startswith('#')]
with open(resultPath, 'r') as file:
    results = [x[:-1] for x in file.readlines() if not x.startswith('#')]

for id in hospitalList:
    print(results[id], sep = '')
