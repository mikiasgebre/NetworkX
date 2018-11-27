Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import networkx as nx
>>> G = nx.Graph()
>>> from networkx import *
>>> import json
>>> import re

>>> data = ""
>>> node_1 = []
>>> node_2 = []
>>> edge_weight = []
>>> node_s = []
>>> node_m = []
>>> 
>>> with open ("CE-LC.txt", "r") as myfile:
	data = myfile.readlines()

	
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    with open ("CE-LC.txt", "r") as myfile:
FileNotFoundError: [Errno 2] No such file or directory: 'CE-LC.txt'
>>> 
