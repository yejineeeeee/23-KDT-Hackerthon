import cv2
import numpy as np
import os

folder_path = r"C:\Users\user\Desktop\chin_image"

contents = os.listdir(folder_path)

for file_name in contents:
    file_path = os.path.join(folder_path, file_name)
    try:
        img_array = np.fromfile(file_path, np.uint8)
        image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

        # 원하는 이미지 크기를 설정합니다.
        desired_width = 160
        desired_height = 120

        # 이미지 크기를 조절합니다.
        resized_image = cv2.resize(image, (desired_width, desired_height))

        height, width, _ = resized_image.shape
        center_x, center_y = width // 2, height // 2
        center_y_2 = center_y + center_y // 2 + center_y // 5

        # 이미지 상단과 하단을 흰색으로 만듭니다.
        top_height = center_y_2  # 상단에서 흰색으로 만들 영역의 높이
        bottom_height = 1  # 하단에서 흰색으로 만들 영역의 높이

        resized_image[:top_height, :] = (255, 255, 255)  # 상단 영역을 흰색으로 설정
        resized_image[-bottom_height:, :] = (255, 255, 255)  # 하단 영역을 흰색으로 설정

        # gray 변환
        gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

        # 노이즈 제거
        gray = cv2.medianBlur(gray, ksize=3)
        
        # threshold보다 큰 값을 가진 픽셀을 흰색으로 변경합니다.
        gray = np.where(gray < 120, 0, gray)

        # Harris 코너 검출을 위한 파라미터 설정
        block_size = 2
        ksize = 3
        k = 0.04

        # Harris 코너 검출
        corners = cv2.cornerHarris(gray, block_size, ksize, k)

        # 결과 이미지에서 좌표를 찾기 위한 임계값 설정
        threshold = 0.5 * corners.max()

        # 코너 위치 표시를 위한 이미지 복사
        corner_image = np.copy(resized_image)

        # # 코너를 찾아서 표시
        # corner_image[corners > threshold] = [0, 0, 255]  # 빨간색으로 표시

        # 코너 위치를 얻기 위한 조건에 맞는 포인트 추출
        corner_points = np.argwhere(corners > threshold)
        
        # 코너 위치에 원 그리기 (빨간색, 두께 2)
        for point in corner_points:
            x, y = point[1], point[0]
            cv2.circle(corner_image, (x, y), 5, (0, 0, 255), 1)    
        
        # 코너 개수 출력
        corner_count = len(corner_points)
        # print(corner_count)
        
        # # 결과 이미지를 표시
        # cv2.imshow('Harris Corners', corner_image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        output_path = os.path.join(r"C:\Users\user\Desktop\23_kdt_hackathon\hackathon_data\data\Training\01.원천데이터\TS_남자사람_얼굴_턱", file_name)
                    
        # 한글포함 경로에 넣기 위함..
        ret, img_arr = cv2.imencode('.jpg', corner_image)

        if ret:
            with open(output_path, mode='w+b') as f:
                img_arr.tofile(f)
                
    except Exception as e:
        print(f"파일 읽기 및 JSON 파싱 오류: {file_name}, 오류 메시지: {str(e)}")