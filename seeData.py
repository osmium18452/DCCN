import scipy.io as scio
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import os
import seaborn as sns

dic=scio.loadmat("data/Indian_pines_gt.mat")["indian_pines_gt"]
# dic=scio.loadmat("data/SalinasA_corrected.mat")["salinasA_corrected"]
# dic = scio.loadmat("data/Botswana.mat")["Botswana"]
# dicc = scio.loadmat("data/Botswana_gt.mat")["Botswana_gt"]
# dic = ["black", "snow", "red", "tomato", "chocolate", "orange", "wheat", "gold", "yellow", "chartreuse",
# 	   "limegreen", "aquamarine", "cyan", "dodgerblue", "slateblue", "violet", "pink"]
# cmap = mpl.colors.ListedColormap(dic[0:len(np.unique(dicc))])
# plt.imshow(dicc,cmap=cmap)
# sv = plt.gcf()
# sv.savefig(os.path.join(".", "gt.png"), format="png", dpi=300)
# plt.show()
palette = {0: (0, 0, 0)}
for k, color in enumerate(sns.color_palette("hls", len(np.unique(dic))-1)):
	palette[k + 1] = tuple(np.asarray(255 * np.array(color), dtype='uint8'))
# print(palette)
for i in palette:
	print(palette[i])
# plt.show()
def convertToColor(palette,map):
	a=np.zeros(shape=(np.shape(map)[0],np.shape(map)[1],3),dtype=np.uint8)
	for i in range(np.shape(map)[0]):
		for j in range(np.shape(map)[1]):
			a[i][j]=palette[map[i][j]]
	return a
if __name__=="__main__":
	a=convertToColor(palette,dic)
	plt.imshow(a)
	plt.show()
