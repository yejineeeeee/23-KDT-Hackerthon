class_mapping = {
    '집전체': 0,
    '지붕': 1,
    '집벽': 2,
    '문': 3,
    '창문': 4,
    '굴뚝': 5,
    '연기': 6,
    '울타리': 7,
    '길': 8,
    '연못': 9,
    '산': 10,
    '나무': 11,
    '꽃': 12,
    '잔디': 13,
    '태양': 14,
    '나무전체': 15,
    '기둥': 16,
    '수관': 17,
    '가지': 18,
    '뿌리': 19,
    '나뭇잎': 20,
    '꽃': 21,
    '열매': 22,
    '그네': 23,
    '새': 24,
    '다람쥐': 25,
    '구름': 26,
    '달': 27,
    '별': 28,
    '여자사람전체': 29,
    '여자머리': 30,
    '여자얼굴': 31,
    '여자 눈': 32,
    '여자 코': 33,
    '여자 입': 34,
    '여자 귀': 35,
    '여자 머리카락': 36,
    '여자 목': 37,
    '여자 상체': 38,
    '여자 팔': 39,
    '여자 손': 40,
    '여자 다리': 41,
    '여자 발': 42,
    '여자 단추': 43,
    '여자 주머니': 44,
    '여자 운동화': 45,
    '여자구두': 46,
    '남자 사람전체': 47,
    '남자 머리': 48,
    '남자 얼굴': 49,
    '남자 눈': 50,
    '남자 코': 51,
    '남자 입': 52,
    '남자 귀': 53,
    '남자 머리카락': 54,
    '남자 목': 55,
    '남자 상체': 56,
    '남자 팔': 57,
    '남자 손': 58,
    '남자 다리': 59,
    '남자 발': 60,
    '남자 단추': 61,
    '남자 주머니': 62,
    '남자운동화': 63,
    '남자구두': 64
}

# 디렉터리 내의 모든 파일을 가져오기
label_directory = "/content/data/labels/train"
label_files = [os.path.join(label_directory, file) for file in os.listdir(label_directory) if file.endswith(".txt")]

# 클래스별 bounding box 크기 및 넓이 저장 딕셔너리 초기화
class_data = {class_name: {"sizes": [], "areas": []} for class_name in class_mapping.keys()}

# 모든 라벨링 파일에서 bounding box 크기와 넓이 추출하여 클래스별로 저장
for label_file_path in label_files:
    with open(label_file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            data = line.strip().split(" ")
            class_idx = int(data[0])
            x_center, y_center, width, height = float(data[1]), float(data[2]), float(data[3]), float(data[4])
            area = width * height  # 넓이 계산
            class_name = [key for key, value in class_mapping.items() if value == class_idx][0]
            class_data[class_name]["sizes"].append((width, height))
            class_data[class_name]["areas"].append(area)

# 각 클래스별 bounding box 크기의 평균과 분산, 넓이의 평균과 분산, 이상치 경계 계산
for class_name, data in class_data.items():
    if data["sizes"]:
        sizes_array = np.array(data["sizes"])
        areas_array = np.array(data["areas"])
        mean_size = np.mean(sizes_array, axis=0)
        variance_size = np.var(sizes_array, axis=0)
        mean_area = np.mean(areas_array)
        variance_area = np.var(areas_array)
        
        # 이상치 경계 계산
        Q1_size = np.percentile(sizes_array, 25, axis=0)
        Q3_size = np.percentile(sizes_array, 75, axis=0)
        IQR_size = Q3_size - Q1_size
        lower_bound_size = Q1_size - 1.5 * IQR_size
        upper_bound_size = Q3_size + 1.5 * IQR_size
        
        Q1_area = np.percentile(areas_array, 25)
        Q3_area = np.percentile(areas_array, 75)
        IQR_area = Q3_area - Q1_area
        lower_bound_area = Q1_area - 1.5 * IQR_area
        upper_bound_area = Q3_area + 1.5 * IQR_area

        print(f"{class_name}: Mean Size: {mean_size}, Variance Size: {variance_size}, "
              f"Mean Area: {mean_area}, Variance Area: {variance_area}, "
              f"Lower Bound Size: {lower_bound_size}, Upper Bound Size: {upper_bound_size}, "
              f"Lower Bound Area: {lower_bound_area}, Upper Bound Area: {upper_bound_area}")
    else:
        print(f"{class_name}: No bounding boxes found.")
