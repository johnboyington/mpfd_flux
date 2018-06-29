import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append('/home/john/workspace/python_modules')
from spectrum import Spectrum
import nice_plots


nodes = ['C1', 'C2', 'C3', 'C4']

error = False

###############################################################################


data = np.load('mpfd_nodal_data.npy')[()]
colors = ['b', 'g', 'r', 'indigo']


fig = plt.figure(0, figsize=(8, 6))
ax = fig.add_subplot(111)
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlim(1e-10, 20)
ax.set_xlabel('Energy $MeV$')
ax.set_ylabel('Flux $cm^{-2}s^{-1}MeV^{-1}$')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)


for i, node in enumerate(nodes):
    node_data = data[node]

    erg, values, err = node_data.T
    values = values[1:]
    err = err[1:]
    spec = Spectrum(erg, values, err * values)

    # plot data
    ax.plot(spec.step_x, spec.step_y, colors[i], linewidth=1, label=node)
    if error:
        ax.errorbar(spec.midpoints, spec.normalized_values, spec.rel_error * spec.normalized_values,
                    color=colors[i], linestyle='none', linewidth=0.8)

ax.legend()
ax.legend(frameon=False)
