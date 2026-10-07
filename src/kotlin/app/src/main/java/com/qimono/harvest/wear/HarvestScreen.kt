package com.qimono.harvest.wear

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

private val ASSETS = listOf(
    "BTC", "ETH", "SOL", "AAVE", "LINK", "TAO",
    "SUI", "NEAR", "ZEC", "RONIN", "PUMP"
)

@Composable
fun HarvestScreen() {
    var asset by remember { mutableStateOf("ETH") }
    var current by remember { mutableStateOf("") }
    var position by remember { mutableStateOf("") }
    var anchor by remember { mutableStateOf("") }
    var result by remember { mutableStateOf<HarvestPreview?>(null) }
    var error by remember { mutableStateOf<String?>(null) }
    var menuExpanded by remember { mutableStateOf(false) }

    Column(
        modifier = Modifier
            .fillMaxSize()
            .verticalScroll(rememberScrollState())
            .padding(12.dp),
        verticalArrangement = Arrangement.spacedBy(8.dp)
    ) {
        Text("QIMONO HARVEST", style = MaterialTheme.typography.titleMedium)
        Text("Asset / quote: $asset / USDT")

        OutlinedButton(onClick = { menuExpanded = true }) { Text(asset) }

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
            label = { Text("Current") },
            singleLine = true
        )
        TextField(
            value = position,
            onValueChange = { position = it },
            label = { Text("Position") },
            singleLine = true
        )
        TextField(
            value = anchor,
            onValueChange = { anchor = it },
            label = { Text("Anchor") },
            singleLine = true
        )

        OutlinedButton(onClick = {
            try {
                result = calculateHarvest(
                    current.toBigDecimal(),
                    position.toBigDecimal(),
                    anchor.toBigDecimal()
                )
                error = null
            } catch (_: NumberFormatException) {
                result = null
                error = "Enter valid numbers."
            }
        }) { Text("CALCULATE") }

        error?.let { Text(it) }

        result?.let { preview ->
            if (!preview.eligible) {
                Text("WAIT")
                Text("Market value: ${preview.marketValue}")
                Text("Threshold: ${preview.threshold}")
            } else {
                Text("GO TO")
                Text("binance.com/en/convert/$asset/USDT")
                Text("Sell ${preview.target} $asset")
                Text("Receive USDT")
            }
        }
    }
}
