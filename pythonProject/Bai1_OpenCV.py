import cv2
image = cv2.imread('freeDrawExport_012314055352.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Áp dụng phương pháp threshold để tạo ảnh nhị phân
_, threshold = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)

# Tìm contours trong ảnh
contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Duyệt qua các contours và tìm bounding box
for contour in contours:
    # Bỏ qua các contour có diện tích nhỏ
    if cv2.contourArea(contour) > 100:  # Có thể thay đổi giá trị ngưỡng diện tích tùy thuộc vào ảnh của bạn
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Hiển thị hình ảnh với bounding box
cv2.imshow('Image with bounding box', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
