import 'package:flutter/material.dart';

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key});

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(title: Text("App")),
        body: ListView(
          //crossAxisAlignment: CrossAxisAlignment.start,
          //mainAxisAlignment: MainAxisAlignment.start,
          children: [
            Text("Baby Yoda"),
            Image.network(
                "https://i.insider.com/5e32f2a324306a19834af322?width=1800&format=jpeg&auto=webp"),
            Row(
              mainAxisAlignment: MainAxisAlignment.end,
              children: [
              IconButton(
              icon: Icon(Icons.favorite),
              onPressed: () {},
            ),
            IconButton(
              icon: Icon(Icons.comment),
              onPressed: () {},
            ),

            Spacer(),

            IconButton(
              icon: Icon(Icons.bookmark_border),
              onPressed: () {},
            ),
            
            ],),

            Text("Baby Yoda"),
            Image.network(
                "https://i.insider.com/5e32f2a324306a19834af322?width=1800&format=jpeg&auto=webp"),
            Row(
              mainAxisAlignment: MainAxisAlignment.end,
              children: [
              IconButton(
              icon: Icon(Icons.favorite),
              onPressed: () {},
            ),
            IconButton(
              icon: Icon(Icons.comment),
              onPressed: () {},
            ),

            Spacer(),

            IconButton(
              icon: Icon(Icons.bookmark_border),
              onPressed: () {},
            ),
            
            ],),


            Text("Baby Yoda"),
            Image.network(
                "https://i.insider.com/5e32f2a324306a19834af322?width=1800&format=jpeg&auto=webp"),
            Row(
              mainAxisAlignment: MainAxisAlignment.end,
              children: [
              IconButton(
              icon: Icon(Icons.favorite),
              onPressed: () {},
            ),
            IconButton(
              icon: Icon(Icons.comment),
              onPressed: () {},
            ),

            Spacer(),

            IconButton(
              icon: Icon(Icons.bookmark_border),
              onPressed: () {},
            ),
            
            ],),

          ],
        ));
  }
}
