from dataloader import DataLoader
from utils import selectData
import numpy as np
import pickle as pkl
import seaborn as sns
import matplotlib.pyplot as plt


def load(path):
	f = open(path, "rb")
	return pkl.load(f)


def convertToColor(map):
	palette = {0: (0, 0, 0)}
	for k, color in enumerate(sns.color_palette("hls", len(np.unique(map)))):
		palette[k + 1] = tuple(np.asarray(255 * np.array(color), dtype='uint8'))
	map = np.array(map, dtype=int)
	unique = np.unique(map)
	lut = np.zeros((int)(np.max(unique) + 1), dtype=np.int)
	for it, i in enumerate(unique):
		lut[i] = it
	map = lut[map]
	a = np.zeros(shape=(np.shape(map)[0], np.shape(map)[1], 3), dtype=np.uint8)
	for i in range(np.shape(map)[0]):
		for j in range(np.shape(map)[1]):
			a[i][j] = palette[map[i][j]]
	return a


if __name__ == "__main__":
	dpi = 100
	dic = {"pc": 3, "pu": 2, "sl": 4, "sa": 5}
	path = "./save/0312309/dccn/p7/sa/1/data/probmap.pkl"
	map = load(path)
	map = np.argmax(map, axis=1)
	currentPx = 0
	pathName, matName = selectData(5)
	dataloader = DataLoader(pathName, matName, 7, 0.1, 1)
	index = dataloader.loadAllLabeledData()[-1]
	gt = np.zeros((dataloader.height, dataloader.width))
	for i in range(len(map)):
		idx = index[i]
		h = idx // dataloader.width
		w = idx % dataloader.width
		gt[h][w] = map[i] + 1
	plt.figure(figsize=(dataloader.width*5/dpi, dataloader.height*5/dpi))
	plt.tick_params(axis='both', which='both', bottom=False, top=False, labelbottom=False, right=False, left=False,
	                labelleft=False)
	plt.imshow(convertToColor(gt))
	# plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)
	plt.show()
