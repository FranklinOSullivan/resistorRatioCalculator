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
            currentBestComb = compareValuesSeries(
                currentBestComb, currentComb, inputVal)
    return currentBestComb, currentBestComb[0] + currentBestComb[1]


def findParallelComb(inputVal):
    # Predefine array values
    currentBestComb = [0, 0]
    currentComb = [0, 0]
    # Loop to find the best values
    for i in resistorValues:
        for j in resistorValues:
            currentComb = [i, j]
            currentBestComb = compareValuesParallel(
                currentBestComb, currentComb, inputVal)
    return currentBestComb, (1/(1/currentBestComb[0])+(1/currentBestComb[1]))


# Find the series values
def compareValuesSeries(val1, val2, expectedVal):
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


# Find the parallel values
def compareValuesParallel(val1, val2, expectedVal):
    # Get the numerical values
    num1 = (1/(1/val1[0]) + (1/val1[1]))
    num2 = (1/(1/val2[0]) + (1/val2[1]))
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
    return (givenVal/expectedVal)*100


wantedVal = int(
    input("What value would you like to find the closest match to? "))


# Find the series value
seriesPair, seriesValue = findSeriesComb(wantedVal)
print("In series: ", seriesPair, ", ", seriesValue, "Ohms")
print("Variation: ", findVariation(seriesValue, wantedVal), "%")

# Find the parallel value
parallelPair, parallelValue = findParallelComb(wantedVal)
print("In parallel: ", parallelPair, ", ", parallelValue, "Ohms")
print("Variation ", findVariation(parallelValue, wantedVal), "%")
