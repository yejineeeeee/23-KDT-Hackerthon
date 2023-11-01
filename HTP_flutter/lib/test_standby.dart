import 'dart:io';

import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'check_before_test.dart';
import 'how_to_upload_picture.dart';


class TestStandbyScreen extends StatefulWidget {
  const TestStandbyScreen({Key? key}): super(key: key);

  @override
  State<TestStandbyScreen> createState() => TestStandbyScreenState();
}

class TestStandbyScreenState extends State<TestStandbyScreen> {
  File? _image;
  final ImagePicker picker = ImagePicker();

  Future getImage(ImageSource imageSource) async {
    final image = await picker.pickImage(source: imageSource);
    setState(() {
      _image = File(image!.path);
    });
  }

  Widget showImage() {
    return Container(
      color: const Color(0xffd0cece),
      width: 300,
      height: 300,
      child: Center(
        child: _image == null
          ? Text('No Image Selected.')
          : Image.file(File(_image!.path))
      )
    );
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        appBar: AppBar(
          backgroundColor: Color(0xFF597F67),
          title: Text('검사 해보기'),
        ),
        body: Container(
          child: Column(
            children: [
              Container(
                width: 350,
                child: Row(
                  children: [
                    Text('확인해주세요'),
                    ElevatedButton(
                      onPressed: () {
                        Navigator.push(
                          context,
                          MaterialPageRoute(
                            builder: (context) => const CheckBeforeTestScreen()
                          )
                        );
                      },
                      style: ButtonStyle(
                        backgroundColor: MaterialStateProperty.all<Color>(Colors.orangeAccent),
                      ),
                      child: Text('자세히')
                    ),
                  ]
                ),
              ),
              Container(

                child: Column(
                  children: [
                    Text('준비물'),
                    Text('8절 스케치북, A4용지, 4B연필, 12가지 컬러 펜, 지우개'),
                    Text('반드시 가로로 제시'),
                  ],
                )
              ),
              Container(
                width: 350,
                child: Row(
                  children: [
                    Text('그림 업로드 방법'),
                    ElevatedButton(
                      onPressed: () {
                        Navigator.push(
                          context,
                          MaterialPageRoute(
                            builder: (context) => const HowToUploadPictureScreen()
                          )
                        );
                      },
                      style: ButtonStyle(
                        backgroundColor: MaterialStateProperty.all<Color>(Colors.orangeAccent),
                      ),
                      child: Text('자세히')
                    ),
                  ]
                ),
              ),
              Container(
                width: 350,
                child: Text('내 업로드'),
              ),
              showImage(),
              Container(
                child: Column(
                  children: [
                    Row(
                      mainAxisAlignment: MainAxisAlignment.spaceAround,
                      children: [
                        Container(
                          margin: const EdgeInsets.fromLTRB(0, 40, 0, 0),
                          width: 150,
                          height: 50,
                          child: ElevatedButton(
                            onPressed: () {
                              getImage(ImageSource.camera);
                            },
                            style: ButtonStyle(
                              backgroundColor: MaterialStateProperty.all<Color>(Color(0xFF597F67)),
                            ),
                            child: const Text(
                              '촬영하기',
                              style: TextStyle(fontSize: 14),
                            ),
                          ),
                        ),
                        Container(
                            margin: const EdgeInsets.fromLTRB(0, 40, 0, 0),
                            width: 150,
                            height: 50,
                            child: ElevatedButton(
                              onPressed: () {
                                getImage(ImageSource.gallery);
                              },
                              style: ButtonStyle(
                                backgroundColor: MaterialStateProperty.all<Color>(Color(0xFF597F67)),
                              ),
                              child: const Text(
                                '앨범에서 가져오기',
                                style: TextStyle(fontSize: 14),
                              ),
                            )
                        ),
                      ],
                    ),
                    Container(
                      margin: const EdgeInsets.fromLTRB(0, 10, 0, 0),
                      width: 345,
                      height: 50,
                      child: ElevatedButton(
                        onPressed: () {
                        },
                        style: ButtonStyle(
                          backgroundColor: MaterialStateProperty.all<Color>(Color(0xFF597F67)),
                        ),
                        child: Text(
                          '다음',
                          style: TextStyle(fontSize: 14)
                        )
                      ),
                    )

                  ],
                )
              ),


            ],
          )
        )
      )
    );
  }
}

