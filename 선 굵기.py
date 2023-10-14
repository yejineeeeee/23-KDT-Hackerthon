import cv2
import numpy as np

# 이미지를 불러옵니다.
img_array = np.fromfile(r'C:\Users\nicho\Desktop\hackathon_data\Data\House_train\images\집_7_남_03613.jpg', np.uint8)
image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

# Canny 엣지 검출
canny = cv2.Canny(image, 100, 200)  # 100과 200은 경계값(threshold)으로 조정 가능합니다.

# 경계선 픽셀 수 계산
edge_pixel_count = np.count_nonzero(canny)

# 경계선 픽셀 수 출력
print(f'경계선의 픽셀 수: {edge_pixel_count}')

def count_dark_pixels(image, threshold=200):
    # 어두운 픽셀 추출
    dark_pixels = (image < threshold).astype(np.uint8) * 255  # 어두운 픽셀을 흰색(255)으로, 나머지를 검은색(0)으로 설정

   # 어두운 픽셀 수 계산
    dark_pixel_count = (dark_pixels == 255).sum()

    return dark_pixels, dark_pixel_count

# 이미지를 불러옵니다.
img_array = np.fromfile(r'C:\Users\nicho\Desktop\hackathon_data\Data\House_train\images\집_7_남_03613.jpg', np.uint8)
image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

# 어두운 픽셀 추출 및 수 계산 (기본 임계값은 128)
dark_pixels, dark_pixel_count = count_dark_pixels(image)

# 어두운 부분 이미지를 화면에 표시
cv2.imshow('Dark Pixels', dark_pixels)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(f'어두운 픽셀 수: {dark_pixel_count}')
