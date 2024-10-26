from django.shortcuts import render


def index(request):
    return render(
        request,
        "vla_django/index.html",
    )
