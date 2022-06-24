from decoder import decode
import matplotlib.pyplot as plt

version = 1
error = ""
datamask = ""
micro = False

outputs = []
graphData = {}

for i in range(2, 5):
    result = decode(i, version, micro, error, datamask)
    graphData.update({str(i): len(result)})

numberOfInput = list(graphData.keys())
combinationsFound = list(graphData.values())

fig, ax = plt.subplot(figsize=(5, 5))
a = ax.bar(numberOfInput, combinationsFound,
           zorder=2, align='center', width=0.5)
ax.bar_label(a)

ax.set_title('Number of combinations found in 2, 3, and 4 inputs')
ax.set_xlabel('Number of Inputs')
ax.set_ylabel('Number of Combinations found')
ax.set_ylim(0, 256)
