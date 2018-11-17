# -*- coding:UTF-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

dataMat = []
fr = open("/home/amber/Documents/Final-project/Step2/a_pca_pro.txt")
for line in fr.readlines():
    curLine = line.strip().split('\t')
    fltLine = map(float,curLine)
    dataMat.append(fltLine)

print(len(dataMat))

km = KMeans(n_clusters=4)
km.fit(dataMat)
km_pred = km.predict(dataMat)
centers = km.cluster_centers_ 

print(km_pred)

plt.scatter(np.array(dataMat)[:, 1], np.array(dataMat)[:, 0], c=km_pred)
plt.scatter(centers[:, 1], centers[:, 0], c="r")
plt.show()


