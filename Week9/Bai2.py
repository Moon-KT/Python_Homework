import numpy as np

# Nhập từ bàn phím 2 vector numpy a và b
n = int(input("Nhập số chiều(kt) của vector: "))
a = np.zeros(n)
b = np.zeros(n)

for i in range(n):
    a[i] = float(input(f"Nhập phần tử a [{i+1}]: "))
for i in range(n):
    b[i] = float(input(f"Nhập phần tử thứ b[{i+1}]: "))

# In ra max, min, giá trị trung bình, độ lệch chuẩn, giá trị trung vị của vector
print("Thông tin về vector a:")
print("Max:", np.max(a))
print("Min:", np.min(a))
print("Giá trị trung bình:", np.mean(a))
print("Độ lệch chuẩn:", np.std(a))
print("Giá trị trung vị:", np.median(a))

print("Thông tin về vector b:")
print("Max:", np.max(b))
print("Min:", np.min(b))
print("Giá trị trung bình:", np.mean(b))
print("Độ lệch chuẩn:", np.std(b))
print("Giá trị trung vị:", np.median(b))
print()

# Tạo ma trận c (2-D) từ a và b
c = np.column_stack((a, b))
print("Ma trận c:",c)

# Tạo ma trận d (2-D) theo phân phối Gauss (với mean, std của b)
mean_b = np.mean(b)
std_b = np.std(b)
d = np.random.normal(mean_b, std_b, (n, n))
print("Ma trận d:",d )

# Tính tổng, hiệu, tích 2 ma trận
sum_matrix = c + d
difference_matrix = c - d
product_matrix = np.matmul(c, d)

# Tính tích ma trận chuyển vị của d với ma trận nghịch đảo của d
d_transpose = np.transpose(d)
d_inverse = np.linalg.inv(d)
product_inverse_matrix = np.matmul(d_transpose, d_inverse)

# In kết quả
print("Tổng của ma trận c và d:")
print(sum_matrix)

print("Hiệu của ma trận c và d:")
print(difference_matrix)

print("Tích của ma trận c và d:")
print(product_matrix)

print("Tích ma trận chuyển vị của d và ma trận nghịch đảo của d:")
print(product_inverse_matrix)

# Chuyển ma trận c về tensor numpy e (3-D)
e = np.expand_dims(c, axis=0)
print("Tensor e (3-D):",e)

