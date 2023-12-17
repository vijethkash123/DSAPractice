'''
Given an integer denoting a total number of wheels, help Amazon Logistics find the number of different ways to choose a fleet of vehicles from an infinite supply of two-wheeled and four-wheeled vehicles such that the group of chosen vehicles has that exact total number of wheels. Two ways of choosing vehicles are considered to be different if and only if they contain different numbers of two-wheeled or four-wheeled vehicles.
For example, if our array wheels = [4,5,6] our return
array would be res = [2, 0, 2]. Case by case, we can
have 1 four-wheel or 2 two-wheel to have 4 wheels.
We cannot have 5 wheels. We can have 1 four-wheel and 1 two-wheel or 3 two-wheel vehicles in the final case.
Function Description
Complete the function chooseFleets in the editor below. The function should return an array of integers representing the answer for each wheelstig.
chooseFleets has the following parameter(s):
wheels[wheels[0]…wheels[n-1]]: an array of integers

Explanation 0:
We must find the number of ways of choosing fleets of vehicles whose total numbers of wheels
correspond to the values in wheels = [6, 3, 2].
• For wheels, = 6, we can choose a fleet with 6 total wheels in two ways:
1. Choose 1 four-wheeled vehicle and 1 two-wheeled vehicle.
2. Choose 3 two-wheeled vehicles.
Thus, we store 2 in index O of our return array.
• There is no way to choose a fleet of vehicles with
exactly wheels, = 3 total wheels because each
vehicle has either two or four wheels, so we store
Oin index 1 of our return array.
• For wheels, = 2, we can only choose 1 two-wheeled vehicle to get a fleet with 2 total wheels.
Thus, we store 1 in index 2 of our return array.
Write code in Python
'''

# Non DP solution:
def chooseFleets(wheels):
    result = []
    for i in range(len(wheels)):
        count = 0  # Number of ways
        x = wheels[i]//2+1 #number of 2 wheelers + 1 because range(3) for wheels[i] = 2 iterates fro  0 to 2
        for j in range(x): # we iterate through number of two wheelers choosed within wheels count for each item in wheels(first loop)
            twowheeled = j 
            fourwheeled = (wheels[i]- (j*2))//4  # checking how many four wheelers we can select after subtracting number of 2 wheelers from available number of wheels and // by 4
            if 2*twowheeled + 4*fourwheeled == wheels[i]:  # check if the combination is valid i.e; chosen two wheels and 4 wheels are in limit of number of wheels
                count += 1
        result.append(count)
    return result

print(chooseFleets([4,3,6]))


# DP solution:
