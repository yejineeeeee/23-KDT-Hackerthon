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




def compare_classes(class_name1, class_name2):
    class_idx1 = class_mapping.get(class_name1)
    class_idx2 = class_mapping.get(class_name2)
    
    if class_idx1 in class_mapping.values() and class_idx2 in class_mapping.values():
        data1 = class_data.get(class_name1)
        data2 = class_data.get(class_name2)
        
        if data1 and data2:
            mean_size1 = np.mean(data1["sizes"], axis=0)
            mean_size2 = np.mean(data2["sizes"], axis=0)
            mean_area1 = np.mean(data1["areas"])
            mean_area2 = np.mean(data2["areas"])
            
            size_ratio_width = mean_size2[0] / mean_size1[0]
            size_ratio_height = mean_size2[1] / mean_size1[1]
            area_ratio = mean_area2 / mean_area1
            
            return {
                "평균 크기 비율 (너비)": size_ratio_width,
                "평균 크기 비율 (높이)": size_ratio_height,
                "평균 넓이 비율": area_ratio
            }
        else:
            return "지정한 클래스에 대한 bounding box가 없습니다."
    else:
        return "매핑 정보에 해당하는 클래스가 없습니다."

# 사용 예시
class_name1 = "나무"
class_name2 = "꽃"
ratio_result = compare_classes(class_name1, class_name2)

# 결과 출력
print(f"{class_name1} 대비 {class_name2}의 크기 및 넓이 비율:")
for stat_name, value in ratio_result.items():
    print(f"{stat_name}: {value}")
