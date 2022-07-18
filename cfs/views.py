from django.shortcuts import render
from OrderApp.forms import NewOrderForm


def index(request):
    return render(request, "index.html")
