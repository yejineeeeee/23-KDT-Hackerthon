import 'package:flutter/material.dart';

class FourthScreen extends StatelessWidget {
  const FourthScreen({Key? key}): super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
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
                            'Fourth Screen',
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