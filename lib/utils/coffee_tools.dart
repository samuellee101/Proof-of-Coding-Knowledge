class CoffeeTools {
  String _device;

  CoffeeTools(String device) {
    _device = device;
  }

  String device() {
    return _device;
  }

  // Input: number of cups (positive integer)
  // Output: number of ounces in a cup
  static int cupsToOunces(int cups) {
    if (cups <= 0) {
      throw ArgumentError();
    }
    return cups * 6;
  }

  static double ratioDrip(int cups) {
    int oWater = cupsToOunces(cups);
    double gWater = ouncesToGrams(oWater);
    double gCoffee = double.parse((gWater / 17).toStringAsFixed(2));
    return gCoffee;
  }

  static double ouncesToGrams(int ounces) {
    if (ounces <= 0) {
      throw ArgumentError();
    }
    return double.parse(((ounces / 6) * 177.42).toStringAsFixed(2));
  }

  static double ratioFrenchPress(int cups) {
    int oWater = cupsToOunces(cups);
    double gWater = ouncesToGrams(oWater);
    double gCoffee = double.parse((gWater / 14).toStringAsFixed(2));
    return gCoffee;
  }
}
