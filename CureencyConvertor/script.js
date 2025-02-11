const apiURL = "https://api.exchangerate-api.com/v4/latest/";

document.addEventListener("DOMContentLoaded", () => {
    fetch(`${apiURL}USD`)
        .then(response => response.json())
        .then(data => {
            let currencies = Object.keys(data.rates);
            let fromSelect = document.getElementById("fromCurrency");
            let toSelect = document.getElementById("toCurrency");

            currencies.forEach(currency => {
                let option1 = new Option(currency, currency);
                let option2 = new Option(currency, currency);
                fromSelect.add(option1);
                toSelect.add(option2);
            });

            fromSelect.value = "USD";
            toSelect.value = "INR";
        });
});

function convertCurrency() {
    let amount = document.getElementById("amount").value;
    let fromCurrency = document.getElementById("fromCurrency").value;
    let toCurrency = document.getElementById("toCurrency").value;
    let resultDisplay = document.getElementById("convertedAmount");
    let historyList = document.getElementById("history");

    if (amount <= 0 || isNaN(amount)) {
        resultDisplay.textContent = "Enter a valid amount!";
        return;
    }

    fetch(`${apiURL}${fromCurrency}`)
        .then(response => response.json())
        .then(data => {
            let rate = data.rates[toCurrency];
            let convertedAmount = (amount * rate).toFixed(2);
            resultDisplay.textContent = `${amount} ${fromCurrency} = ${convertedAmount} ${toCurrency}`;

            let historyItem = document.createElement("li");
            historyItem.textContent = `${amount} ${fromCurrency} → ${convertedAmount} ${toCurrency}`;
            historyList.prepend(historyItem);
        })
        .catch(() => {
            resultDisplay.textContent = "Error fetching exchange rate.";
        });
}

function swapCurrencies() {
    let fromSelect = document.getElementById("fromCurrency");
    let toSelect = document.getElementById("toCurrency");
    [fromSelect.value, toSelect.value] = [toSelect.value, fromSelect.value];
}

function resetConverter() {
    document.getElementById("amount").value = "";
    document.getElementById("convertedAmount").textContent = "--";
    document.getElementById("history").innerHTML = "";
}