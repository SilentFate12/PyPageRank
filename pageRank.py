# -*- coding: utf-8 -*-
"""
Created on Sat May 14 19:39:36 2022

@author: Edward
"""
import os;

def pageRank(damp, Nodes, connections):
    finalRanks = []
    size_factor = (1 - damp) / len(Nodes) # (1 - d)/N
    for node in Nodes:
        sumOf = 0
        for con in connections: #Getting all incoming connections
            if con[1] == node[0]: #checking if any connections go to our current node
                sumOf += Nodes[con[0] - 1][1] / Nodes[con[0] - 1][2] #PageRank / Outgoing Num of Edges
        
        nodeRank =  size_factor + damp * sumOf #(1 - d)/N + d * (PR(a1)/O(a1) + PR(a2)/O(a2) + ... + PR(aN)/O(aN))
        finalRanks.append(nodeRank)
        
    return finalRanks
        

damp = 0.7
Nodes = [[1, 1, 1], [2, 1, 2], [3, 1, 1], [4, 1, 1], [5, 1, 1]] #Format is [Node #, PageRank, outgoingCount]
connections = [(1, 2), (2, 3), (2, 5), (3, 1), (4, 5), (5, 5)] #Format is (Going from node, Coming to node)
currentRanks = pageRank(damp, Nodes, connections)
notConverged = True
numOfIterations = 1
while notConverged:
    sumOfRanks = 0
    for rank in currentRanks:
        sumOfRanks += rank
    if sumOfRanks <= 1.0001:
        notConverged = False
    else:
        for idx, node in enumerate(Nodes):
            node[1] = currentRanks[idx]
        numOfIterations += 1
        currentRanks = pageRank(damp, Nodes, connections)

print ("Final ranking is: " + str(currentRanks))
print ("Number of iterations needed: " + str(numOfIterations))
os.system("pause");
