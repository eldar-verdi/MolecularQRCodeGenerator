from decoder import decode
import matplotlib.pyplot as plt

'''
Test 3: Four Inputs.
QR Code versions 1, 10, 20, 30, 40, M1, M2, M3, M4 
M = Micro QR code
'''
numberOfInputs = 4
error = ""
mask = ""
graphData = {}

def fourInput_QR_1():
    microBool = False
    version = 1
    result = decode(numberOfInputs, version, microBool, error, mask)
    # print("\nVersion:", version, "\nLength: ",
    #       len(result), "\nResult: ", result)
    graphData.update({str(version): len(result)})

def fourInput_QR_M1():
    microBool = True
    version = "M1"
    m1Error = None
    result = decode(numberOfInputs, version, microBool, m1Error, mask)
    # print("\nVersion:", version, "\nLength: ",
    #       len(result), "\nResult: ", result)
    graphData.update({version: len(result)})


def fourInput_QR_M2():
    microBool = True
    version = "M2"
    result = decode(numberOfInputs, version, microBool, error, mask)
    # print("\nVersion:", version, "\nLength: ",
    #       len(result), "\nResult: ", result)
    graphData.update({version: len(result)})

def fourInput_QR_M3():
    microBool = True
    version = "M3"
    result = decode(numberOfInputs, version, microBool, error, mask)
    # print("\nVersion:", version, "\nLength: ",
    #       len(result), "\nResult: ", result)
    graphData.update({version: len(result)})

def fourInput_QR_M4():
    microBool = True
    version = "M4"
    result = decode(numberOfInputs, version, microBool, error, mask)
    # print("\nVersion:", version, "\nLength: ",
    #       len(result), "\nResult: ", result)
    graphData.update({version: len(result)})

def runTests():
    # Comment out functions to test one at a time
    fourInput_QR_1()
    fourInput_QR_M1()
    fourInput_QR_M2()
    fourInput_QR_M3()
    fourInput_QR_M4()
    versions = list(graphData.keys())
    combinations = list(graphData.values())

    print(versions)
    print(combinations)
    fig, ax = plt.subplots()
    a = ax.bar(versions, combinations, zorder=2)
    ax.bar_label(a)

    ax.set_title(
        'Number of Combinations found with Four Input QR Codes \n Default Mask and Error Codes')
    ax.set_xlabel("QR Code Version")
    ax.set_ylabel("Number of Combinations found")
    ax.set_ylim(0, 255)
    plt.grid(axis='y', alpha=0.4, zorder=3)
    plt.show()


runTests()
