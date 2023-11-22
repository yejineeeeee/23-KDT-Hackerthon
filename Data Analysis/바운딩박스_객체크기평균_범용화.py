# 라벨 파일이 저장된 디렉터리 경로 설정
label_directory = "/content/data/labels/train"
# 디렉터리 내의 모든 파일 가져오기
label_files = [os.path.join(label_directory, file) for file in os.listdir(label_directory) if file.endswith(".txt")]

# 각 클래스별 bounding box 크기 및 넓이 저장 딕셔너리 초기화
class_data = {class_name: {"sizes": [], "areas": []} for class_name in class_mapping.keys()}

# 라벨링 파일에서 bounding box 크기와 넓이 추출하여 클래스별로 저장
for label_file_path in label_files:
    with open(label_file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            data = line.strip().split(" ")
            class_idx = int(data[0])

            # 주석 처리된 클래스를 제외하고 데이터 처리
            if class_idx in class_mapping.values():
                x_center, y_center, width, height = float(data[1]), float(data[2]), float(data[3]), float(data[4])
                area = width * height  # 넓이 계산
                class_name = [key for key, value in class_mapping.items() if value == class_idx][0]
                class_data[class_name]["sizes"].append((width, height))
                class_data[class_name]["areas"].append(area)

# 각 클래스별 bounding box 크기의 평균과 분산, 넓이의 평균과 분산, 이상치 경계 계산
def get_class_statistics(class_identifiers):
    results = {}
    for class_identifier in class_identifiers:
        if isinstance(class_identifier, str):
            class_idx = class_mapping.get(class_identifier)
        elif isinstance(class_identifier, int):
            class_idx = class_identifier
        else:
            return "유효하지 않은 입력입니다."

        if class_idx in class_mapping.values():
            data = class_data.get(class_identifier)
            if data:
                sizes_array = np.array(data["sizes"])
                areas_array = np.array(data["areas"])
                mean_size = np.mean(sizes_array, axis=0)
                variance_size = np.var(sizes_array, axis=0)
                median_size = np.median(sizes_array, axis=0)
                mean_area = np.mean(areas_array)
                variance_area = np.var(areas_array)
                median_area = np.median(areas_array)

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

                results[class_identifier] = {
                    "평균 크기": mean_size,
                    "크기 분산": variance_size,
                    "크기 중앙값": median_size,
                    "평균 넓이": mean_area,
                    "넓이 분산": variance_area,
                    "넓이 중앙값": median_area,
                    "크기 이상치 하한": lower_bound_size,
                    "크기 이상치 상한": upper_bound_size,
                    "넓이 이상치 하한": lower_bound_area,
                    "넓이 이상치 상한": upper_bound_area
                }
            else:
                return "지정한 클래스에 대한 bounding box가 없습니다."
        else:
            return "매핑 정보에 해당하는 클래스가 없습니다."

    return results


# 사용 예시
class_identifiers = ["나무", "꽃", "태양"]  # 여러 클래스를 리스트로 입력할 수 있습니다
result = get_class_statistics(class_identifiers)

# 결과 출력
for class_name, statistics in result.items():
    print(f"{class_name}에 대한 통계 정보:")
    for stat_name, value in statistics.items():
        print(f"{stat_name}: {value}")
    print("=" * 40)  # 클래스별 구분선 추가
