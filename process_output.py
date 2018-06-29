import numpy as np

with open('mcnp.io', 'r') as F:
    output = F.read()

output = output.split('1particles and energy limits')[1].split('Flux in Node ')[1:-1]

keys = []
vals = []
letters = 'ABCDEFGHIJKLMNOP'
for i, letter in enumerate(letters):
    for j in range(1, 5):
        keys.append(8000 + 6 + j + (20 * i))
        vals.append(letter + str(j))

code = dict(zip(keys, vals))

data = {}
for node in output:
    name = float(node[:5])
    node = node.split('energy')[1].split('\n')[1:-5]
    node_data = []
    for line in node:
        line = line.split()
        entry = []
        for value in line:
            entry.append(float(value))
        node_data.append(entry)
    node_data = np.array(node_data)
    data[code[name]] = node_data

np.save('mpfd_nodal_data.npy', data)
