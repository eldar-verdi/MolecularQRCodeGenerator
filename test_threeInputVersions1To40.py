from decoder import decode
import matplotlib.pyplot as plt

'''
Test 4: Three Inputs.
QR Code versions 1 to 40
'''
numberOfInputs = 3
error = ""
mask = ""
graphData = {}
microBool = False


def threeInputDecode(version):
    result = decode(numberOfInputs, version, microBool,
                    error, mask)
    # print("\nVersion:", version, "\nLength: ",
    #       len(result), "\nResult: ", result)
    graphData.update({str(version): len(result)})

def runTests():

    for c in range(1, 10):
        threeInputDecode(c)

    versions = list(graphData.keys())
    combinations = list(graphData.values())

    # print(versions)
    # print(combinations)
    fig, ax = plt.subplots(figsize=(10, 10))
    a = ax.bar(versions, combinations, zorder=2, align='center', width=0.4)
    ax.bar_label(a)

    ax.set_title(
        'Number of Combinations found with Three Input QR Codes \n Default data masks')
    ax.set_xlabel("QR Code Version")
    ax.set_ylabel("Number of Combinations found")
    ax.set_ylim(0, 256)
    plt.grid(axis='y', alpha=0.4, zorder=3)
    plt.show()


runTests()
