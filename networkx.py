import networkx as nx
import json 
import re
from networkx import *



g = nx.Graph()
data = ""
node_1 = []
node_2 = []
edge_weight = []  # node for weight 
node_s = []   # node for node 1
node_m = []   #  node for node 2

with open ("CE-LC.txt", "r") as myfile:
    data=myfile.readlines()
	
for nodein in data:
		node_1.append(nodein.split(" "))


for ns in node_1:
	for nn in ns:
		nn.split("\t")
		nn.split(" ")
		nn.split("\t")
		node_2.append(nn)

slices = []

for nn in node_2:
	slices.append(nn.split("\t"))
	
for ss in slices:
	node_s.append(ss[0])
	
for i in range(len(slices) - 1):
	node_s.append(slices[i][0])
	node_m.append(slices[i][1])
	edge_weight.append(slices[i][2].rstrip())
	







