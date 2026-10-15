# Kotlin Wear OS scaffold

A calculator-style Wear OS UI for the Qimono 50% harvest rule.

## UI

The initial scaffold provides:

- Asset/currency selector
- Current-price input
- Position input
- Material-anchor input
- Calculate button
- WAIT / GO TO Binance result

The default quote currency is **USDT** because that is the current crypto harvest settlement convention.

## Project layout

```text
src/kotlin/
├── settings.gradle.kts
├── build.gradle.kts
├── gradle.properties
└── app/
    ├── build.gradle.kts
    └── src/main/
        ├── AndroidManifest.xml
        ├── java/com/qimono/harvest/wear/MainActivity.kt
        └── res/values/styles.xml
```

This is a UI scaffold, not an execution client. It does not authenticate with Binance or place trades.

For a production Wear OS build, pin the Android/Compose versions to the toolchain used by the project and add the Gradle wrapper from the selected Android Studio distribution.
