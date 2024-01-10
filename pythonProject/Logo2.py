import numpy as np
import cv2

# Tạo hình ảnh với nền màu đen (kích thước 500x800)
height, width = 430, 350
img = np.zeros((height, width, 3), dtype=np.uint8)  # Tạo ma trận các giá trị 0

# Màu cam (BGR: (0, 140, 255))
orange_color = (0, 140, 255)

# Tọa độ trung tâm và bán kính của hình tròn
center_coordinates = (width // 2, height // 2)
radius = 165

# Văn bản cần chèn
text_HIT = "HIT"
text_CLUB = "CLUB"
text_CLB = "CLB Tin Hoc DH CNHN"

# Tọa độ và font
center_text_HIT = (65, 270)
center_text_CLUB = (115, 315)
center_text_CLB = (66, 310)
font_face = cv2.FONT_HERSHEY_SIMPLEX

text_size = cv2.getTextSize(text_CLUB, font_face, 7, 5)[0]
text_x = int((width - text_size[0]) / 2)
text_y = int((height + text_size[1]) / 2)

cv2.putText(img, text_CLUB, center_text_CLUB, font_face, 1, orange_color, 2, cv2.LINE_AA)

# Vẽ 3 đường thẳng
cv2.line(img, (236, 220),  (264, 220), orange_color,2 , cv2.LINE_AA)
cv2.line(img, (250, 220),  (250, 250), orange_color,2 , cv2.LINE_AA)
cv2.line(img, (250, 250),  (270, 250), orange_color,2 , cv2.LINE_AA)

rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), 90, 1)
rotation_out = cv2.warpAffine(img, rotation_matrix, (width, height))

cv2.putText(rotation_out, text_HIT, center_text_HIT, font_face, 4.5, orange_color, 19 ,cv2.LINE_AA)
cv2.putText(rotation_out, text_CLB, center_text_CLB, font_face, 0.6, orange_color, 2 ,cv2.LINE_AA)

# Vẽ hình tròn
cv2.circle(rotation_out, center_coordinates, radius, orange_color, 4,cv2.LINE_AA)

# Vẽ hình elip
cv2.ellipse(rotation_out, (175, 140), (25, 15), 0, 0, 360, orange_color, 2, cv2.LINE_AA)

# Mịn hoặc làm mờ ảnh rotation_out
# Điều chỉnh kích thước kernel và các tham số tùy thuộc vào từng hàm để có kết quả phù hợp với mong muốn của bạn

# Làm mịn ảnh bằng GaussianBlur
gaussian_blur = cv2.GaussianBlur(rotation_out, (5, 5), 0.6)  # Kích thước kernel: (5, 5), độ lệch chuẩn = 0

# Làm mịn ảnh bằng bilateralFilter
bilateral_filtered = cv2.bilateralFilter(gaussian_blur, 9, 75, 60)  # Các tham số: (ảnh, đường kính không gian, độ mịn màu sắc, độ mịn không gian)

# Hiển thị các ảnh đã làm mịn hoặc làm mờ
cv2.imshow('Filtered - bilateralFilter', bilateral_filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Lưu các ảnh đã làm mịn hoặc làm mờ
cv2.imwrite('HIT_bilateral_filtered.png', bilateral_filtered)
