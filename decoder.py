'''
Step by step:
1. generate qr codes based on input number
2. grab matrices for each qr code
3. search through the matrices at specific pixel locations
4. add truth table to list.
5. generate boolean expressions from each list item
6. add boolean expression to dictionary
7. keep doing this until all the combinations have been found or that the full QR
code matrix has been scanned
'''

import math
from sympy.logic import SOPform, POSform
from sympy import symbols
import itertools
import segno
import numpy as np
import matplotlib.pyplot as plt
import colorcet as cc
import seaborn as sns
import sys
np.set_printoptions(threshold=sys.maxsize)


# Generates binary combinations based on n. example: 00, 01, 10, 11
def generatePossibleCombinations(n):
    return list(itertools.product([0, 1], repeat=n))


# Generates the qr code matrices
def generateQRCodeMatrices(numberOfInputs, version, microBool, error, mask):
    possibleCombinationsList = generatePossibleCombinations(numberOfInputs)
    inputList = []

    for c in possibleCombinationsList:
        string = "".join(str(value) for value in c)
        inputList.append(string)
    string = ""

    qrMatrices = []

    for currentInput in inputList:
        # If not error or mask is given, use the Segno default values. Error == None is tested against as Micro QR code M1
        # doesn't have error code capabilities
        if ((error == "" or error == None) and mask == ""):
            qrcode = segno.make(currentInput, micro=microBool,
                                version=version)

        # Instance where mask is given but error code is not
        elif (error == ""):
            qrcode = segno.make(currentInput, micro=microBool,
                                version=version, mask=mask)

        # Instance where error is given but mask is not, boost_error=False to override default error value
        elif (mask == ""):
            qrcode = segno.make(currentInput, micro=microBool,
                                version=version, error=error, boost_error=False)

        # Both mask and error is given
        else:
            qrcode = segno.make(currentInput, micro=microBool,
                                version=version, error=error, mask=mask, boost_error=False)

        # Uncomment this if you want to save each of the QR codes as images. You will need to fix the path
        # qrcode.save(
        #     f'qrcodes/{numberOfInputs}_input/{version}/QRCode_{currentInput}.png', scale=6, border=0)

        print("\nversion: ", version, "currentInput: ", currentInput, "error code: ",
              qrcode.error, "mask: ", qrcode.mask)

        qrMatrices.append(np.asarray(qrcode.matrix))

    return qrMatrices


# Generates truth tables using pixels from each qr matrix
def generateTruthTablesFromQRMatrix(matrixList):
    currentTruthTable = []
    truthTables = []
    qrWidth = len(matrixList[0])
    qrHeight = len(matrixList[0])

    for x in range(0, qrWidth):
        for y in range(0, qrHeight):
            for currentMatrix in matrixList:
                currentTruthTable.append(currentMatrix[x][y])
            truthTables.append(currentTruthTable)
            currentTruthTable = []
    return truthTables


# Converts a binary string to a Boolean expression
def decodeBinaryToBooleanExpression(truthString):
    # We are using log base 2 to get the number of inputs based on the truth string
    numberOfSymbols = int(math.log(len(truthString), 2))
    inputs = generatePossibleCombinations(numberOfSymbols)

    inputLabels = []
    for i in range(numberOfSymbols):
        # Get ASCII value starting from A, B etc
        inputLabels.append(chr(i + 65))
        # Convert ASCII to string
        inputLabelStringForm = " ".join(inputLabels)
    # Turn strings into SymPy.symbols
    symbolLetters = symbols(inputLabelStringForm)

    # Converting from List of Tuples to List of Lists
    listOfInputs = [list(element) for element in inputs]

    minterms = []
    j = 0
    # Example: if truth string = 1010
    for t in truthString:
        if t == 1:
            # minterms would be = [[0,0],[1,0]]
            minterms.append(listOfInputs[j])
        j += 1
    # Bool expression would be = ~B

    booleanExpression = (POSform(symbolLetters, minterms, dontcares=None))

    return booleanExpression


# Loops through the truth tables (i.e. 1011) and converts each to Boolean expressions
def generateBoolExpDictionary(truthTables):
    booleanExpressions = {}
    for t in truthTables:
        truthString = "".join(str(element) for element in t)
        booleanExpressions.update(
            {truthString: decodeBinaryToBooleanExpression(t)})

    return booleanExpressions


def convertTruthTableIntoBinaryValues(truthTables):
    listOfBinaryValues = []
    for t in truthTables:
        truthString = "".join(str(element) for element in t)
        binaryValue = int(truthString, 2)
        listOfBinaryValues.append(binaryValue)

    return listOfBinaryValues


def createHeatmap(binaryValues, boolDict, matrixSize):
    # Shape array into QR size
    array = np.array(binaryValues)
    reshapedArray = np.reshape(array, (matrixSize, matrixSize))

    # Add the colour bar using an ordered dictionary indicating the boolean expressions
    n = len(boolDict)
    cmap = sns.color_palette(cc.glasbey_hv, n)
    ax = sns.heatmap(reshapedArray, cmap=cmap, linewidths=.6)
    colorbar = ax.collections[0].colorbar
    r = colorbar.vmax - colorbar.vmin

    # Place the labels for the colour bar in a structure manner
    colorbar.set_ticks([colorbar.vmin + 0.5 * r / (n) +
                       r * i / (n) for i in range(n)])
    sortedDict = dict(sorted(boolDict.items()))
    colorbar.set_ticklabels(list(sortedDict.values()))
    plt.title(
        "Colour Coordinated Matrix of Boolean Expressions\n 2 Input, Micro QR code (Version M3), 15 by 15 Modules")
    plt.show()


def decode(inputs, version, microBool, error, mask):
    matrixList = generateQRCodeMatrices(
        inputs, version, microBool, error, mask)
    matrixSize = len(matrixList[0])
    truthTables = generateTruthTablesFromQRMatrix(matrixList)
    boolDict = generateBoolExpDictionary(truthTables)

    binaryValues = convertTruthTableIntoBinaryValues(truthTables)

    # Pretty printing of the dictionary if needed
    print("\n{\n" + "\n".join("{!r}: {!r},".format(k, v)
          for k, v in boolDict.items()) + "\n}")
    # print("\n", len(boolDict))

    # Creates heatmap
    createHeatmap(binaryValues, boolDict, matrixSize)
    return boolDict


# Small test
decode(2, 'M3', True, "", "")
