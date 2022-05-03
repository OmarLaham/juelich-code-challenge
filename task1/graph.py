# Python program that uses topologicall sorting
# to find shortest pathes from root node to all nodes
# in a graph represented by adjacency matrix

from utils import exitWithCode
from collections import defaultdict
 
#Class to represent a graph
class Graph:

	""" Initialize the graph using adjacency matrix, n_nodes (NO. of nodes) and the root node """
	def __init__(self, adj_matrix, root_node) -> None:
		# Number of nodes in the graph. Init with 0 and fill after checking input format
		self.n_nodes = 0
		# Number of root node in [1,n_nodes]
		self.root_node = root_node
		# Adjacency list. Will be filled later from adjacency matrix
		self.adj_list = defaultdict(list)
        
		# Check if adj_matrix has a valid adjacency matrix format
		adj_matrix = self.isValidAdjMatrixFormat(adj_matrix, root_node)
		
		if adj_matrix == None:
			exitWithCode("Error: You must provide a valid adjacency matrix. You can use -h for help and information. Terminated")

		# Fill set n_nodes value to the number of nodes in the graph
		self.n_nodes = len(adj_matrix)

		# Check if root_node is a valid int
		try:
			root_node = int(root_node)
		except:
			exitWithCode("Error: You must provide an int value for the root node parameter. Terminated")
			
		# Check if root_node >= 1
		if root_node < 0:
			exitWithCode("Error: Root node must be >= 0. Terminated")
			
		# Check if root_node > self.n_nodes
		if root_node > self.n_nodes - 1:
			exitWithCode("Error: Root node must be between 0 and {0}".format(self.n_nodes - 1))

		# Print adj_matrix to stdout
		print("Adjacency matrix:")
		for i in range(len(adj_matrix)):
			print(adj_matrix[i])
			
		# Print root_node to stdout
		print("Root node: {0}".format(root_node))
        
		# Use adj_matrix to create "adj_list" dict
		for i in range(len(adj_matrix)):
			for j in range(len(adj_matrix[i])):
				if adj_matrix[i][j] == 1:
					self.addEdge(i, j)


	""" Check if the passed adjacency matrix format is a valid one. If yes return edges after formating as a list of tuples """
	def isValidAdjMatrixFormat(self, adj_matrix, root_node) -> list:

		# Format passed adj_matrix into a list of lists
		adj_matrix = adj_matrix.split("|") # We use "|" as a row separator
		
		for i in range(len(adj_matrix)):
			adj_matrix[i] = adj_matrix[i].split(",") # We use "," as a matrix cell separator
			
			# Check if nrows == ncols after split
			if len(adj_matrix[i]) != len(adj_matrix):
				print("Error: Your adjacency matrix is not a square matrix.")
				return None
			
			# Check if all values are non-negative numbers
			for j in range(len(adj_matrix[i])):
				try:
					adj_matrix[i][j] = int(adj_matrix[i][j])
				except:
					print("Error: You must provide int values for every cell in your adacency matrix.")
					return None
				if adj_matrix[i][j] not in [0,1]:
					print("Error: Adjacency matrix can contain only ones and zeroes.")
					return None
    	
		return adj_matrix


	""" Adds an edge to the graph """
	def addEdge(self,src,dest,weight=1) -> None:
		self.adj_list[src].append((dest,weight))

	""" Prints shortest path from root node to j using parent array """
	def getPath(self, parent, i, steps=[]) -> list:

		# Get the parent of i from parent list
		i_parent = parent[i]

		# If i is the root node
		if i_parent == -1:
			return steps # Stop recursion
		else:
			# Add parent to the beginning of the path as str to join later
			steps.insert(0, str(i_parent))
			# Continue with recursion till you reach the root node
			return self.getPath(parent, parent[i], steps)


	""" A recursive function used by shortestPath """
	def recursiveTopologicalSorting(self, node, visited, stack) -> None:

		# Check if current graph is a DAG
		assert self.isDAG() == True

		# Flag the current node as visited
		visited[node] = True

		# Recur for all the vertices that have edges directed from this node
		# Check if there is any edge that leaves the current node
		if node in self.adj_list.keys():
			# Note: I supported weights in this solution as extra work
			for v, weight in self.adj_list[node]:
				if visited[v] == False:
					self.recursiveTopologicalSorting(v, visited, stack)


		# Add the current node to stack variable that keeps track of the topological sort of the graph
		stack.append(node)

	""" Finds shortest paths from the root node to all other vertices using topological sorting """
	""" Return the solution as a list of list where each child list contains [node_number, distance from root, path]"""
	def shortestPathTopologicalSorting(self) -> list:

		# Flag all nodes as NOT visited as initialization
		visited = [False]*self.n_nodes

		# The stack variable that will keep track of the topological sort of the graph
		stack =[]

		# Call the recursive helper function to store Topological and fill stack variable
		# Use root node as the source
		for i in range(self.n_nodes):

			if visited[i] == False:
				self.recursiveTopologicalSorting(self.root_node,visited,stack)

		# Initialize distances to all vertices as infinite (represents the max distance, before editing by recursive)
		dist = [float("Inf")] * (self.n_nodes)

		# distance of root_node is always 0
		dist[self.root_node] = 0

		# store parent of each node according to shortest path
		parent = [-1] * self.n_nodes

		# Process nodes in topological order

		# While stack is not empty
		while stack:

			# Get the next node from topological order
			i = stack.pop()

			# Update distances of all adjacent vertices
			for node,weight in self.adj_list[i]:
				if dist[node] > dist[i] + weight:
					dist[node] = dist[i] + weight
					#tick
					parent[node] = i


		# Print the solution containing the calculated shortest distances
		solution = []
		for i in range(self.n_nodes):

			# Don't include root node in solution
			if i == self.root_node:
				continue

			node_dist = dist[i] if dist[i] != float("Inf") else "Inf"
			# Get the path from root node. Cast to str to join later
			path_steps = self.getPath(parent, i, steps=[str(i)])
			path = " -> ".join(path_steps)
			# Add solution for each node as a tuple: (node_id, distance, path from root)
			solution.append((i, node_dist, path))

		return solution
      
        
	""" Apply Depth First Search (DFS) recursively on the graph and set the departure time of all nodes of the graph """
	""" Source before modification: https://www.techiedelight.com/check-given-digraph-dag-directed-acyclic-graph-not/ """
	def DFS(self, node, discovered, departure, time) -> int:

		# Flag the current node as discovered
		discovered[node] = True

		# Do for every edge (node, u)
		for u, weight in self.adj_list[node]:
			# if `u` is still not discovered
			if not discovered[u]:
				time = self.DFS(u, discovered, departure, time)

		# ready to backtrack
		# set departure time of node `node`
		departure[node] = time
		time = time + 1

		return time


	""" Returns true if the given directed graph is DAG """
	""" Source before modification: https://www.techiedelight.com/check-given-digraph-dag-directed-acyclic-graph-not/ """
	def isDAG(self) -> bool:

		n = self.n_nodes

		# Stores the discovery state of all nodes
		discovered = [False] * n

		# For all nodes, stores the departure time returned by DFS
		departure = [None] * n

		time = 0

		# Apply DFS from all undiscovered nodes to traverse across all connected nodes of a graph
		for i in range(n):
			if not discovered[i]:
				# Avoid creating empty lists by DFS snice adj_list is a defaultdict(list)
				if i in self.adj_list.keys():
					time = self.DFS(i, discovered, departure, time)

		# Check if the given directed graph is acyclic, then if is a DAG as a result
		for u in range(n):

			# Avoid creating empty lists by DFS snice adj_list is a defaultdict(list)
			if u in self.adj_list.keys():

				# check if (u, v) forms a back-edge.
				for v, weight in self.adj_list[u]:

					# If the departure time of node `v` is greater than equal
					# to the departure time of `u`, they form a back edge.

					# Note that `departure[u]` will be equal to `departure[v]`
					# only if `u = v`, i.e., node contain an edge to itself
					if departure[u] <= departure[v]:
						return False

		# no back edges
		return True
