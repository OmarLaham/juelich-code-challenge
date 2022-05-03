#!/bin/bash

################################################################################
# Help                                                                         #
################################################################################
Help()
{
   # Display Help
   echo "Runs some tests to make sure that the Graph class works correctly as a part of the Test Driven Development (TDD) process."
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

# Create a virtual environment for our modules
python3 -m venv task1-env

# Activate our virtual environment
. task1-env/bin/activate 

# Upgrade pip
pip install --upgrade pip 

# Install requirements
pip install -r test_requirements.txt

# Run task1 and pass parameters
# $1 represents adjacency matrix
# $2 represents root node
python test_graph.py
