import numpy as np
from scipy.spatial import Delaunay
from scipy.spatial import KDTree
from scipy.spatial.distance import euclidean
from scipy.spatial.distance import cityblock
from scipy.spatial.distance import cosine
from scipy.spatial.distance import hamming

points = [(1,-1),(2,3),(-2,3),(2,-3)]



#Find the nearest neighbor to point (1,1):
kdtree = KDTree(points)
res = kdtree.query((1,1))
print(res)

# euclidean distance 
print("eulidean distance :")
p1 = (1,0)
p2 = (10,2)

res1 = euclidean(p1,p2)

print(res1)

# Cityblock Distance (Manhattan Distance)
res1 = cityblock(p1,p2)
print(res1)

# cosine distance 
print("cosine distance :")
res1 = cosine(p1,p2)
print(res1)

# hamming distance for binary
print("hamming distance :")
q1 = (True,False,True)
q2 = (False,True,True)
res2 = hamming(q1,q2)
print(res2)