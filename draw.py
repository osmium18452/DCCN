from dataloader import DataLoader
from utils import selectData
import numpy as np
import pickle as pkl
import seaborn as sns
import matplotlib.pyplot as plt
import argparse


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

def draw(pic):
	pass


if __name__ == "__main__":
	parser=argparse.ArgumentParser()
	parser.add_argument("-d","--data",default="sa")
	args=parser.parse_args()
	dpi = 100
	dic = {"pc": 3, "pu": 2, "sl": 4, "sa": 5}
	for i in (args.data,):
		path = "./save/0312309/data/DCCN/p7/"+i+"/1/data/probmap.pkl"
		map = load(path)
		map = np.argmax(map, axis=1)
		currentPx = 0
		pathName, matName = selectData(dic[i])
		dl = DataLoader(pathName, matName, 7, 0.1, 1)
		index = dl.loadAllLabeledData()[-1]
		gt = np.zeros((dl.height, dl.width))
		for i in range(len(map)):
			idx = index[i]
			h = idx // dl.width
			w = idx % dl.width
			gt[h][w] = map[i] + 1
		plt.figure(figsize=(dl.width * 5 / dpi, dl.height * 5 / dpi))
		plt.tick_params(axis='both', which='both', bottom=False, top=False, labelbottom=False, right=False, left=False,
						labelleft=False)
		plt.imshow(convertToColor(gt))
		# plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)
		plt.show()
		del(dl)
