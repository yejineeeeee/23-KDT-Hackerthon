import cv2
import numpy as np
import random

# 이미지를 불러옵니다.
img_array = np.fromfile(r'C:\Users\nicho\Desktop\hackathon_data\Data\House_train\images\집_7_남_00885.jpg', np.uint8)
image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
# 이미지의 높이와 너비를 얻습니다.
height, width, _ = image.shape

# 이미지 상단과 하단을 흰색으로 만듭니다.
top_height = 5  # 상단에서 흰색으로 만들 영역의 높이
bottom_height = 5  # 하단에서 흰색으로 만들 영역의 높이

image[:top_height, :] = (255, 255, 255)  # 상단 영역을 흰색으로 설정
image[-bottom_height:, :] = (255, 255, 255)  # 하단 영역을 흰색으로 설정

# 이미지를 그레이스케일로 변환
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 노이즈 제거
gray = cv2.medianBlur(gray, ksize=3)

# threshold보다 큰 값을 가진 픽셀을 흰색으로 변경합니다.
binary_image = np.where(gray >= 240, 255, gray)

# Canny 엣지 검출
edges = cv2.Canny(binary_image, 100, 200)  # 100과 200은 경계값(threshold)으로 조정 가능합니다.

kernel = np.ones((3,3),np.uint8)
edges = cv2.dilate(edges, kernel, iterations=1)
edges = cv2.erode(edges, kernel, iterations=1)