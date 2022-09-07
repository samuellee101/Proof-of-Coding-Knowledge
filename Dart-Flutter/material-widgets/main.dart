import 'package:flutter/material.dart';

void main(){
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(home: MyHomePage());
  }
}

class MyHomePage extends StatelessWidget {
  void Nothing(){

  }
  const MyHomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("App"), backgroundColor: Colors.amber, actions: [Icon(Icons.alarm_off), Icon(Icons.play_arrow)],),
      body: Column(children: [
        Text("howdy", style: TextStyle(fontSize: 24, color: Colors.blue, fontWeight: FontWeight.w900)),
        Icon(Icons.stop, color: Colors.red,),
        ElevatedButton(child: Text("click",  style: TextStyle(color: Colors.indigo)), onPressed: Nothing),
        TextField(),
        Image.network("https://clipart.world/wp-content/uploads/2020/09/Fire-clipart-5.png", height: 200.0, width: 200.0,),
      ],),
    );
  }
}