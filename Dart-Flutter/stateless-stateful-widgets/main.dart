import 'package:flutter/material.dart';

void main() {
  runApp(MyCoolApplication());
}

class MyCoolApplication extends StatelessWidget {
  const MyCoolApplication({super.key});

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
  int counter = 0;

  void increment(){
    counter++;
    print("$counter");
    setState(() {
      
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("App"),
      ),
      body: Column(children: [ Text("You have pressed the button this many times: "), Text("$counter")],),
      floatingActionButton: FloatingActionButton(child: Icon(Icons.add), onPressed: increment,),
    );
  }
}
