'''
From ChatGPT: https://chatgpt.com/c/ff85633b-74bf-4716-9590-0234aceb9b0c
'''

from collections import defaultdict, deque
import copy

def countDelayedFlights(flight_nodes, flight_from, flight_to, delayed):
    # Step 1: Create adjacency list for the graph
    graph = defaultdict(list)
    for frm, to in zip(flight_from, flight_to):
        graph[to].append(frm)
    
    # Step 2: Set to keep track of delayed flights
    delayed_flights = set(delayed)
    queue = deque(delayed)
    initial = copy.deepcopy(delayed_flights)
    
    def dfs(flight):
        for nei in graph[flight]:
            if nei not in delayed_flights:
                delayed_flights.add(nei)
                dfs(nei)
    
    for i in initial:
        dfs(i)

    
    # Step 4: Convert the set to a sorted list
    result = sorted(delayed_flights)
    
    return result

# Example usage:
flight_nodes = 4
flight_from = [4, 3]
flight_to = [1, 2]
delayed = [1, 3]

# Test Case 2:
# flight_nodes = 4
# flight_from = [1, 2, 3, 1]
# flight_to = [4, 1, 2, 3]
# delayed = [1]

print(countDelayedFlights(flight_nodes, flight_from, flight_to, delayed))
# Output should be [1, 3, 4]
