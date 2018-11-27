import networkx as nx 
import json 
import re

data = ""
with open ("test.txt", "r") as myfile:
    data=myfile.readlines()

	
values = []
d = str(data)
d.split(',')


print(len(data))
