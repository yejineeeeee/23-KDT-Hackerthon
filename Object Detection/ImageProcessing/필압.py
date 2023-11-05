import cv2
import numpy as np

# 이미지를 불러옵니다.
img_array = np.fromfile(r'C:\Users\nicho\Desktop\hackathon_data\Data\House_train\images\집_7_남_03613.jpg', np.uint8)
image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

# 이미지를 그레이 스케일로 변환합니다.
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 원하는 threshold 값을 설정합니다.
threshold_value = 220

# threshold보다 큰 값을 가진 픽셀을 흰색으로 변경합니다.
binary_image = np.where(gray_image > threshold_value, 255, gray_image)

# 이진 이미지에서 흰색이 아닌 부분을 추출합니다.
non_white_pixels = binary_image[binary_image != 255]

# 결과 출력
cv2.imshow('Binary Image', binary_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 이미지의 모든 픽셀 값의 평균을 계산합니다.
average_pixel_value = np.mean(non_white_pixels)

# 결과 출력
print(f'픽셀 평균 값: {average_pixel_value:.2f}')