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
