from skimage.metrics import structural_similarity as ssim
import cv2
import os
import json
import numpy as np
import matplotlib.pyplot as plt

# 데이터 저장
data = []
# 폴더 경로를 지정합니다. 여기서는 현재 작업 디렉토리('.')를 사용합니다.
# 라벨링 들어있는 폴더
folder_path = r'C:\Users\nicho\Desktop\hackathon_data\Data\House_train\TL_집'
# 이미지파일 읽을 폴더
image_path = r'C:\Users\nicho\Desktop\hackathon_data\Data\House_train\images'

# 지정한 폴더 내의 모든 파일과 폴더 목록을 가져옵니다.
contents = os.listdir(folder_path)
#print(contents)
# 파일과 폴더 목록을 출력합니다.
for file_name in contents:
    #print(file_name)
    file_path = os.path.join(folder_path, file_name)
    try:
        # JSON 파일을 열어서 내용을 읽고 파싱합니다.
        with open(file_path, "r", encoding="utf-8") as file:
            json_data = json.load(file)
            json_data = json_data['annotations']['bbox'][0]
            #print(json_data['x'])

            # 이미지 파일 열기
            img_name = file_name[:-5] + '.jpg'
            #print(img_name)
            
            img_array = np.fromfile(os.path.join(image_path, img_name), np.uint8)
            image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            #cv2.imshow('원본', image)  # 반전된 이미지를 화면에 표시
            #cv2.waitKey(0)

            if image is not None:
                # 자를 부분의 좌표와 크기를 지정합니다.
                x, y, width, height = json_data['x'], json_data['y'], json_data['w'], json_data['h']  #좌표 및 크기

                # 이미지에서 지정한 부분을 자릅니다.
                cropped_image = image[y:y+height, x:x+width]  # 반전된 이미지를 화면에 표시
                #cv2.imshow('자른이미지', cropped_image)
                #cv2.waitKey(0)

                # 회색으로 만들기
                gray_image = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)

                #좌우 반전
                flipped_image = cv2.flip(gray_image, 1)  # 1은 좌우 반전을 나타냅니다.
                #cv2.imshow('좌우반전', flipped_image)
                #cv2.waitKey(0)

                # 이미지 유사성 측정
                similarity_score = ssim(gray_image, flipped_image)
                data.append(similarity_score)
                print(similarity_score)



            else:
                print("이미지를 열 수 없습니다.")
                  
            file.close()
            
    except Exception as e:
        print(f"파일 읽기 및 JSON 파싱 오류: {file_name}, 오류 메시지: {str(e)}")


plt.boxplot(data)
plt.title('데이터 분포 Box Plot')
plt.ylabel('값')
plt.show()