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

def data_etl(data_path):
    # Read in routes.csv provided to you
    df = pd.read_csv(data_path)
    routes = df.copy() 
    # Rename 'destination apirport' column name to 'destination airport'
    routes = routes.rename(columns={'destination apirport':'destination airport'})
    # Drop 'codeshare' column
    routes = routes.drop(columns=['codeshare'])
    # Drop rows with nan or null values
    routes = routes.dropna(axis=0)
    # Filter out airlines not in airline_set
    airline_set = set(routes['airline']) # I'm assuming this is the airline_set, but can be defined elsewhere
    routes = df[df['airline'].isin(airline_set)]
    # Convert 'source airport id' and 'destination airport id' to int
    routes['source airport id'] = routes['source airport id'].astype(int)
    # Convert 'destination airport id' to int
    routes['destination airport id'] = routes['destination airport id'].astype(int)
    # Print dataframe
    print(routes)
    return(routes)


# TODO: Section 2: Create Network
# Iterate through dataframe and create network given definitions in graph.py.
# Use the columns: 'source airport', 'source airport id', 'destination airport',
# 'destination airport id', and 'equipment'. Add each airport from source and 
# destination only once (the airport id should be used to check).
# Add each flight to the network.

def make_routes_network(routes_df):
    # Create the Network object as clear template
    network = Network()

    # I'll use this dictionary to store all airports (from source to dest)
    airport_dict = {}
    # I'll search line by line
    for k, row in routes_df.iterrows():
        print(f'iteration: {k} of {routes_df.shape[0]}') # I could use tqdm to print status instead
        # these variables are stored temporarly
        source_airport = row['source airport']
        source_id = row['source airport id']
        dest_airport = row['destination airport']
        dest_id = row['destination airport id']
        equipment = row['equipment']

        # Create source and destination airports if they don't exist in the dictionary already
        if source_id not in airport_dict:
            source = Airport(source_airport, source_id)
            network.add_airport(source)
            airport_dict[source_id] = source
        else:
            source = airport_dict[source_id]

        if dest_id not in airport_dict:
            destination = Airport(dest_airport, dest_id)
            network.add_airport(destination)
            airport_dict[dest_id] = destination
        else:
            destination = airport_dict[dest_id]

        # make flights between sources and destination
        flight = Flight(source, destination, equipment)
        network.add_flight(flight) # adding a flight

    return network

# TODO: Section 3 (continued): List all destinations from a given airport.
# Remember to fill out the function definition at the end of graph.py.
# Print all destinations from airport AER, id 2965

def list_destinations_from_source_id(source_search_id):

    source_airport = next(airport for airport in network.airports if airport.id == source_search_id)
    # List and print all destinations from the source airport AER
    destinations = network.list_all_dest(source_airport)
    print(f"Airport destinations, from: {source_airport.name} to: {', '.join(destinations)}")

if __name__ == '__main__':
    airport_search_id = 2965
    data_path = 'data/routes.csv'
    # SECTION 1
    routes = data_etl(data_path)
    # SECTION 2
    network = make_routes_network(routes)
    # SECTION 3
    list_destinations_from_source_id(airport_search_id)