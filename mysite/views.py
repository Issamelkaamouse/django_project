from django.http import HttpResponse
from django.shortcuts import render


def index_project(request):
    # return HttpResponse("Hello")
    return render(request, "base.html")
