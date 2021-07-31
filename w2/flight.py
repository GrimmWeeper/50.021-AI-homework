import search

# PART 1: State
# A good choice will be current city and current time (State = tuple type: (city, time))

class Flight:
    def __init__(self, start_city, start_time, end_city, end_time):
        self.start_city = start_city
        self.start_time = start_time
        self.end_city = end_city
        self.end_time = end_time
        
    def __str__(self):
        return str((self.start_city, self.start_time)) + ' -> ' + str((self.end_city, self.end_time))
        
    __repr__ = __str__

    
    # PART 2: MATCHES
    def matches(self, city, time):
        if city == self.start_city and time <= self.start_time:
            return True
        else:
            return False


flightDB = [Flight('Rome', 1, 'Paris', 4),
    Flight('Rome', 3, 'Madrid', 5),
    Flight('Rome', 5, 'Istanbul', 10),
    Flight('Paris', 2, 'London', 4),
    Flight('Paris', 5, 'Oslo', 7),
    Flight('Paris', 5, 'Istanbul', 9),
    Flight('Madrid', 7, 'Rabat', 10),
    Flight('Madrid', 8, 'London', 10),
    Flight('Istanbul', 10, 'Constantinople', 10)]


class FlightProblem(search.Problem):

    # State = tuple type: (city, time)
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal = goal)

    def actions(self, state):
        actionList = []
        for flight in flightDB:
            if flight.matches(state[0], state[1]):
                actionList.append(flight)
        return actionList


    def result(self, state, action):
        return (action.end_city, action.end_time)

    def goal_test(self, state):
        if state[0] == self.goal[0] and state[1] <= self.goal[1]:
            return True
        else:
            return False

    def path_cost(self, c, state1, action, state2):
        return c + (state2[1] - state1[1])


# PART 3: FLIGHT ITINERARY
def find_itinerary(start_city, start_time, end_city, deadline):
    initialState = (start_city,start_time)
    endState = (end_city, deadline)
    try:
        path = search.uniform_cost_search(FlightProblem(initialState, endState)).path()
    except:
        return 'NO AVAILABLE PATH'

    return path


# PART 4

# Yes. In my implementation of find_itinerary(), it will output the path available to reach destination.
# If no path is available, it will not return a path. Hence, increasing the time 1 by 1 would mean the first path available is the shortest path.

# 2x

def find_shortest_itinerary(start_city, end_city):
    deadline = 1
    isNotPath = True
    while isNotPath:
        path = find_itinerary(start_city, 1, end_city, deadline)
        if path != 'NO AVAILABLE PATH':
            isNotPath = False
            return path
        deadline += 1


if __name__ == '__main__':
    print(find_itinerary('Rome',1,'Constantinople',10))
    print(find_itinerary('Paris',2,'Madrid',8))
    print(find_itinerary('Paris',2,'Constantinople',10))
    print(find_itinerary('Paris',2,'Constantinople',8))

    print(find_shortest_itinerary("Rome", "Istanbul"))