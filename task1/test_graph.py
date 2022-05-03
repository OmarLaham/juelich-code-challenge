# Test file for Graph class


from graph import Graph
import pytest
import sys

def main() -> int:
	"""The main function. Runs multiple defined test functions"""

	# Creat a cyclic graph and check if if it's a DAG
	# The following string represents an adjacency matrix for a cyclic graph (NOT DAG):
	# cyclic_adj_matrix = [
	# 	[0, 1, 1, 0, 0, 0],
	# 	[0, 0, 1, 1, 0, 0],
	# 	[0, 0, 0, 1, 1, 1],
	# 	[0, 0, 0, 0, 1, 0],
	# 	[0, 0, 0, 0, 0, 1],
	# 	[1, 0, 0, 0, 0, 0]
	# ]
	cyclic_adj_matrix = "0,1,1,0,0,0|0,0,1,1,0,0|0,0,0,1,1,1|0,0,0,0,1,0|0,0,0,0,0,1|1,0,0,0,0,0"
	g = Graph(cyclic_adj_matrix, 0)
	assert g.isDAG() == False
	print("Passed the 'cyclic NOT DAG' test successfully!")

	del g

	# Creat an undirected graph and check if if it's a DAG
	# The following string represents an adjacency matrix for an undirected graph (NOT DAG):
	# undirected_adj_matrix = [
	# 	[0, 1, 1, 0, 0, 0],
	# 	[0, 0, 1, 1, 0, 0],
	# 	[0, 0, 0, 1, 1, 1],
	# 	[0, 0, 0, 0, 1, 0],
	# 	[0, 0, 0, 0, 0, 1],
	# 	[0, 0, 0, 0, 0, 0]
	# ]
	undirected_adj_matrix = "0,1,1,0,0,0|1,0,1,1,0,0|0,0,0,1,1,1|0,0,0,0,1,0|0,0,0,0,0,1|0,0,0,0,0,0"
	g = Graph(cyclic_adj_matrix, 0)
	assert g.isDAG() == False
	print("Passed the 'undirected NOT DAG' test successfully!")

	del g

	# Creat a DAG graph and check if it's a DAG
	# The following string represents this adjacency matrix:
	# dag_adj_matrix = [
	# 	[0, 1, 1, 0, 0, 0],
	# 	[0, 0, 1, 1, 0, 0],
	# 	[0, 0, 0, 1, 1, 1],
	# 	[0, 0, 0, 0, 1, 0],
	# 	[0, 0, 0, 0, 0, 1],
	# 	[0, 0, 0, 0, 0, 0]
	# ]
	dag_adj_matrix = "0,1,1,0,0,0|0,0,1,1,0,0|0,0,0,1,1,1|0,0,0,0,1,0|0,0,0,0,0,1|0,0,0,0,0,0"

	g = Graph(dag_adj_matrix, 0)
	assert g.isDAG() == True
	print("Passed the 'is DAG' test successfully!")
    
	# Find shortest path
	solution = g.shortestPathTopologicalSorting()
	correct_solution = [
		(1, 1, "0 -> 1"),
		(2, 1, "0 -> 2"),
		(3, 2, "0 -> 1 -> 3"),
		(4, 2, "0 -> 2 -> 4"),
		(5, 2, "0 -> 2 -> 5"),
	]

	# Must return true
	assert solution == correct_solution
	print("Passed solving shortest path test successfully!")

	# Free resources
	del g

	# Creat a graph
	# dag_adj_matrix = [
	# 	[0, 1, 1, 0, 0, 1],
	# 	[0, 0, 1, 1, 0, 0],
	# 	[0, 0, 0, 1, 1, 1],
	# 	[0, 0, 0, 0, 1, 0],
	# 	[0, 0, 0, 0, 0, 1],
	# 	[0, 0, 0, 0, 0, 0]
	# ]
	dag_adj_matrix = "0,1,1,0,0,1|0,0,1,1,0,0|0,0,0,1,1,1|0,0,0,0,1,0|0,0,0,0,0,1|0,0,0,0,0,0"

	g = Graph(dag_adj_matrix, 0)
	incorrect_solution = [
			(1, 2, "0 -> 2 -> 1"),
			(2, 1, "0 -> 2"),
			(3, 1, "0 -> 3"),
			(4, 2, "0 -> 2 -> 4"),
			(5, 2, "0 -> 2 -> 5"),
		]

	# Must return true because the path from root (0) to (5) is "0 -> 5" not "0 -> 2 -> 5"
	assert solution != incorrect_solution
	print("Passed catching wrong solution for shortest path test successfully!")

	# Free resources
	del g

	return 0


if __name__ == '__main__':
	# Return value of main is passed into sys.exit()
	sys.exit(main())
