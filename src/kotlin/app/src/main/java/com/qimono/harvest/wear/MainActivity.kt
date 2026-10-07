package com.qimono.harvest.wear

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.DropdownMenu
import androidx.compose.material3.DropdownMenuItem
import androidx.compose.material3.OutlinedButton
import androidx.compose.material3.Text
import androidx.compose.material3.TextField
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.wear.compose.material3.MaterialTheme

private val ASSETS = listOf("BTC", "ETH", "SOL", "AAVE", "LINK", "TAO", "SUI", "NEAR", "ZEC", "RONIN", "PUMP")

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent { HarvestScreen() }
    }
}

@Composable
fun HarvestScreen() {
    var asset by remember { mutableStateOf("ETH") }
    var current by remember { mutableStateOf("") }
    var position by remember { mutableStateOf("") }
    var anchor by remember { mutableStateOf("") }
    var result by remember { mutableStateOf<String?>(null) }
    var menuExpanded by remember { mutableStateOf(false) }

    Column(
        modifier = Modifier
            .fillMaxSize()
            .verticalScroll(rememberScrollState())
            .padding(12.dp),
        verticalArrangement = Arrangement.spacedBy(8.dp)
    ) {
        Text("QIMONO HARVEST", style = MaterialTheme.typography.titleMedium)

        Text("Asset")
        OutlinedButton(onClick = { menuExpanded = true }) {
            Text("$asset / USDT")
        }
        DropdownMenu(
            expanded = menuExpanded,
            onDismissRequest = { menuExpanded = false }
        ) {
            ASSETS.forEach { symbol ->
                DropdownMenuItem(
                    text = { Text(symbol) },
                    onClick = {
                        asset = symbol
                        menuExpanded = false
                    }
                )
            }
        }

        TextField(
            value = current,
            onValueChange = { current = it },
            label = { Text("Current price") }
        )
        TextField(
            value = position,
            onValueChange = { position = it },
            label = { Text("Position") }
        )
        TextField(
            value = anchor,
            onValueChange = { anchor = it },
            label = { Text("Material anchor") }
        )

        OutlinedButton(onClick = {
            result = calculateHarvestPreview(current, position, anchor, asset)
        }) {
            Text("CALCULATE")
        }

        result?.let { Text(it) }
    }
}

private fun calculateHarvestPreview(
    currentText: String,
    positionText: String,
    anchorText: String,
    asset: String
): String {
    return try {
        val current = currentText.toBigDecimal()
        val position = positionText.toBigDecimal()
        val anchor = anchorText.toBigDecimal()
        val threshold = anchor + "0.01".toBigDecimal()
        val marketValue = position * current

        if (marketValue < threshold) {
            "WAIT\\nMarket value: $marketValue\\nThreshold: $threshold"
        } else {
            val calculated = (marketValue - anchor) / current
            val half = calculated / "2".toBigDecimal()
            val target = half.setScale(6, java.math.RoundingMode.DOWN)
            "GO TO\\nhttps://www.binance.com/en/convert/$asset/USDT\\nsell $target $asset"
        }
    } catch (_: NumberFormatException) {
        "Enter valid numeric values."
    }
}
