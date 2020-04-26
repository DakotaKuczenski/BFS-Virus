import networkx as nx 
import pandas as pd 
import matplotlib.pyplot as plt
from google.colab import files
import time

nodes = pd.read_csv('/content/nodes.csv', header = None )
mapping = pd.read_csv('/content/mappings.csv', header = None )
g = nx.Graph()          # creates the graph 
start = ['Three Rivers']  # start from 
citylist = []           # list of every city 
vac = []





def addcity():
  i = 0 
  for index in nodes.iterrows():
    city = nodes[0][i]
    y = nodes[1][i]
    x = nodes[2][i]
    g.add_node(city, pos=(x, y))
    pos = nx.get_node_attributes(g,'pos')
    citylist.append(city)
    nx.draw(g, pos,  with_labels = True)
    i+=1 
  mappin(pos)
  

def mappin(pos):
  k = 0 
  for x in mapping.iterrows():
    a = mapping[0][k]
    b = mapping[1][k]
    w = mapping[2][k]
    g.add_edge(a, b, weight=w)
    nx.draw(g, pos,  with_labels = True)
    k+=1
    value = [w, 'false']
  spread()


def spread():                     # loop thru all three starting points  
  for j in start:                 
    ordr = []   
    dist = 0            
    ordr.append(j)
    record = {}
    record[j] = [0, False]
    pathfinder(ordr, record, dist)


def pathfinder(ordr, record, dist):
  dist = 0 
  for w in ordr:
    s = record.get(w)
    if s[1] == False:                     # if hasnt been visited  
      pt = g.edges(w, data = 'weight')    # pt is a list
      for i in pt:                        # for tuples in that list
        srt = i[0]
        end = i[1]
        weit = i[2] + s[0]        
        if end not in ordr:
          ordr.append(end)
          record.update({end: [weit, False]})
  x = sorted(record.items(), key=lambda x: x[1])
  ouputs(record, ordr, x)


def ouputs(record, ordr, x):
  
  cc = 0
  gg = 0
  tr = 0
  
  for k in x:
    
    if k[0] == "Three Rivers" and tr == 0:
      print("Outbreak in Three Rivers")
      for i in x:
        print(i[0])
      print(' ')
      tr = 1

if __name__ == "__main__":
  addcity()
  global i
  global k
  global g  
  spd = 25        # speed the virus travels 


