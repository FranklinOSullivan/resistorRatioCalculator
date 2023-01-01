# Python calculator to find the closest possible resistor pair to a given input resistance

# Using some inital values of mine to test function
resistorValues = [0, 10, 22, 47, 100, 150, 200, 220, 270, 330, 470,
                  510, 680, 1000, 2000, 2200, 3300, 4700, 5100, 6800, 10000]


# Function to find the best series combination
def findSeriesComb(inputVal):
    # Predefine array values
    currentBestComb = [0, 0]
    currentComb = [0, 0]
    # Loop through to find the closest value
    for i in resistorValues:
        for j in resistorValues:
            currentComb = [i, j]
            currentBestComb = compareValues(
                currentBestComb, currentComb, inputVal)
    return currentBestComb


def findParallelComb(inputVal):
    return


def compareValues(val1, val2, expectedVal):
    # Get the numerical values
    num1 = val1[0] + val1[1]
    num2 = val2[0] + val2[1]
    # Find the smaller distance to the expected val
    dist1 = abs(expectedVal - num1)
    dist2 = abs(expectedVal - num2)
    # Based on the distance, return the best combination
    if dist1 < dist2:
        return val1
    else:
        return val2


# Function the find the variation between the values
def findVariation(givenVal, expectedVal):
    return ((givenVal[0] + givenVal[1])/expectedVal)*100


wantedVal = int(
    input("What value would you like to find the closest match to? "))


# Find the series value
seriesPair = findSeriesComb(wantedVal)
print(seriesPair)
print("Variation: ", findVariation(seriesPair, wantedVal), "%")
