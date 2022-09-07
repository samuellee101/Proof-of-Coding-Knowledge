import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
   return MaterialApp(
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key});

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  bool checked = false;

  void toggled(bool? value){
    checked = !checked;
    print(checked);
    setState((){});
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(title: Text("App")),
        body: Column(children: [
        Icon( checked ? Icons.mood : Icons.mood_bad , size: 200,),
        Checkbox(value: checked, onChanged: toggled,),
        ],),
    );
  }
}