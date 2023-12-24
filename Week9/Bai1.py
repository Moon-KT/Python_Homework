import numpy as np

# Khởi tạo mảng numpy a (1-D) với n phần tử ngẫu nhiên khoảng từ [1, 14]
n = 10  # Số phần tử của mảng a
a = np.random.randint(1, 15, n)
print("Mảng a:", a)
print("ndim:", a.ndim)
print("shape:", a.shape)
print("len:", len(a))
print("itemsize:", a.itemsize)
print("dtype:", a.dtype)

# Khởi tạo mảng numpy b với 100 số chẵn đầu tiên
b = np.arange(0, 200, 2)
print("Mảng b:",b )

# Khởi tạo ma trận numpy c có kích thước nxn với 100 phần tử 0, in ra màn hình
n = 10  # Kích thước ma trận nxn
c = np.zeros((n, n))
print("Ma trận c:", c)
print("ndim:", c.ndim)
print("shape:", c.shape)
print("len:", len(c))
print("itemsize:", c.itemsize)
print("dtype:", c.dtype)

# Khởi tạo ma trận đơn vị d có kích thước nxn
d = np.eye(n)
print("Ma trận đơn vị d:",d)
print("ndim:", d.ndim)
print("shape:", d.shape)
print("len:", len(d))
print("itemsize:", d.itemsize)
print("dtype:", d.dtype)
print()

# Khởi tạo ma trận đường chéo e với các giá trị trên đường chéo là mảng a
e = np.diag(a)
print("Ma trận đường chéo e:", e)
print("ndim:", e.ndim)
print("shape:", e.shape)
print("len:", len(e))
print("itemsize:", e.itemsize)
print("dtype:", e.dtype)
