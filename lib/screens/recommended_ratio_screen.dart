import 'package:flutter/material.dart';
import 'choose_device_screen.dart';
import 'package:homebrew/utils/coffee_tools.dart';

class RecommendedRatioScreen extends StatefulWidget {
  double gramsCoffee;
  double gramsWater;
  RecommendedRatioScreen(this.gramsCoffee, this.gramsWater);
  @override
  _RecommendedRatioScreen createState() => _RecommendedRatioScreen();
}

class _RecommendedRatioScreen extends State<RecommendedRatioScreen> {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        home: Scaffold(
            extendBodyBehindAppBar: true,
            backgroundColor: Color(0xffFFFFFF),
            appBar: AppBar(
                backgroundColor: Colors.transparent,
                elevation: 0,
                leading: IconButton(
                  key: Key('back-btn'),
                  icon: Icon(Icons.arrow_back_ios, color: Color(0xff4C748B)),
                  onPressed: () => Navigator.of(context).pop(),
                )),
            body: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                crossAxisAlignment: CrossAxisAlignment.center,
                children: [
                  Align(alignment: Alignment.center),
                  new SizedBox(
                      width: 300,
                      height: 150,
                      child: Container(
                          padding: EdgeInsets.fromLTRB(0, 10, 0, 0),
                          alignment: Alignment.center,
                          decoration: BoxDecoration(
                            border:
                                Border.all(color: Color(0xff4C748B), width: 2),
                            borderRadius: BorderRadius.all(Radius.circular(10)),
                          ),
                          child: Column(children: <Widget>[
                            Text("Recommended",
                                key: Key('recommended-text'),
                                style: TextStyle(
                                    fontFamily: 'Kollektif',
                                    fontSize: 18,
                                    letterSpacing: 1,
                                    color: Color(0xff4C748B))),
                            Divider(
                                color: Color(0xff4C748B),
                                thickness: 2,
                                indent: 20,
                                endIndent: 20),
                            new Container(
                                padding: EdgeInsets.fromLTRB(0, 10, 0, 0),
                                child: Column(children: [
                                  Text(
                                      "${widget.gramsCoffee.round()}g - course ground coffee",
                                      key: Key('coffee-ratio'),
                                      style: TextStyle(
                                          fontFamily: 'Kollektif',
                                          fontSize: 14,
                                          letterSpacing: 1,
                                          color: Color(0xff4C748B))),
                                  Text("${widget.gramsWater.round()}g - water",
                                      key: Key('water-ratio'),
                                      style: TextStyle(
                                          fontFamily: 'Kollektif',
                                          fontSize: 14,
                                          letterSpacing: 1,
                                          color: Color(0xff4C748B))),
                                  new Container(
                                      padding: EdgeInsets.fromLTRB(0, 35, 0, 0),
                                      child: Column(
                                        children: [
                                          Text("Enjoy your delicious coffee",
                                              key: Key('enjoy-text'),
                                              style: TextStyle(
                                                  fontFamily: 'Montserrat',
                                                  fontSize: 10,
                                                  letterSpacing: 1,
                                                  color: Color(0xff4C748B)))
                                        ],
                                      ))
                                ])),
                          ]))),
                  new Container(
                      child: Padding(
                          padding: EdgeInsets.fromLTRB(0, 10, 0, 0),
                          child: Column(children: [
                            new OutlinedButton(
                                key: Key('done-btn'),
                                style: OutlinedButton.styleFrom(
                                    onSurface: Colors.white,
                                    backgroundColor: Color(0xff4C748B),
                                    minimumSize: Size(150, 50),
                                    maximumSize: Size(200, 50),
                                    shape: RoundedRectangleBorder(
                                        borderRadius:
                                            BorderRadius.circular(50))),
                                child: Column(
                                    mainAxisAlignment: MainAxisAlignment.center,
                                    children: [
                                      Text('Done',
                                          style: TextStyle(
                                              fontFamily: 'Montserrat',
                                              fontSize: 14,
                                              color: Color(0xffFFFFFF))),
                                    ]),
                                onPressed: () {
                                  Navigator.push(
                                      context,
                                      MaterialPageRoute(
                                          builder: (context) =>
                                              ChooseDeviceScreen()));
                                })
                          ])))
                ])));
  }
}
