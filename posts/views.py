from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render


def main(request):
    if request.method == 'GET':
        return HttpResponse('Hello')


def hello(request):
    if request.method == 'GET':
        return HttpResponse('Hello! Its my project')


def now_date(request):
    now = datetime.now()
    if request.method == 'GET':
        return HttpResponse(now.strftime("%d %B %Y (%A)"))


def bye(request):
    if request.method == 'GET':
        return HttpResponse('Goodbye user!!!')