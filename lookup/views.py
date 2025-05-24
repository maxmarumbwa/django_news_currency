from django.shortcuts import render
from . import views


# Createf your views here.
def home(request):
    import requests
    import json

    # get crypto currency
    price_request = requests.get(
        "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD"
    )
    price = json.loads(price_request.content)

    # get news item
    api_request = requests.get(
        "https://min-api.cryptocompare.com/data/v2/news/?lang=EN"
    )
    api = json.loads(api_request.content)
    return render(request, "home.html", {"api": api, "price": price})


def about(request):
    return render(request, "about.html", {})


def prices(request):
    if request.method == "POST":
        import requests
        import json

        # get crypto currency
        quote = request.POST["quote"]
        quote = quote.upper()
        crypto_request = requests.get(
            "https://min-api.cryptocompare.com/data/pricemultifull?fsyms="
            + quote
            + "&tsyms=USD"
        )
        crypto = json.loads(crypto_request.content)
        return render(request, "prices.html", {"quote": quote, "crypto": crypto})
    else:
        notfound = "Enter a crypto currency symbol in the form above"
        return render(request, "prices.html", {"notfound": notfound})
