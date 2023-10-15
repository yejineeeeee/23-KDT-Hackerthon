
from PIL import Image # 한글 경로 문제 
import os
import cv2
import numpy as np
from sklearn.cluster import KMeans

## 1. 데이터 로딩
target = '창문'
folder_path = 'C:/Users/user/Documents/GitHub/23-KDT-Hackerthon/yolov8_ubuntu/house/FeatureExtraction/cropped/' + target
image_file_names = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and f.endswith('.jpg')]

# 이미지 파일 이름을 사용하여 이미지를 로드하고 NumPy 배열로 변환
cropped_images = []
for img_fname in image_file_names:
    img_path = folder_path +'/' + img_fname
    with Image.open(img_path) as img:
        cropped_images.append(np.array(img))

# 이미지에서 Hu Moments를 추출하는 함수
def extract_features(image):
    image_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    moments = cv2.moments(image_gray)
    # print(moments)
    hu_moments = cv2.HuMoments(moments).flatten()
    return hu_moments

# 모든 이미지에 대해 특징 추출
features = [extract_features(img) for img in cropped_images]

# 2. K-means 클러스터링 적용
kmeans = KMeans(n_clusters=3)
clusters = kmeans.fit_predict(features)

# 3. 클러스터링 결과 확인 및 저장
# for idx, cluster_label in enumerate(clusters):
#     print(f"Image {idx} is assigned to cluster {cluster_label}")

cluster_path = folder_path = 'C:/Users/user/Documents/GitHub/23-KDT-Hackerthon/yolov8_ubuntu/house/FeatureExtraction/cropped/' + target +'_cluster'
# cluster label명 폴더 준비
for cluster_label in set(clusters):
    cluster_folder = cluster_path + f"/{cluster_label}"
    if not os.path.exists(cluster_folder):
        os.makedirs(cluster_folder)

# 이미지를 해당 클러스터 폴더에 저장
for fname, image_np, cluster_label in zip(image_file_names, cropped_images, clusters):
    cluster_folder = cluster_path + f"/{cluster_label}"
    img_pil = Image.fromarray(image_np)
    img_pil.save(cluster_folder + f"/{fname[:-4]}.jpg")
