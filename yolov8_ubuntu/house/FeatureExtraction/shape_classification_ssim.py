from PIL import Image # 한글 경로 문제 
import os
# from skimage.metrics import structural_similarity as ssim
import numpy as np
import tensorflow as tf
from collections import defaultdict

# 데이터 로딩
target = '창문'
folder_path = 'C:/Users/user/Desktop/GitHub/23-KDT-Hackerthon/yolov8_ubuntu/house/FeatureExtraction/cropped/' + target + '/contours'
image_file_names = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and f.endswith('.jpg')]

################## ssim #############################
# 이미지 크기를 맞추기 위한 함수
def resize_images(img1, img2):
    w1, h1 = img1.size
    w2, h2 = img2.size
    max_width = max(w1, w2)
    max_height = max(h1, h2)
    return img1.resize((max_width, max_height)), img2.resize((max_width, max_height))

# label 이미지 불러오기
label_images = []
label_names = []
label_path = folder_path + '/labels'
for filename in os.listdir(label_path):
    if filename.endswith(".png") or filename.endswith(".jpg"):
        img = Image.open(os.path.join(label_path, filename)).convert('L')  # Convert to grayscale
        if img:
            label_images.append(img)
            label_names.append(filename.split('.')[0][:-1])
            # img.show() 
# print(label_names)    
    
# 이미지 파일 이름을 사용하여 이미지를 로드하고 NumPy 배열로 변환
labels = []
cropped_images = []
for img_fname in image_file_names:
    img_path = folder_path +'/' + img_fname
    with Image.open(img_path).convert('L') as img:
        cropped_images.append(np.array(img))
        score = defaultdict(int)
        for ref_img, label_class in zip(label_images, label_names):
            resized_img, resized_ref_img = resize_images(img, ref_img)

            # Convert PIL images to NumPy arrays and add an extra channel dimension
            im1 = np.expand_dims(np.array(resized_img), axis=-1)
            im2 = np.expand_dims(np.array(resized_ref_img), axis=-1)

            # Convert NumPy arrays to tf.Tensor
            im1 = tf.convert_to_tensor(im1, dtype=tf.float32)
            im2 = tf.convert_to_tensor(im2, dtype=tf.float32)

            # Compute SSIM using TensorFlow
            similarity_score = tf.image.ssim(im1, im2, max_val=255.0).numpy()

            score[label_class] += similarity_score
        
        max_label = max(score, key=score.get)        # 최댓값을 가지는 class
        print(score)
        print(img_fname, ':', max_label) 
        labels.append(max_label)

################################################################
# 이미지를 해당 클러스터 폴더에 저장
for fname, image_np, label in zip(image_file_names, cropped_images, labels):
    label_folder = label_path + f"/{label}"
    
    # Check if the folder exists; if not, create it
    if not os.path.exists(label_folder):
        os.makedirs(label_folder)

    img_pil = Image.fromarray(image_np)
    img_pil.save(label_folder + f"/{fname[:-4]}.jpg")
