import scipy.io as scio
import numpy as np

# dic=scio.loadmat("data/Salinas_corrected.mat")["salinas_corrected"]
# dic=scio.loadmat("data/SalinasA_corrected.mat")["salinasA_corrected"]
dic=scio.loadmat("data/KSC.mat")["KSC"]
dicc=scio.loadmat("data/KSC_gt.mat")["KSC_gt"]
print(np.shape(dic))