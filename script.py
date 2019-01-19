import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.colors as mcol

with open("notes 2019 cs sys elec.txt", 'r') as f:
	lines = [[1 if ans=="V" else 0 for ans in f[1:].split(' ')[1:] ] for f in f.read().split("\n")]

import pprint
pprint.pprint(lines)

result = np.array(lines)
print(result)
print()
print(result.sum())
print(result.size)
print(result.sum()/result.size)


# Make a user-defined colormap.
cm1 = mcol.LinearSegmentedColormap.from_list("MyCmapName",["r","b"])

nrows, ncols = result.shape 

gs = gridspec.GridSpec(ncols, 2)

plt.subplot(gs[:, 0])
plt.imshow(result, cmap=cm1)#plt.cm.gray)
plt.title("total = {} | True={} ({}%)/ False={} ({}%)".format(result.size, 
															  result.sum(), 
															  100*result.sum()/result.size,
															  result.size-result.sum(),
															  100*(result.size-result.sum())/result.size))

for l in range(ncols):
	plt.subplot(gs[l, 1])

	n, bins, patches = plt.hist(result[:, l], bins=2)#, density=True)

	plt.title("{} : F / V".format(chr(ord('A')+l)))
	for p, c in zip(patches, ['red', 'blue']):
		plt.setp(p, 'facecolor', c)



plt.show()