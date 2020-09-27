from django.shortcuts import render
from datetime import datetime


def index(request):
    now = datetime.now()
    data = now

    context = {
        'data': data
    }
    return render(request, "core/index.html", context)


