import cv2
import numpy as np

# 이미지를 불러옵니다.
img_array = np.fromfile(r'C:\Users\nicho\Desktop\hackathon_data\Data\House_train\images\집_7_남_06076.jpg', np.uint8)
image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
# 이미지의 높이와 너비를 얻습니다.
height, width, _ = image.shape

# 이미지 상단과 하단을 흰색으로 만듭니다.
top_height = 20  # 상단에서 흰색으로 만들 영역의 높이
bottom_height = 20  # 하단에서 흰색으로 만들 영역의 높이

image[:top_height, :] = (255, 255, 255)  # 상단 영역을 흰색으로 설정
image[-bottom_height:, :] = (255, 255, 255)  # 하단 영역을 흰색으로 설정

# 이미지를 그레이스케일로 변환합니다.
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 가우시안 블러로 노이즈를 제거합니다.
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Canny 엣지 검출을 사용하여 에지를 찾습니다.
edges = cv2.Canny(blurred, 50, 150)

# 에지 이미지에서 선을 찾습니다. maxlineGap 수정필요
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=100, minLineLength=100, maxLineGap=100)

n_line = []
# 찾은 선을 원본 이미지에 그립니다.
for line in lines:
    x1, y1, x2, y2 = line[0]
    # 직선의 각도를 계산하고 수평으로 된 직선만을 선택합니다.
    angle = np.arctan2(y2 - y1, x2 - x1) * 180 / np.pi
    if angle >= -20 and angle <= 20:
        n_line.append(line)
        #cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)


# 가장 긴 선분을 찾습니다.
longest_line = None
max_length = 0

for line in n_line:
    x1, y1, x2, y2 = line[0]
    length = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    if length > max_length:
        max_length = length
        longest_line = line

print(longest_line)
# 가장 긴 선분만을 그립니다.
if longest_line is not None:
    x1, y1, x2, y2 = longest_line[0]
    cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

# 결과 이미지를 보여줍니다.
cv2.imshow('Longest Line', image)
cv2.waitKey(0)
cv2.destroyAllWindows()