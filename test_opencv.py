import cv2
import numpy as np

# 創建一個空白影像
image = np.zeros((500, 500, 3), dtype="uint8")

# 在影像上繪製矩形
cv2.rectangle(image, (50, 50), (450, 450), (0, 255, 0), 3)

# 保存影像
cv2.imwrite("output_image.png", image)
print("Image saved as output_image.png")

