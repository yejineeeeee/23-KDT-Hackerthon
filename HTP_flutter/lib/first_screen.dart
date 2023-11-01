import 'package:flutter/material.dart';
import 'test_standby.dart';

class FirstScreen extends StatelessWidget {
  const FirstScreen({Key? key}): super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        appBar: AppBar(
          backgroundColor: Color(0xFF7B95C0),
          title: Text('Mind Decoder'),
        ),
        body: Container(
          child: Column(
            children: [
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                children: [
                  Container(
                    margin: const EdgeInsets.fromLTRB(0, 30, 0, 0),
                    width: 150,
                    height: 100,
                    child: ElevatedButton(
                      onPressed: () {
                        // Navigator.push();
                      },
                      style: ButtonStyle(
                        backgroundColor: MaterialStateProperty.all<Color>(Colors.grey)
                      ),
                      child: const Text(
                        '센터 찾기',
                        style: TextStyle(fontSize: 16),
                      ),
                    ),
                  ),
                  Container(
                    margin: const EdgeInsets.fromLTRB(0, 30, 0, 0),
                    width: 150,
                    height: 100,
                    child: ElevatedButton(
                      onPressed: () {
                        Navigator.push(
                          context,
                          MaterialPageRoute(
                            builder: (context) => const TestStandbyScreen()
                          )
                        );
                      },
                      style: ButtonStyle(
                        backgroundColor: MaterialStateProperty.all<Color>(Colors.grey)
                      ),
                      child: const Text(
                        '검사 해보기',
                        style: TextStyle(fontSize: 16),
                      ),
                    )
                  ),
                ],
              ),
              Container(
                margin: const EdgeInsets.fromLTRB(0, 30, 0, 0),
                width: 335,
                height: 60,
                decoration: BoxDecoration(
                  border: Border.all(
                    color: Colors.black,
                    width: 1,
                  ),
                  borderRadius: BorderRadius.circular(10)
                ),
                child: const Text(
                  '진행중인 분석',
                  style: TextStyle(
                    height: 2.1,
                    fontSize: 20,
                    fontWeight: FontWeight.w400,
                  ),
                  textAlign: TextAlign.center,
                ),
              ),
              Container(
                margin: const EdgeInsets.fromLTRB(0, 30, 0, 0),
                width: 335,
                height: 60,
                child: const Text(
                  '확인해주세요!',
                  style: TextStyle(
                    fontSize: 20,
                    fontWeight: FontWeight.w400,
                  ),
                  textAlign: TextAlign.start,
                ),
              ),
              Row(
                // 슬라이드 만들어야 함
              )
            ],
          )
        )
      )
    );
  }
}