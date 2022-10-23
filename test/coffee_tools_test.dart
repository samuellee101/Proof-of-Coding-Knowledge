import 'package:homebrew/utils/coffee_tools.dart';
import 'package:test/test.dart';

void main() {
  group("cupsToOunces", () {
    test('calculates ounces on 1 cup', () {
      var ounces = CoffeeTools.cupsToOunces(1);
      expect(ounces, 6);
    });

    test('calculates ounces on positive number of cups', () {
      var ounces = CoffeeTools.cupsToOunces(4);
      expect(ounces, 24);
    });

    test('throws ArgumentError on zero', () {
      expect(() => CoffeeTools.cupsToOunces(0), throwsArgumentError);
    });

    test('throws ArgumentError on negative number', () {
      expect(() => CoffeeTools.cupsToOunces(-4), throwsArgumentError);
    });
  });

  group("ratioFrenchPress", () {
    test('calculates coffee to water ratio for French Press', () {
      var ratio = CoffeeTools.ratioFrenchPress(5);
      expect(ratio, 63.36);
    });

    test('throws ArgumentError on zero', () {
      expect(() => CoffeeTools.ratioFrenchPress(0), throwsArgumentError);
    });

    test('throws ArgumentError on negative number', () {
      expect(() => CoffeeTools.ratioFrenchPress(-2), throwsArgumentError);
    });
  });

  group("ouncesToGrams", () {
    test('calculates grams on 6 ounces', () {
      var grams = CoffeeTools.ouncesToGrams(6);
      expect(grams, 177.42);
    });

    test('calculates grams on positive number of ounces', () {
      var grams = CoffeeTools.ouncesToGrams(30);
      expect(grams, 887.1);
    });

    test('throws ArgumentError on zero', () {
      expect(() => CoffeeTools.ouncesToGrams(0), throwsArgumentError);
    });

    test('throws ArgumentError on negative number', () {
      expect(() => CoffeeTools.ouncesToGrams(-4), throwsArgumentError);
    });
  });

  group("ratioDrip", () {
    test('calculates coffee to water ratio for Drip Machine', () {
      var ratio = CoffeeTools.ratioDrip(5);
      expect(ratio, 52.18);
    });

    test('throws ArgumentError on zero', () {
      expect(() => CoffeeTools.ratioDrip(0), throwsArgumentError);
    });

    test('throws ArgumentError on negative number', () {
      expect(() => CoffeeTools.ratioDrip(-4), throwsArgumentError);
    });
  });
}
