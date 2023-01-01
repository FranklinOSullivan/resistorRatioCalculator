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
    # If either of the values are exactly correct
    if val1 == expectedVal:
        return val1
    elif val2 == expectedVal:
        return val2
    # If both values are less
    elif (val1 < expectedVal and val2 < expectedVal):
        # Find closest
        if (val1 > val2):
            return val1
        else:
            return val2
    # If both are greater than the expected
    elif (val1 > expectedVal)


wantedVal = input("What value would you like to find the closest match to? ")


# Find the series value
seriesPair = findSeriesComb(wantedVal)
