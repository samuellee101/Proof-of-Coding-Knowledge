import 'package:flutter/material.dart';
import 'package:homebrew/screens/recommended_ratio_screen.dart';
//import '../recommended_ratio_screen.dart';
import 'package:homebrew/utils/coffee_tools.dart';

class ChooseCupsScreen extends StatefulWidget {
  String device;
  ChooseCupsScreen(this.device);
  @override
  _ChooseCupsScreenState createState() => _ChooseCupsScreenState();
}

class _ChooseCupsScreenState extends State<ChooseCupsScreen> {
  final cupsOfCoffee = TextEditingController();
  int cups;
  double gramsCoffee;
  double gramsWater;
  int ouncesWater;
  bool enable = false;
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
            body: Container(
                alignment: Alignment.center,
                child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: <Widget>[
                      new Container(
                          child: Padding(
                              padding: EdgeInsets.fromLTRB(0, 0, 0, 10),
                              child: Column(children: [
                                Text("How many cups would you like?",
                                    key: Key('cup-text'),
                                    style: TextStyle(
                                        fontFamily: 'Montserrat',
                                        fontSize: 18,
                                        color: Color(0xff4C748B)))
                              ]))),
                      new SizedBox(
                          width: 300,
                          height: 40,
                          child: TextField(
                            key: Key('enter-cups'),
                            style: TextStyle(
                                fontFamily: 'Montserrat',
                                fontSize: 14,
                                color: Color(0xff4C748B)),
                            decoration: new InputDecoration(
                              enabledBorder: const OutlineInputBorder(
                                  borderSide: const BorderSide(
                                      color: Color(0xff4C748B), width: 2)),
                              contentPadding: EdgeInsets.symmetric(
                                  vertical: 1, horizontal: 20),
                            ),
                            textAlign: TextAlign.left,
                            textAlignVertical: TextAlignVertical.center,
                            controller: cupsOfCoffee,
                            keyboardType: TextInputType.number,
                            onChanged: (cupsOfCoffee) {
                              cups = int.parse(cupsOfCoffee);
                              if (cups > 0) {
                                enable = true;
                                // ignore: unrelated_type_equality_checks
                                if (widget.device == "frenchPress") {
                                  gramsCoffee =
                                      CoffeeTools.ratioFrenchPress(cups);
                                  ouncesWater = CoffeeTools.cupsToOunces(cups);
                                  gramsWater =
                                      CoffeeTools.ouncesToGrams(ouncesWater);
                                } else if (widget.device == "dripMachine") {
                                  gramsCoffee = CoffeeTools.ratioDrip(cups);
                                  ouncesWater = CoffeeTools.cupsToOunces(cups);
                                  gramsWater =
                                      CoffeeTools.ouncesToGrams(ouncesWater);
                                }
                              }
                            },
                          )),
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
                                            borderRadius:
                                                BorderRadius.circular(50))),
                                    child: Column(
                                        mainAxisAlignment:
                                            MainAxisAlignment.center,
                                        children: [
                                          Text('Continue',
                                              style: TextStyle(
                                                  fontFamily: 'Montserrat',
                                                  fontSize: 14,
                                                  color: Color(0xffFFFFFF))),
                                        ]),
                                    onPressed: () {
                                      if (enable) {
                                        Navigator.push(
                                            context,
                                            MaterialPageRoute(
                                                builder: (context) =>
                                                    RecommendedRatioScreen(
                                                        gramsCoffee,
                                                        gramsWater)));
                                      }
                                    })
                              ])))
                    ]))));
  }
}
