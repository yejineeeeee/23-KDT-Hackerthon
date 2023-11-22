import cv2
import numpy as np
import random

# 이미지를 불러옵니다.
img_array = np.fromfile(r'C:\Users\nicho\Desktop\4.jpg', np.uint8)
image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
# 이미지의 높이와 너비를 얻습니다.
height, width, _ = image.shape
center_x, center_y = width // 2, height // 2

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
gray = np.where(gray >= 240, 255, gray)

# Canny 엣지 검출
edges = cv2.Canny(gray, 100, 200)  # 100과 200은 경계값(threshold)으로 조정 가능합니다.

kernel = np.ones((3,3),np.uint8)
edges = cv2.dilate(edges, kernel, iterations=1)
edges = cv2.erode(edges, kernel, iterations=1)

# 윤곽선 찾기
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#print(len(contours))

# 외곽선 중에서 중심에서 가장 먼 외곽선을 찾습니다.
max_contour = max(contours, key=lambda c: cv2.contourArea(c))

# 외곽선을 감싸는 최소 크기의 타원을 구합니다.
ellipse = cv2.fitEllipse(max_contour)

# 타원의 반지름을 변경합니다.
new_semimajor_axis = ellipse[1][0] * 0.7  # 주축 반지름 변경
new_semiminor_axis = ellipse[1][1] * 0.7  # 부축 반지름 변경

# 이미지 크기와 같은 빈 이미지를 생성합니다.
result = np.ones_like(gray) * 255

# 타원 내부의 마스크를 생성합니다.
mask = np.zeros_like(gray)
cv2.ellipse(mask, (ellipse[0], (new_semimajor_axis, new_semiminor_axis), ellipse[2]), 255, -1)  # 타원 내부를 흰색으로 채웁니다.

# 타원 외부의 마스크를 생성합니다.
outer_mask = np.bitwise_not(mask)  # 타원 내부의 반대 영역을 검은색으로 채웁니다.

# 원본 이미지에서 흰색이 아닌 부분을 추출합니다.
result = cv2.bitwise_and(image, image, mask=mask)

# 타원 외부를 하얀색으로 처리합니다.
result[outer_mask == 255] = 255

# 결과 이미지를 표시합니다.
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()