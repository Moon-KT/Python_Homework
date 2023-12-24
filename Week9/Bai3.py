import numpy as np

# Lập mảng 2 chiều với 20 phần tử mỗi hàng random trong khoảng từ [0, 10]
marks = np.random.uniform(0, 11, size=(3, 20))
subjects = ['Đại số tuyến tính', 'Xác suất thống kê', 'Giải tích']

# In ra giá trị lớn nhất và nhỏ nhất ở mỗi môn
for i in range(len(subjects)):
    max_mark = np.max(marks[i])
    min_mark = np.min(marks[i])
    print(f"Điểm cao nhất của môn {subjects[i]}: {max_mark}")
    print(f"Điểm thấp nhất của môn {subjects[i]}: {min_mark}")

# Làm phẳng mảng và xóa các vị trí có điểm là 0
flattened_marks = marks.flatten()
non_zero_marks = flattened_marks[flattened_marks != 0]
print("Mảng sau khi làm phẳng và loại bỏ các điểm là 0:")
print(non_zero_marks)

# Sắp xếp giảm theo thuật toán quicksort
sorted_marks = np.sort(non_zero_marks)[::-1]
print("Mảng sau khi sắp xếp giảm dần:", sorted_marks)

# Nhập số thực k từ bàn phím
k = float(input("Nhập số thực k: "))

# Tìm vị trí chèn k vào mảng sao cho không phá vỡ tính sắp xếp của mảng
insert_index = np.searchsorted(sorted_marks, k, side='right')
sorted_marks = np.insert(sorted_marks, insert_index, k)
print(f"Mảng sau khi chèn số {k}:", sorted_marks)
