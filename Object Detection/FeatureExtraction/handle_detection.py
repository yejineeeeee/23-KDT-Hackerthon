import cv2
import numpy as np

# 학습 이미지와 타겟 이미지 로드
train_img = cv2.imread('door_handle_train.jpg', 0)  # 학습 이미지 (문의 손잡이가 포함된 이미지)
test_img = cv2.imread('door_handle_test.jpg', 0)    # 타겟 이미지

# SIFT 객체 생성
sift = cv2.SIFT_create()

# 학습 이미지와 타겟 이미지에서 SIFT 특징점 추출
kp1, des1 = sift.detectAndCompute(train_img, None)
kp2, des2 = sift.detectAndCompute(test_img, None)

# BFMatcher 객체 생성
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1, des2, k=2)

# 좋은 매칭점 선택
good = []
for m, n in matches:
    if m.distance < 0.75 * n.distance:
        good.append(m)

# 손잡이 탐지 및 결과 표시
if len(good) > 10:
    src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
    dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)

    M, _ = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
    h, w = train_img.shape
    pts = np.float32([[0, 0], [0, h-1], [w-1, h-1], [w-1, 0]]).reshape(-1, 1, 2)
    dst = cv2.perspectiveTransform(pts, M)

    test_img = cv2.polylines(test_img, [np.int32(dst)], True, 255, 3, cv2.LINE_AA)

cv2.imshow('Detected Door Handle', test_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
