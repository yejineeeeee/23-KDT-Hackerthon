import 'package:flutter/material.dart';

class HowToUploadPictureScreen extends StatelessWidget {
  const HowToUploadPictureScreen({Key? key}): super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        appBar: AppBar(
          backgroundColor: Color(0xFF597F67),
          title: Text('그림 업로드 방법'),
        ),
        body: Container(
          child: Column(
            children: [
              Text('1. 사진 촬영'),
              Text('"사진 촬영" 버튼을 통해 사진 촬영 후 올려주세요'),
              Column(
                children: [
                  Text('사진 촬영시 유의 사항'),
                  Text('도화지 전체가 사진 안에 나오도록 촬영해주세요'),
                  Text('종이는 바닥에 내려두고 촬영해주세요'),
                  Text('종이와 대비되는 어두운색 배경 위에 조이를 올려두고 촬영해주세요'),
                  Text('종이와 아이의 그림을 가릴 수 있는 물건은 잠시 옆에 치워두고 촬영해주세요'),
                  Text('그림이 찢어지거나, 구겨진 경우 AI가 정확한 인식을 할 수 없으므로 그림을 다시 그려주세요'),
                ],
              ),
              Text('2. 앨범에서 불러오기'),
              Text('그림을 미리 촬영한 경우 "앨범에서 불러오기" 버튼을 통해 앨범에서 촬영한 그림을 올려주세요'),
              Text('3. 사진 자르기'),
              Column(
                children: [
                  Text('AI의 정확도를 톺이기 위해 아이의 그림을 제외한 배경은 잘라주세요'),
                  Text('사진 자를 때 유의 사항'),
                  Text('종의와 같은 크기로 아이의 그림이 모두 나오게 사진을 잘라주세요'),
                  Text('그림이 돌아간 경우 회전을 통해 그림을 맞춰주세요'),
                  Text('아이아 그린 그림까지 잘리지 않도록 유의해주세요'),
                ],
              ),
            ]
          )
        )
      )
    );
  }
}

