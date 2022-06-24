from decoder import decode
import matplotlib.pyplot as plt

'''
Test 1: Two Inputs.
QR Code versions 1, M1, M2, M3, M4 
M = Micro QR code
'''
numberOfInputs = 2
error = ''
mask = ''
graphData = {}

def twoInput_QR_1():
    microBool = False
    version = 1
    result = decode(numberOfInputs, version, microBool,
                    error, mask)
    # print("\nVersion:", version, "\nLength: ",
    #       len(result), "\nResult: ", result)
    graphData.update({str(version): len(result)})

def twoInput_QR_M1():
    microBool = True
    version = "M1"
    m1Error = None
    result = decode(numberOfInputs, version, microBool,
                    m1Error, mask)
    # print("\nVersion:", version, "\nLength: ",
    #       len(result), "\nResult: ", result)
    graphData.update({version: len(result)})


def twoInput_QR_M2():
    microBool = True
    version = "M2"
    result = decode(numberOfInputs, version, microBool,
                    error, mask)
    # print("\nVersion:", version, "\nLength: ",
    #       len(result), "\nResult: ", result)
    graphData.update({version: len(result)})

def twoInput_QR_M3():
    microBool = True
    version = "M3"
    result = decode(numberOfInputs, version, microBool,
                    error, mask)
    # print("\nVersion:", version, "\nLength: ",
    #       len(result), "\nResult: ", result)
    graphData.update({version: len(result)})

def twoInput_QR_M4():
    microBool = True
    version = "M4"
    result = decode(numberOfInputs, version, microBool,
                    error, mask)
    # print("\nVersion:", version, "\nLength: ",
    #       len(result), "\nResult: ", result)
    graphData.update({version: len(result)})

def runTests():
    # Comment out functions to test one at a time
    twoInput_QR_1()
    twoInput_QR_M1()
    twoInput_QR_M2()
    twoInput_QR_M3()
    twoInput_QR_M4()
    versions = list(graphData.keys())
    combinations = list(graphData.values())

    print(versions)
    print(combinations)
    fig, ax = plt.subplots()

    a = ax.bar(versions, combinations, zorder=2)
    ax.bar_label(a)
    ax.set_title(
        'Number of Boolean Expressions Found in Three Input Micro QR Codes\n Incrementing Data Masks')
    ax.set_xlabel("QR Code Version")
    ax.set_ylabel("Number of Combinations found")
    ax.set_ylim(0, 20)
    plt.grid(axis='y', alpha=0.4, zorder=3)

    plt.show()


runTests()
