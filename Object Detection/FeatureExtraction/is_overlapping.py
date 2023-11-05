from PIL import Image, ImageDraw, ImageFont  # 한글 파일명 처리
import yaml


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


def is_overlapping(box1, box2):
    # box: (x1, y1, x2, y2)
    x1_1, y1_1, x2_1, y2_1 = box1
    x1_2, y1_2, x2_2, y2_2 = box2

    # Check for overlap
    return not (x2_1 < x1_2 or x1_1 > x2_2 or y2_1 < y1_2 or y1_1 > y2_2)
