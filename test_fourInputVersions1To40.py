import random
from decoder import decode
import matplotlib.pyplot as plt

'''
Test 5: Four Inputs.
QR Code versions 1 to 40
'''
numberOfInputs = 4
error = ""
graphData = {}
microBool = False


def fourInputDecode(version):
    result = decode(numberOfInputs, version, microBool, error)
    # print("\nVersion:", version, "\nLength: ",
    #       len(result), "\nResult: ", result)
    graphData.update({str(version): len(result)})

def runTests():

    for c in range(1, 7):
        fourInputDecode(c)

    versions = list(graphData.keys())
    combinations = list(graphData.values())

    # print(versions)
    # print(combinations)
    fig, ax = plt.subplots(figsize=(10, 10))
    a = ax.bar(versions, combinations, zorder=2, align='center', width=0.6)
    ax.bar_label(a)

    ax.set_title(
        'Number of Combinations found with Four Input QR Codes \n Default Mask and Error Codes')
    ax.set_xlabel("QR Code Version")
    ax.set_ylabel("Number of Combinations found")
    ax.set_ylim(0, 256)
    plt.grid(axis='y', alpha=0.4, zorder=3)
    plt.show()


runTests()
