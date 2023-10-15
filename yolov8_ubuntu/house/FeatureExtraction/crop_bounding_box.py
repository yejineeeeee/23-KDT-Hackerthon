from PIL import Image, ImageDraw, ImageFont  # 한글 파일명 처리
import numpy as np
import os
import yaml
import matplotlib.pyplot as plt
import cv2

## 1. 필요한 파일 불러오기
path = 'C:/Users/user/Documents/GitHub/23-KDT-Hackerthon/yolov8_ubuntu/house'
yaml_path = path + '/house.yaml'
with open(yaml_path, 'r', encoding='utf-8') as file:
    yaml_data = yaml.safe_load(file)
# print(yaml_data)

label_folder = path + '/House_valid/labels'
label_fnames = [f for f in os.listdir(label_folder) if os.path.isfile(os.path.join(label_folder, f)) and f.endswith('.txt')]
# print(label_fnames[:5])

image_folder = path + '/House_valid/images'
image_fnames = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f)) and f.endswith('.jpg')]
# print(image_fnames[:5])

# 안정성 (파일명 짝 맞추기)
label_fnames.sort(key=lambda x: os.path.splitext(x)[0])
image_fnames.sort(key=lambda x: os.path.splitext(x)[0])
# print(label_fnames[:5]), print(image_fnames[:5])


## 바운딩 박스 시각화
def draw_bounding_boxes(img_path, txt_content, class_names, font_path='C:/Windows/Fonts/malgun.ttf'):
    # 이미지 로드
    with Image.open(img_path) as img:
        image_np = np.array(img)
        
    # Convert NumPy array to PIL Image
    img_pil = Image.fromarray(image_np)
    draw = ImageDraw.Draw(img_pil)
    
    # 레이블 파싱
    lines = txt_content.strip().split("\n")
    
    # Load font for text
    font = ImageFont.truetype(font_path, 20)  # Adjust font size as needed
    
    
    for line in lines:
        parts = line.split()
        class_id, x_center, y_center, width, height = map(float, parts)
        class_id = int(class_id)
        
        # 바운딩 박스 좌표 계산
        x_center *= image_np.shape[1]
        y_center *= image_np.shape[0]
        width *= image_np.shape[1]
        height *= image_np.shape[0]
        
        x1 = int(x_center - (width / 2))
        y1 = int(y_center - (height / 2))
        x2 = int(x_center + (width / 2))
        y2 = int(y_center + (height / 2))
        
        # Draw rectangle using PIL
        draw.rectangle([x1, y1, x2, y2], outline=(255, 0, 0), width=2)
        
        # Draw text using PIL
        draw.text((x1, y1 - 25), class_names[class_id], font=font, fill=(255, 0, 0))  # Adjusted y-coordinate for visibility
    
    # Convert back to NumPy array
    image_np = np.array(img_pil)
    
    plt.imshow(image_np)
    plt.axis('off')
    plt.show()


## 필요한 class 잘라오기
def crop_and_save(img_path, txt_content, class_names, target, font_path='path_to_font.ttf'):
    # 이미지 로드
    with Image.open(img_path) as img:
        image_np = np.array(img)
    
    # Convert NumPy array to PIL Image
    img_pil = Image.fromarray(image_np)
    
    # 레이블 파싱
    lines = txt_content.strip().split("\n")
    
    cropped_images = []
    
    for line in lines:
        parts = line.split()
        class_id, x_center, y_center, width, height = map(float, parts)
        class_id = int(class_id)
        
        # 바운딩 박스 좌표 계산
        x_center *= image_np.shape[1]
        y_center *= image_np.shape[0]
        width *= image_np.shape[1]
        height *= image_np.shape[0]
        
        x1 = int(x_center - (width / 2))
        y1 = int(y_center - (height / 2))
        x2 = int(x_center + (width / 2))
        y2 = int(y_center + (height / 2))
        
        # If the class name is "문", crop that part of the image
        if class_names[class_id] == target:
            cropped_img = img_pil.crop((x1, y1, x2, y2))
            cropped_images.append(cropped_img)
            
    # 저장하기
    cropped_path = path + '/FeatureExtraction/cropped/' + target 
    if not os.path.exists(cropped_path): # 폴더가 없으면 생성
        os.makedirs(cropped_path)
        
    # 잘라낸 이미지를 폴더 내에 저장
    for idx, cropped_img in enumerate(cropped_images):
        cropped_img.save(cropped_path + f"/{image_fname[:-4]}_{idx}.jpg")
        
    return
        
target = '창문'
for image_fname, label_fname in zip(image_fnames, label_fnames):
    print(image_fname)
    img_path = image_folder+'/'+image_fname
    with open(label_folder+'/'+label_fname, 'r', encoding='utf-8') as file:
        label = file.read()
        
    # draw_bounding_boxes(img_path, label, yaml_data["names"])  # 바운딩박스 시각화
    
    crop_and_save(img_path, label, yaml_data["names"], target) # 필요한 class 잘라오기 
    
    # break # 일단 이미지 하나만