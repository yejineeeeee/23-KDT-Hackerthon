import 'package:flutter/material.dart';

class ThirdScreen extends StatelessWidget {
  const ThirdScreen({Key? key}): super(key: key);

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
                color: Colors.red,
                child: Center(
                    child: Column(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          Text(
                            'Third Screen',
                            style:  TextStyle(color: Colors.white, fontSize: 30),
                          ),
                        ]
                    )
                )
            )
        )
    );
  }
}