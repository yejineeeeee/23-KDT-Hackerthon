from PIL import Image # 한글 경로 문제 
import os
import cv2
import numpy as np

## 최외각선만 뽑기
def draw_contour(target):
    folder_path = 'C:/Users/user/Desktop/GitHub/23-KDT-Hackerthon/yolov8_ubuntu/house/FeatureExtraction/cropped/' + target
    image_file_names = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and f.endswith('.jpg')]
    
    # edge_folder_path = folder_path + '/edges'
    # if not os.path.exists(edge_folder_path):
    #     os.makedirs(edge_folder_path)
        
    contour_folder_path = folder_path + '/contours' 
    if not os.path.exists(contour_folder_path):
        os.makedirs(contour_folder_path)  
        
    for img_fname in image_file_names:
        img_path = folder_path + f'/{img_fname}'
        
        with Image.open(img_path) as img:
            img = np.array(img)
            # height, width, _ = img.shape
            
        edges = cv2.Canny(img, 50, 150)  # Canny 엣지 검출
        
        # Morphological operations to reduce noise  ## 끊어진 엣지를 연결하며 (팽창), 노이즈나 작은 객체를 제거 (침식)
        kernel = np.ones((3,3),np.uint8)
        edges = cv2.dilate(edges, kernel, iterations=1)
        edges = cv2.erode(edges, kernel, iterations=1)
        
        # # 엣지 이미지 저장
        # img_pil = Image.fromarray(edges)
        # edge_img_path = edge_folder_path + f'/{img_fname}'
        # img_pil.save(edge_img_path)

        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # Find contours

        # # 창문의 contour가 연결된 상태이므로, min_contour_area로 쳐내는 것은 불가함.
        # # Filter contours by area
        # min_contour_area = height * width * 0.8
        # filtered_contours = [contour for contour in contours if cv2.contourArea(contour) > min_contour_area]

        # # Draw the filtered contours
        # outline_img = np.zeros_like(img)
        # cv2.drawContours(outline_img, filtered_contours, -1, (0, 255, 0), 2)  # 인덱스 0: 첫번째 윤곽선만 (-1: 모든윤곽선)
        
        # # 외곽선 이미지 저장
        # img_pil = Image.fromarray(outline_img)
        # contour_img_path = contour_folder_path + f'/{img_fname}'
        # img_pil.save(contour_img_path)
        
        # Draw the contours
        outline_img = np.zeros_like(img)
        cv2.drawContours(outline_img, contours, -1, (0, 255, 0), 2)  # 인덱스 0: 첫번째 윤곽선만 (-1: 모든윤곽선)
        img_pil = Image.fromarray(outline_img)
        contour_img_path = contour_folder_path + f'/{img_fname}'
        img_pil.save(contour_img_path)
        
    return

target = '창문'
draw_contour(target)