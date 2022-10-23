import 'package:flutter/material.dart';
import 'dart:async';
import 'choose_device_screen.dart';

class SplashScreen extends StatefulWidget {
  @override
  _SplashScreenState createState() => _SplashScreenState();
}

class _SplashScreenState extends State<SplashScreen> {
  @override
  void initState() {
    super.initState();
    startTime();
  }

  startTime() async {
    var duration = Duration(seconds: 2);
    return Timer(duration, navigateToDeviceScreen);
  }

  navigateToDeviceScreen() {
    Navigator.pushReplacement(
        context, MaterialPageRoute(builder: (context) => ChooseDeviceScreen()));
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Color(0xff4c748b),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text(
              "HOMEBREW",
              style: TextStyle(
                  color: Color(0xffFFFFFF),
                  fontFamily: 'Norwester',
                  fontSize: 48,
                  letterSpacing: 6.0),
            ),
            Text(
              "Great Coffee at Home",
              style: TextStyle(
                  color: Color(0xffFFFFFF),
                  fontFamily: 'Kollektif',
                  fontSize: 18,
                  letterSpacing: 2.0),
            )
          ],
        ),
      ),
    );
  }
}
