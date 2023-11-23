# <tên_biến> = <tên_kiểu_collection>(map(<tên_kiểu_dữ_liệu>, <giá_trị_nhận_vào>))
# Chuyển <giá_trị_nhận_vào> về kiểu dữ liệu <tên_kiểu_collection>, lưu nó vào biến <tên_biến>
ban1 = set(map(str, input("Nhập danh sách bàn 1: ").split()))
ban2 = set(map(str, input("Nhập danh sách bàn 2: ").split()))

# A.union(B) -> gộp A vào B
# A.intersection(B) -> lấy phần chung cuả A, B
# A.difference(B) -> lấy phần A có, B không có
# A.symmetric_difference -> lấy phần không chung của A, B

# Danh sách đk cả 2 bàn
sun = ban1.intersection(ban2)
print("Đk cả 2 bàn: ", sun)

# Danh sách bàn 1 , 2
moon = ban1.union(ban2)
print("Danh sách tổng hợp 2 bàn: ", moon)

# Danh sách đk bàn 1 not 2
cloud = ban1.difference(ban2)
print("Danh sách đk bàn 1 not 2: ", cloud)

# Danh sách đk 1 bàn duy nhất
star = ban1.symmetric_difference(ban2)
print("Danh sách đk 1 bàn duy nhất: ", star)