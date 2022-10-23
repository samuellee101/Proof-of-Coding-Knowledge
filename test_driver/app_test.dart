// Imports the Flutter Driver API.
import 'package:flutter_driver/flutter_driver.dart';
import 'package:test/test.dart';

void main() {
  FlutterDriver driver;

  // Connect to the Flutter driver before running any tests.
  setUpAll(() async {
    driver = await FlutterDriver.connect();
  });

  // Close the connection to the driver after the tests have completed.
  tearDownAll(() async {
    if (driver != null) {
      driver.close();
    }
  });
  group('Happy Paths', () {
    /*
      Given I am on the Coffee Device Selection Screen
      When I tap "French Press"
      And I tap "Continue"
      And I enter "5"
      And I tap "Continue"
      Then I should see "63g - course ground coffee"
      And I should see "887g - water"
    */
    test("should give recommendation for French Press", () async {
      // your code here
      final deviceSelection = find.byValueKey('device-selection-text');
      expect(await driver.getText(deviceSelection),
          "What coffee maker are you using?");

      final btnFrenchPress = find.byValueKey('btn-french-press');
      await driver.tap(btnFrenchPress);

      final btnContinue = find.byValueKey('continue-btn');
      await driver.tap(btnContinue);

      final cupsText = find.byValueKey('cup-text');
      expect(await driver.getText(cupsText), "How many cups would you like?");

      final cupsTextController = find.byValueKey('enter-cups');

      await driver.tap(cupsTextController);
      await driver.enterText('4');
      await driver.waitFor(find.text('4'));

      await driver.tap(btnContinue);

      final recommendedText = find.byValueKey('recommended-text');
      expect(await driver.getText(recommendedText), "Recommended");
      final coffeeRatio = find.byValueKey('coffee-ratio');
      expect(await driver.getText(coffeeRatio), "51g - course ground coffee");
      final waterRatio = find.byValueKey('water-ratio');
      expect(await driver.getText(waterRatio), "710g - water");
      final enjoyText = find.byValueKey('enjoy-text');
      expect(await driver.getText(enjoyText), "Enjoy your delicious coffee");

      final btnDone = find.byValueKey('done-btn');
      await driver.tap(btnDone);
      expect(await driver.getText(deviceSelection),
          "What coffee maker are you using?");
    });

    /*
      Given I am on the Coffee Device Selection Screen
      When I tap "Drip Machine"
      And I tap "Continue"
      And I enter "5"
      And I tap "Continue"
      Then I should see "52g - medium ground coffee"
      And I should see "887g - water"
    */
    test("should give recommendation for Drip Machine", () async {
      //your code here
      final deviceSelection = find.byValueKey('device-selection-text');
      expect(await driver.getText(deviceSelection),
          "What coffee maker are you using?");

      final btnDrip = find.byValueKey('btn-drip-machine');
      await driver.tap(btnDrip);

      final btnContinue = find.byValueKey('continue-btn');
      await driver.tap(btnContinue);

      final cupsText = find.byValueKey('cup-text');
      expect(await driver.getText(cupsText), "How many cups would you like?");

      final cupsTextController = find.byValueKey('enter-cups');

      await driver.tap(cupsTextController);
      await driver.enterText('4');
      await driver.waitFor(find.text('4'));

      await driver.tap(btnContinue);

      final recommendedText = find.byValueKey('recommended-text');
      expect(await driver.getText(recommendedText), "Recommended");
      final coffeeRatio = find.byValueKey('coffee-ratio');
      expect(await driver.getText(coffeeRatio), "42g - course ground coffee");
      final waterRatio = find.byValueKey('water-ratio');
      expect(await driver.getText(waterRatio), "710g - water");
      final enjoyText = find.byValueKey('enjoy-text');
      expect(await driver.getText(enjoyText), "Enjoy your delicious coffee");

      final btnDone = find.byValueKey('done-btn');
      await driver.tap(btnDone);
      expect(await driver.getText(deviceSelection),
          "What coffee maker are you using?");
    });
  });

  /*group('Back Button', () {
    //make up your own tests to check that the back button works
    test("should go back to device selection from choose cups screen",
        () async {
      final btnBack = find.byValueKey('back-btn');
      await driver.tap(btnBack);

      final deviceSelection = find.byValueKey('device-selection-text');
      expect(await driver.getText(deviceSelection),
          "What coffee maker are you using?");
    });

    test(
        "should go to main screen from recommended ratio screen using back button",
        () async {
      final deviceSelection = find.byValueKey('device-selection-text');
      expect(await driver.getText(deviceSelection),
          "What coffee maker are you using?");

      final btnFrenchPress = find.byValueKey('btn-french-press');
      await driver.tap(btnFrenchPress);

      final btnContinue = find.byValueKey('continue-btn');
      await driver.tap(btnContinue);

      final cupsText = find.byValueKey('cup-text');
      expect(await driver.getText(cupsText), "How many cups would you like?");

      final cupsTextController = find.byValueKey('enter-cups');

      await driver.tap(cupsTextController);
      await driver.enterText('4');
      await driver.waitFor(find.text('4'));

      await driver.tap(btnContinue);

      final recommendedText = find.byValueKey('recommended-text');
      expect(await driver.getText(recommendedText), "Recommended");
      final coffeeRatio = find.byValueKey('coffee-ratio');
      expect(await driver.getText(coffeeRatio), "51g - course ground coffee");
      final waterRatio = find.byValueKey('water-ratio');
      expect(await driver.getText(waterRatio), "710g - water");
      final enjoyText = find.byValueKey('enjoy-text');
      expect(await driver.getText(enjoyText), "Enjoy your delicious coffee");

      final btnBack = find.byValueKey('back-btn');
      await driver.tap(btnBack);

      expect(await driver.getText(cupsText), "How many cups would you like?");

      await driver.tap(btnBack);

      expect(await driver.getText(deviceSelection),
          "What coffee maker are you using?");
    });
    //on every page
  });*/
}
