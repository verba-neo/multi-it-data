# myapp/views.py

from django.shortcuts import render

from django.http import HttpResponse

# view => function
def hello(request):
    return HttpResponse('Hello World!')


def bye(request):
    return HttpResponse('Goodbye My Friend')


def review(request):
    return render(request, 'myapp/review.html')


def index(request):
    return render(request, 'myapp/index.html')


# http://127.0.0.1:8000/yourapp/index/