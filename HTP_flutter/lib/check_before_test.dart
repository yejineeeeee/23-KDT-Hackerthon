import 'package:flutter/material.dart';

class CheckBeforeTestScreen extends StatelessWidget {
  const CheckBeforeTestScreen({Key? key}): super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        appBar: AppBar(
          backgroundColor: Color(0xFF597F67),
          title: Text('확인해 주세요'),
        ),
        body: Container(
          child: Column(
            children: [
              Text('가장 편안하고 즐거운 상태에서 그림을 그려주세요'),
              Text('아이가 그림을 그리는 동안 모든 질문에는 "마음대로 해"라고 말해주세요'),
              Text('유아는 8철 스케치북에 그리도록 해주세요'),
              Text('초등학생 이상, 성인은 A4용지에 그리세요'),
            ]
          )
        )
      )
    );
  }
}

