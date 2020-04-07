import numpy as np
import matplotlib.pyplot as plt

a = np.array([1, 2, 3, 4, 5])
b = np.array([6, 7, 8, 9, 10])

c = np.sum((a, b), axis=0)
d = np.sum((a, b), axis=1)

print("a: ", a)
print("b: ", b)
print("c: ", c)
print("d: ", d)
print("maximum element of b: ", np.max(b))

e = np.array([1, 2, 3, 4])
print("e: ", e)
print("Shape of the numpy array e: ", e.shape)
f = e.reshape((2, 2))
print("f: ", f)
print("Shape of the numpy array f: ", f.shape)

j = np.array([1, 4, 2, 9, 5 ,7 ,6, 8, 0])
k = np.sort(j)
print("j: ", j)
print("k: ", k)

g = [1, 2, 3, 4]
h = [1, 4, 9, 16]
plt.plot(g, h)
plt.show()