from PIL import Image, ImageDraw, ImageFont  # 한글 파일명 처리
import numpy as np
import os
import yaml
import matplotlib.pyplot as plt
import cv2

## 1. 필요한 파일 불러오기
path = 'C:/Users/user/Desktop/GitHub/23-KDT-Hackerthon/yolov8_ubuntu/house'
yaml_path = path + '/house.yaml'
with open(yaml_path, 'r', encoding='utf-8') as file:
    yaml_data = yaml.safe_load(file)
# print(yaml_data)

label_path = "C:/Users/user/Desktop/GitHub/23-KDT-Hackerthon/yolov8_ubuntu/house/House_valid/labels/집_7_남_06605.txt"
label_fname = "집_7_남_06739.txt"

image_path = "C:/Users/user/Desktop/GitHub/23-KDT-Hackerthon/yolov8_ubuntu/house/House_valid/images/집_7_남_06605.jpg"
image_fname = '집_7_남_06739.jpg'


        
class_mapping = {
    0: '집전체',
    1: '지붕',
    2: '집벽',
    3: '문',
    4: '창문',
    5: '굴뚝',
    6: '연기',
    7: '울타리',
    8: '길',
    9: '연못',
    10: '산',
    11: '나무',
    12: '꽃',
    13: '잔디',
    14: '태양',
}

result = """ """
with open(label_path, 'r', encoding='utf-8') as file:
    label = file.read()

obj = set()
windowN = 0
for line in label.strip().split("\n"):
    a = int(line.split()[0])
    if a == 4:
        windowN  += 1
    obj.add(class_mapping[a])
    
## 유무 확인
if '지붕' not in obj:
    result += '공상력이 없는 사람이며, 정신지체인일 수 있다. 보통의 지능을 가지고 있으면서 위축된 성격을 갖고 있으며 구체적인 것만을 추구하는 경향을 보인다.\n'
if '문' not in obj and '창문' not in obj:
    result += '분열증의 징후가 보인다.\n'
else:
    if '문' not in obj:
        result += '가정환경에서 타인과 접촉하지 않으려는 감정, 외계와의 교류를 원치 않는 냉정한 사람에게 많다.\n'
    if '창문' not in obj:
        result += '철회와 상당한 편집증적 경향성이 있다.\n'
if '울타리' in obj:
    result += '자기가 느끼고 있는 안전을 방해받고 싶지 않다.'
    
## 개수 확인
if windowN >=3 :
    result += '개방과 환경적 접촉에 대한 갈망한다.\n'
    
print(result)
    
    
