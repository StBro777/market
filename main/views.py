from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context: dict = {
        "title": "Home",
        "content": "Главная страница магазина - HOME",
        "list": ["first", "second"],
        "dict": {"first": 1},
        "bool": True,
    }
    return render(request, "main/index.html", context)


def about(request):
    return HttpResponse("About page")
