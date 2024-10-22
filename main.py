# This is an evaluation to test basic data science and engineering skills.
# There are three parts to this evaluation: 1. Reading in data and formatting it,
# 2. Iterating through data and creating a network, and 3. Implementing a function
# that lists all destinations from a given airport. The first two sections are within
# the main.py file, and the third section is within the graph.py file. We are looking
# for the knowledge of data manipulation, object-oriented programming, and
# algorithm design. You have 1 hour and you are allowed to use the internet.
# This evaluation was tested using Python 3.9.7 and pandas==2.2.1. Other versions
# are allowed as long as it's Python 3. Good luck!

# Import packages
import pandas as pd
import numpy as np # Not necessary for this evaluation
from graph import Airport, Flight, Network

# TODO: Section 1: Data Manipulation
# Given set of airlines

# Read in routes.csv provided to you

# Rename 'destination apirport' column name to 'destination airport'

# Drop 'codeshare' column

# Drop rows with nan or null values

# Filter out airlines not in airline_set

# Convert 'source airport id' and 'destination airport id' to int

# Convert 'destination airport id' to int

# Print dataframe



# TODO: Section 2: Create Network
# Iterate through dataframe and create network given definitions in graph.py.
# Use the columns: 'source airport', 'source airport id', 'destination airport',
# 'destination airport id', and 'equipment'. Add each airport from source and 
# destination only once (the airport id should be used to check).
# Add each flight to the network.



# TODO: Section 3 (continued): List all destinations from a given airport.
# Remember to fill out the function definition at the end of graph.py.
# Print all destinations from airport AER, id 2965