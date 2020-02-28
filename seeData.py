import scipy.io as scio
import numpy as np

# dic=scio.loadmat("data/Salinas_corrected.mat")["salinas_corrected"]
# dic=scio.loadmat("data/SalinasA_corrected.mat")["salinasA_corrected"]
dic=scio.loadmat("data/Pavia.mat")["pavia"]
print(np.shape(dic))