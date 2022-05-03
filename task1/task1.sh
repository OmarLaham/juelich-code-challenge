#!/bin/bash

################################################################################
# Help                                                                         #
################################################################################
Help()
{
   # Display Help
   echo "Finds the shortest paths from the root node to all other nodes in a directeed acyclic graph (DAG)."
   echo
   echo "Syntax: ./task1.sh [adjacency_matrix] [root_node]"
   echo "options:"
   echo "adacency_matrix: The adjacency matrix that represents your DAG. E.g. \"0,1,1|0,0,1|0,0,0\", where | separates rows and , separates cells."
   echo "root_node: The number of the root node [0, n_nodes-1]."
   echo
}

################################################################################
# Process the input options. Add options as needed.                            #
################################################################################
# Get the options
while getopts ":h" option; do
   case $option in
      h) # display Help
         Help
         exit;;
   esac
done

################################################################################
# Main program                                                                 #
################################################################################

# Run task1 and pass parameters
# $1 represents adjacency matrix
# $2 represents root node
python task1.py $1 $2
