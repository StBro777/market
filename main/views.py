from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context: dict = {
        "title": "Home - Главная",
        "content": "Магазин мебели В гостях у StBro",
    }
    return render(request, "main/index.html", context)


def about(request):
    context: dict = {
        "title": "Home - О нас",
        "content": "О нас",
        "text_on_page": "Текст про хороший магазин",
    }
    return render(request, "main/about.html", context)
