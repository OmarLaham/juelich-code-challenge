import sys
from utils import exitWithCode
from graph import Graph


def main() -> int:
	"""The main function. Checks input and prints the solution to the stdout"""

	# Check the input arguments and print them to stdout

	# Check if both adjacency matrix and the root node are provided
	if len(sys.argv) != 3:
		exitWithCode("Error: You must provide adjacency matrix and the root node as parameters. Terminated.")

	adj_matrix = sys.argv[1]
	root_node = sys.argv[2]

	# Check if root_node is a valid int
	try:
		root_node = int(root_node)
	except:
		exitWithCode("Error: You must provide an int value for the root node parameter. Terminated")

	# Check if root_node >= 1
	if root_node < 0:
		exitWithCode("Error: Root node must be >= 1. Terminated")


	# Create an instance of Graph obj and initialize it with adj_matrix and root_node
	print("Creating graph using passed parameters..")
	g = Graph(adj_matrix, root_node)

	# Check if g is DAG
	if not g.isDAG():
		exitWithCode("Error: The graph must be a directed a cyclic graph. Please provide a correct adjacency matrix that represents a DAG. Terminated.")

	# Solve
	print("Solving..")
	solution = g.shortestPathTopologicalSorting()

	# Print the solution
	for i in range(len(solution)):
		print("{0} -> {1}:\t Distance: {2}\t Path: {3}".format(g.root_node, solution[i][0], solution[i][1],
															   solution[i][2]))
	
	return 0





if __name__ == '__main__':
	# Return value of main is passed into sys.exit()
    sys.exit(main())
