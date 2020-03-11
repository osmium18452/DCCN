import scipy.io as scio
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from utils import selectData
import os


# dic=scio.loadmat("data/Indian_pines_gt.mat")["indian_pines_gt"]
# print(palette)
# for i in palette:
# 	print(palette[i])
# plt.show()
def convertToColor(palette, map):
	a = np.zeros(shape=(np.shape(map)[0], np.shape(map)[1], 3), dtype=np.uint8)
	for i in range(np.shape(map)[0]):
		for j in range(np.shape(map)[1]):
			a[i][j] = palette[map[i][j]]
	return a


if __name__ == "__main__":
	for i in range(7):
		path, mat = selectData(i)
		dic = scio.loadmat(path[1])[mat[1]]
		print(mat[1], np.shape(dic))
		continue

		unique = np.unique(dic)
		lut = np.zeros(np.max(unique) + 1, dtype=np.int)
		for iter, i in enumerate(unique):
			lut[i] = iter
		dic = lut[dic]
		palette = {0: (0, 0, 0)}
		for k, color in enumerate(sns.color_palette("hls", len(np.unique(dic)) - 1)):
			palette[k + 1] = tuple(np.asarray(255 * np.array(color), dtype='uint8'))
		gt = convertToColor(palette, dic)
		plt.imshow(gt)
		sv = plt.gcf()
		sv.savefig(".\\paper\\pic\\" + mat[1] + ".eps", format="eps", dpi=300)
