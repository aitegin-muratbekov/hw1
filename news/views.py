from django.shortcuts import render, HttpResponse

def main_view(request):
    return HttpResponse('<h1>Welcome to the candy shop</h1>')


# Create your views here.

def index_view(request):
    dict_ = {
        'color': 'red',
        'number': 'five',
        'list': [1, 2, 3, 4]
    }
    return render(request, 'index.html', context=dict_)
