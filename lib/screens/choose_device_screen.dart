// ignore_for_file: non_constant_identifier_names

import 'package:flutter/material.dart';
import 'choose_cups_screen.dart';
import 'package:homebrew/utils/coffee_tools.dart';

class ChooseDeviceScreen extends StatefulWidget {
  @override
  _ChooseDeviceScreenState createState() => _ChooseDeviceScreenState();
}

class _ChooseDeviceScreenState extends State<ChooseDeviceScreen> {
  bool frenchPress = false;
  bool dripMachine = false;
  String device = "";

  void french_press() {
    if (dripMachine) {
      frenchPress = !frenchPress;
      dripMachine = !dripMachine;
      device = "frenchPress";
    } else {
      frenchPress = !frenchPress;
      device = "frenchPress";
    }
    setState(() {});
  }

  void drip_machine() {
    if (frenchPress) {
      dripMachine = !dripMachine;
      frenchPress = !frenchPress;
      device = "dripMachine";
    } else {
      dripMachine = !dripMachine;
      device = "dripMachine";
    }
    setState(() {});
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        home: Scaffold(
            body: Container(
      child: Column(mainAxisAlignment: MainAxisAlignment.center, children: <
          Widget>[
        new Container(
            child: Padding(
                padding: EdgeInsets.fromLTRB(0, 0, 0, 10),
                child: Column(children: [
                  Text("What coffee maker are you using?",
                      key: Key('device-selection-text'),
                      style: TextStyle(
                          fontFamily: 'Montserrat',
                          fontSize: 18,
                          color: Color(0xff4C748B)))
                ]))),
        new Container(
          child: Column(
            children: <Widget>[
              OverflowBar(
                overflowDirection: VerticalDirection.down,
                overflowAlignment: OverflowBarAlignment.center,
                children: [
                  new OutlinedButton(
                    key: Key('btn-french-press'),
                    style: OutlinedButton.styleFrom(
                        side: BorderSide(width: 2.0, color: Color(0xff4C748B)),
                        minimumSize: Size(0, 50),
                        maximumSize: Size(300, 50),
                        shape: RoundedRectangleBorder(
                            borderRadius: BorderRadius.circular(10))),
                    child: Align(
                        alignment: Alignment.centerLeft,
                        child: Row(children: [
                          Text('FrenchPress',
                              style: TextStyle(
                                  fontFamily: 'Montserrat',
                                  fontSize: 14,
                                  color: Color(0xff4C748B))),
                          Spacer(),
                          Visibility(
                              visible: frenchPress,
                              child:
                                  Icon(Icons.check, color: Color(0xff4C748B)))
                        ])),
                    onPressed: () {
                      french_press();
                    },
                  ),
                  new OutlinedButton(
                      key: Key('btn-drip-machine'),
                      style: OutlinedButton.styleFrom(
                          side:
                              BorderSide(width: 2.0, color: Color(0xff4C748B)),
                          minimumSize: Size(0, 50),
                          maximumSize: Size(300, 50),
                          shape: RoundedRectangleBorder(
                              borderRadius: BorderRadius.circular(10))),
                      child: Align(
                          alignment: Alignment.centerLeft,
                          child: Row(children: [
                            Text('Drip Machine',
                                style: TextStyle(
                                    fontFamily: 'Montserrat',
                                    fontSize: 14,
                                    color: Color(0xff4C748B))),
                            Spacer(),
                            Visibility(
                                visible: dripMachine,
                                child:
                                    Icon(Icons.check, color: Color(0xff4C748B)))
                          ])),
                      onPressed: () {
                        drip_machine();
                      }),
                ],
              ),
            ],
          ),
        ),
        new Container(
            child: Padding(
                padding: EdgeInsets.fromLTRB(0, 10, 0, 0),
                child: Column(children: [
                  new OutlinedButton(
                      key: Key('continue-btn'),
                      style: OutlinedButton.styleFrom(
                          onSurface: Colors.white,
                          backgroundColor: Color(0xff4C748B),
                          minimumSize: Size(150, 50),
                          maximumSize: Size(200, 50),
                          shape: RoundedRectangleBorder(
                              borderRadius: BorderRadius.circular(50))),
                      child: Column(
                          mainAxisAlignment: MainAxisAlignment.center,
                          children: [
                            Text('Continue',
                                style: TextStyle(
                                    fontFamily: 'Montserrat',
                                    fontSize: 14,
                                    color: Color(0xffFFFFFF))),
                          ]),
                      onPressed: () {
                        if (frenchPress || dripMachine) {
                          Navigator.push(
                              context,
                              MaterialPageRoute(
                                  builder: (context) =>
                                      ChooseCupsScreen(device)));
                        }
                      })
                ])))
      ]),
    )));
  }
}
