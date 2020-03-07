import scipy.io as scio
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import os

# dic=scio.loadmat("data/Salinas_corrected.mat")["salinas_corrected"]
# dic=scio.loadmat("data/SalinasA_corrected.mat")["salinasA_corrected"]
# dic = scio.loadmat("data/Botswana.mat")["Botswana"]
dicc = scio.loadmat("data/Botswana_gt.mat")["Botswana_gt"]
dic = ["black", "snow", "red", "tomato", "chocolate", "orange", "wheat", "gold", "yellow", "chartreuse",
	   "limegreen", "aquamarine", "cyan", "dodgerblue", "slateblue", "violet", "pink"]
cmap = mpl.colors.ListedColormap(dic[0:len(np.unique(dicc))])
plt.imshow(dicc,cmap=cmap)
sv = plt.gcf()
sv.savefig(os.path.join(".", "gt.png"), format="png", dpi=300)
plt.show()

print(np.unique(dicc))
