# Class defining an airport
class Airport:
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id

    def __str__(self):
        return self.name

# Class defining a flight
class Flight:
    def __init__(self, source: Airport, destination: Airport, equipment: str):
        self.source = source
        self.destination = destination
        self.equipment = equipment

    def __str__(self):
        return f"{str(self.source)} -> {str(self.destination)} ({self.equipment})"

# Class defining a network of airports and flights
class Network:
    def __init__(self, airports: set[Airport] = set(), flights: set[Flight] = set()):
        self.airports = airports
        self.flights = flights

    def __str__(self):
        return f"Network with {len(self.airports)} airports and {len(self.flights)} flights."

    def add_airport(self, airport: Airport):
        self.airports.add(airport)

    def add_flight(self, flight: Flight):
        self.flights.add(flight)

    # TODO: Section 3: List all destinations from a given airport
    # Given an airport, return all the destinations that can be reached from it.
    # Return the list of destination airport names only.
    # This includes all the destinations that can be reached by taking one or more
    # flights. For example, if there is a flight from A to B and another flight
    # from B to C, then list both B and C as destinations. Remember to add a print
    # statement at the bottom of main.py calling this function.
    def list_all_dest(self, source: Airport) -> set[str]:
        visited = set()
        to_visit = [source] # We'll use our source airport as the first node
        # I am going to do a node search algorithm, this will consist on check for nodes next to our airport of interest
        # and then check if the next airport has another destinations as well
        while to_visit:
            current_airport = to_visit.pop()
            for flight in self.flights:
                if flight.source == current_airport and flight.destination not in visited:
                    visited.add(flight.destination)
                    to_visit.append(flight.destination)

        return set(airport.name for airport in visited)