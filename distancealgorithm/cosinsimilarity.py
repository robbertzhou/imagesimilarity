import numpy as np
from scipy.spatial.distance import pdist
import math

x=[1,1,1]
y=[5,5,2]
dist2 = pdist(np.vstack([x,y]),'cosine')
dist1 = 1 - np.dot(x,y)/(np.linalg.norm(x)*np.linalg.norm(y))
print(dist2,dist1)

xx = 1* 5 + 5 + 2
ax = 3
ay = 54
print(1 - (12 / (math.sqrt(3) * math.sqrt(54))))