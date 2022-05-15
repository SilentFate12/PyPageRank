# PyPageRank
A simple python script that calculates the values of PageRank over a system of connected nodes.

In order to use this script, python must already be set up on your device. Go download it [here](https://www.python.org/downloads/) if you don't already have it.

Next, to edit the script you'll need an IDE. I personally use [Spyder](https://www.spyder-ide.org/), but you're free to use any IDE you like.

There are 4 different controls for the script: the Nodes list, the connections list, the dampening factor, and epsilon.

* The Nodes list is a representation of all the nodes in your system. The format is as follows for a single node: [Node #, PageRank, OutgoingEdges]. the PageRank formula requires every node to start at 1, so leave PageRank as 1 for all Nodes you add. OutgoingEdges is simple: it's the number of edges going from the node to another node. And finally, number your nodes in ascending order to keep things neat. Technically you can name your nodes anything and the script will still work (as long as you're consistent with your connections list) but keeping nodes neatly numbered is the best way to guarantee the script to work.
* The connection list is a simple set of tuples representing all the connections in your system. The format is (Outgoing_Node, Incoming_Node). For example, a connection from Node 4 to Node 1 would be (4, 1). Order is irrelevant within the array, just make sure you don't forget any connections.
* The dampening factor is an arbitrary factor that is usually set around 0.7 to 0.85. This helps reduce the numbers, and is generally useful. Don't worry too much about this value, set it to 0.85 or keep it at 0.7 if you'd like.
* Epsilon is the range at which we accept the PageRank system to be properly reduced. This value is actually always 1 + Epsilon, but it's not too important. Just remember that the bigger the range, the less reduced the system will be, and the fewer iterations of PageRank will be run. Consider leaving it as is, or only increasing it by increments of 0.0001.
---
Finally, we can run the script. If you're using Spyder, you can execute it within the IDE without too much trouble, but otherwise you can execute it from the command line. Simply open up a terminal, navigate to the folder where you downloaded the script, and type `python pageRank.py` to start the script. You may have to type `python3 pageRank.py` instead depending on your python version. Otherwise, that's all there is to using this script. Have fun!
