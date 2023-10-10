import os
import json

def house(name):
    if name == '집전체':
        return 0
    elif name == '지붕':
        return 1
    elif name == '집벽':
        return 2
    elif name == '문':
        return 3
    elif name == '창문':
        return 4
    elif name == '굴뚝':
        return 5
    elif name == '연기':
        return 6
    elif name == '울타리':
        return 7
    elif name == '길':
        return 8
    elif name == '연못':
        return 9
    elif name == '산':
        return 10
    elif name == '나무':
        return 11
    elif name == '꽃':
        return 12
    elif name == '잔디':
        return 13
    elif name == '태양':
        return 14

def tree(name):
    if name == '나무전체':
        return 0
    elif name == '기둥':
        return 1
    elif name == '수관':
        return 2
    elif name == '가지':
        return 3
    elif name == '뿌리':
        return 4
    elif name == '나뭇잎':
        return 5
    elif name == '꽃':
        return 6
    elif name == '열매':
        return 7
    elif name == '그네':
        return 8
    elif name == '새':
        return 9
    elif name == '다람쥐':
        return 10
    elif name == '구름':
        return 11
    elif name == '달':
        return 12
    elif name == '별':
        return 13

man_mapping ={"사람전체":0,
                "머리":1,
                "얼굴":2,
                "눈":3,
                "코":4,
                "입":5,
                "귀":6,
                "머리카락":7,
                "목":8,
                "상체":9,
                "팔":10,
                "손":11,
                "다리":12,
                "발":13,
                "단추":14,
                "주머니":15,
                "운동화":16,
                "남자구두":17
                }

woman_mapping ={'사람전체':0,
                '머리':1,
                '얼굴':2,
                '눈':3,
                '코':4,
                '입':5,
                '귀':6,
                '머리카락':7,
                '목':8,
                '상체':9,
                '팔':10,
                '손':11,
                '다리':12,
                '발':13,
                '단추':14,
                '주머니':15,
                '운동화':16,
                '여자구두':17
                }

# 폴더 경로를 지정합니다. 여기서는 현재 작업 디렉토리('.')를 사용합니다.
# 라벨링 들어있는 폴더
folder_path = r'C:\Users\nicho\Desktop\해커톤\Data\Validation\02.라벨링데이터\VL_여자사람'
# txt파일 저장할 폴더
write_path = r'C:\Users\nicho\Desktop\해커톤\Data\Woman_valid\labels'

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
            json_data = json_data['annotations']['bbox']
            # TXT 파일 열기
            txt_name = file_name[:-5]
            
            with open(write_path+'\\'+txt_name+'.txt', 'w') as file:
                for temp in json_data:
                    class_num = woman_mapping[temp['label']] # class 바꾸는부분
                    x = (temp['x'] + temp['w']/2)/1280
                    y = (temp['y'] + temp['h']/2)/1280
                    w = temp['w']/1280
                    h = temp['h']/1280

                    info = f"{class_num} {x} {y} {w} {h}\n"
                    file.write(info)
                    #print(info)
        
            file.close()
            
    except Exception as e:
        print(f"파일 읽기 및 JSON 파싱 오류: {file_name}, 오류 메시지: {str(e)}")
