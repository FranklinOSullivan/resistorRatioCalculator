# Python calculator to find the closest possible resistor pair to a given input resistance

# Using some inital values of mine to test function
resistorValues = [0, 10, 22, 47, 100, 150, 200, 220, 270, 330, 470,
                  510, 680, 1000, 2000, 2200, 3300, 4700, 5100, 6800, 10000]


# Function to find the best series combination
def findSeriesComb(input):
    currentBestVal = 0
    # Loop through to find the closest value
    for i in resistorValues:
        for j in resistorValues:
            currentVal = i+j

    return


def findParallelComb(input):
    return


def compareValues(val1, val2, expectedVal):
    # Find the smaller distance to the expected val
    dist1 = abs(expectedVal - val1)
    dist2 = abs(expectedVal - val2)
    if dist1 < dist2:
        return dist1
    else:
        return dist2


wantedVal = input("What value would you like to find the closest match to? ")


# Find the series value
seriesPair = findSeriesComb(wantedVal)
