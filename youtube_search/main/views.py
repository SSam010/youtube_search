from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    data = {'title': 'Этот сайт создан в рамках обучения работы с DJANGO',
            'values': ['ВДудь', 'BadComedian', 'ещёнепознер'],
            }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')
