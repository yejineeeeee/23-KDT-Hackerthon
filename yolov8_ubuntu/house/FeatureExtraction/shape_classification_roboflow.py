from PIL import Image # 한글 경로 문제 
from roboflow import Roboflow
import os
import cv2
import numpy as np

# 데이터 로딩
target = '창문'
folder_path = 'C:/Users/user/Documents/GitHub/23-KDT-Hackerthon/yolov8_ubuntu/house/FeatureExtraction/cropped/' + target + '/contours'
image_file_names = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and f.endswith('.jpg')]

################## Roboflow 모델 #############################

rf = Roboflow(api_key="Uc9bUhdm6sv8YmOdomYr")
project = rf.workspace().project("shape-detector-sc66g")
model = project.version(1).model

# infer on a local image
labels = []
i = 0
for fname in os.listdir(folder_path):
    if i == 500: break
    prediction = model.predict(folder_path+'/'+fname, confidence=40, overlap=30).json()
    print(prediction)
    if prediction['predictions']:
        labels.append(prediction['predictions'][0]['class'])
    else:
        labels.append('unknown')
        
    i += 1
        
# visualize your prediction
# model.predict("your_image.jpg", confidence=40, overlap=30).save("prediction.jpg")

# infer on an image hosted elsewhere
# print(model.predict("URL_OF_YOUR_IMAGE", hosted=True, confidence=40, overlap=30).json())

################################################################

# 결과 폴더별 저장
label_path = 'C:/Users/user/Documents/GitHub/23-KDT-Hackerthon/yolov8_ubuntu/house/FeatureExtraction/cropped/' + target +'_labels'
for label in set(labels):  # label명 폴더 준비
    label_folder = label_path + f"/{label}"
    if not os.path.exists(label_folder):
        os.makedirs(label_folder)

# 이미지를 해당 레이블 폴더에 저장
cropped_images = []  
for img_fname in image_file_names:  # 이미지 파일 이름을 사용하여 이미지를 로드하고 NumPy 배열로 변환
    img_path = folder_path +'/' + img_fname
    with Image.open(img_path) as img:
        cropped_images.append(np.array(img))
        
for fname, image_np, label in zip(image_file_names, cropped_images, labels):
    label_folder = label_path + f"/{label}"
    img_pil = Image.fromarray(image_np)
    img_pil.save(label_folder + f"/{fname[:-4]}.jpg")