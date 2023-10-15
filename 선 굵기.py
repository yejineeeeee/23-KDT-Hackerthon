import cv2
import numpy as np

# 이미지를 불러옵니다.
img_array = np.fromfile(r'C:\Users\nicho\Desktop\hackathon_data\Data\House_train\images\집_7_남_03613.jpg', np.uint8)
image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

# 이미지를 그레이 스케일로 변환합니다.
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# threshold보다 큰 값을 가진 픽셀을 흰색으로 변경합니다.
binary_image = np.where(gray_image > 220, 255, gray_image)

# 전체 픽셀수
binary_pixel_count = np.count_nonzero(binary_image != 255)

# Canny 엣지 검출
canny = cv2.Canny(binary_image, 100, 200)  # 100과 200은 경계값(threshold)으로 조정 가능합니다.

# 결과 이미지를 보여주기
cv2.imshow("Canny Edge Detection", canny)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 경계선 픽셀 수 계산
edge_pixel_count = np.count_nonzero(canny)

# 경계선 픽셀 수 출력
print(f'경계선의 픽셀 수: {edge_pixel_count}')
print(f'전체 픽셀 수: {binary_pixel_count}')
print(f'비율: {edge_pixel_count/binary_pixel_count}')