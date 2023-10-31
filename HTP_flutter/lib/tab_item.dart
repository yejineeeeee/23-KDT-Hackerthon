import 'package:flutter/material.dart';
import 'first_screen.dart';
import 'second_screen.dart';
import 'third_screen.dart';
import 'fourth_screen.dart';


enum TabItem {first, second, third, fourth}

const Map<TabItem, int> tabIdx = {
  TabItem.first: 0,
  TabItem.second: 1,
  TabItem.third: 2,
  TabItem.fourth: 3,
};

Map<TabItem, Widget> tabScreen = {
  TabItem.first: FirstScreen(),
  TabItem.second: SecondScreen(),
  TabItem.third: ThirdScreen(),
  TabItem.fourth: FourthScreen(),
};
