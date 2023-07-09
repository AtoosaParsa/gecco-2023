import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(range(10))
ax.set_xlabel('X-axis')
ax.set_ylabel('NAND-ness($\omega$=20)', fontsize=42)

ax.spines['bottom'].set_color('orange')
ax.spines['top'].set_color('orange')
ax.xaxis.label.set_color('orange')
ax.tick_params(axis='x', colors='orange')

ax.spines['left'].set_color('orange')
ax.spines['right'].set_color('orange')
ax.yaxis.label.set_color('orange')
ax.tick_params(axis='y', colors='orange', labelsize=32, width=2, length=15)
ax.locator_params(axis='y', nbins=5)

ax.set_ylim((0, 1))

plt.show()