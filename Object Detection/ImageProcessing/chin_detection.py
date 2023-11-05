import cv2
import numpy as np
import os
import json
import pandas as pd
import math

folder_path1 = r"C:\Users\user\Desktop\23_kdt_hackathon\hackathon_data\data\Training\01.원천데이터\TS_남자사람"
folder_path2 = r"C:\Users\user\Desktop\23_kdt_hackathon\hackathon_data\data\Training\02.라벨링데이터\TL_남자사람"

# 지정한 폴더 내의 모든 파일과 폴더 목록을 가져옵니다.
contents = os.listdir(folder_path1)
cnt=0
numofpoint=dict()

# 파일과 폴더 목록을 출력합니다.
for file_name in contents:
    if cnt==10000:
        break
    cnt+=1
    file_path = os.path.join(folder_path1, file_name)
    json_path = os.path.join(folder_path2, file_name)
    try:
        img_array = np.fromfile(file_path, np.uint8)
        image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        json_path = json_path[:-2]+'son'
        
        with open(json_path, "r", encoding="utf-8") as file:
            json_data = json.load(file)
            
            # 얼굴에서 이목구비 지우기
            for box in json_data['annotations']['bbox']:    
                if (box['label']=='얼굴' or box['label']=='머리' or box['label']=='사람전체') == False:
                    x, y, width, height = box['x'], box['y'], box['w'], box['h']  #좌표
                    background_color = (255, 255, 255)
                    image[y:y+height, x:x+width] = background_color

            face = json_data['annotations']['bbox'][2]
            if face['label'] != '얼굴':
                continue
            x, y, width, height = face['x'], face['y'], face['w'], face['h']  # 얼굴좌표
            
            # 이목구비 지워진 얼굴이 roi에 저장
            roi = image[y:y+height, x:x+width]
            
            # 노이즈 제거
            roi = cv2.medianBlur(roi, ksize=5)
            
            # 상단 절반을 흰색으로 채우기
            top_height = int(0.75 * height)
            roi[:top_height, :] = (255, 255, 255)
            
            roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
            
            # Harris 코너 검출을 위한 파라미터 설정
            block_size = 6
            ksize = 3
            k = 0.05

            # Harris 코너 검출
            corners = cv2.cornerHarris(roi, block_size, ksize, k)

            # 결과 이미지에서 좌표를 찾기 위한 임계값 설정
            threshold = 0.05* corners.max()

            # 코너 위치 표시를 위한 이미지 복사
            corner_image = np.copy(roi)

            # 코너 위치를 얻기 위한 조건에 맞는 포인트 추출
            corner_points = np.argwhere(corners > threshold)
            
            # 제거할 거리 기준
            threshold_distance = 30

            # 일정 거리 이내의 좌표를 제외한 좌표를 저장할 리스트
            filtered_coord_list = []

            # 거리 계산 함수
            def distance(p1, p2):
                x1, y1 = p1
                x2, y2 = p2
                return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

            # 좌표 간의 거리를 검사하고 일정 거리 이내의 좌표를 제외
            for i, point1 in enumerate(corner_points):
                within_threshold = False
                for j, point2 in enumerate(corner_points):
                    if (i < j) and (distance(point1, point2) <= threshold_distance):
                        within_threshold = True
                        break
                if not within_threshold:
                    filtered_coord_list.append(point1)

            # 다시 RGB로
            corner_image = cv2.cvtColor(corner_image, cv2.COLOR_GRAY2BGR)
            
            # 코너 위치에 원 그리기 (빨간색, 두께 1)
            for point in filtered_coord_list:
                x, y = point[1], point[0]
                red = (0, 0, 255)
                cv2.circle(corner_image, (x, y), 4, color=red, thickness=-1)

            # 코너 개수 출력
            corner_count = len(filtered_coord_list)

            if corner_count>4:
                numofpoint[file_name] = corner_count
            
            output_path = os.path.join(r"C:\Users\user\Desktop\23_kdt_hackathon\hackathon_data\data\Training\01.원천데이터\TS_남자사람_얼굴테두리만", file_name)
                    
        # 한글포함 경로에 넣기 위함..
        ret, img_arr = cv2.imencode('.jpg', corner_image)

        if ret:
            with open(output_path, mode='w+b') as f:
                img_arr.tofile(f)
                
    except Exception as e:
        print(f"파일 읽기 및 JSON 파싱 오류: {file_name}, 오류 메시지: {str(e)}")
        

# df에 코너 개수 5개 이상인 경우만 추출하여 저장
df = pd.DataFrame()
df = df.append(numofpoint, ignore_index=True)

df.to_excel(r"C:\Users\user\Desktop\df.xlsx", index=False)