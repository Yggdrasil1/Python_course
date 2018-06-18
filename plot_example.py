import matplotlib.pyplot as plt


measured_ccm = [1500, 1234, 1432, 1324, 1543]
simulated_ccm = [1600, 1114, 1632, 1111, 2333]

measured_cb = [200, 500, 333, 444]
simulated_cb = [188, 100, 123, 444]

fig = plt.figure()
plt.plot([0, 2500], [0, 2500], label=None, color='k', alpha=0.3, linewidth=3)
plt.scatter(measured_ccm, simulated_ccm, label='Central Carbon Metabolism')
plt.annotate('important enzyme',
			 xy=(1234, 1114),
			 xytext=(200, 1500),
			 arrowprops=dict(facecolor='black', width=2, headwidth=8))
plt.scatter(measured_cb, simulated_cb, label='Cofactor Biosynthesis')
plt.text(1800, 200, "I am a string.")
plt.xlim(0, 2500)
plt.ylim(0, 2500)
plt.legend()
plt.xlabel('Measured Protein Abundance [copies/cell]')
plt.ylabel('Simulated Protein Abundance [copies/cell]')
plt.show()

