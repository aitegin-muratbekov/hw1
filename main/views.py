from django.shortcuts import render
import datetime
now = datetime.datetime.now()

# Create your views here.
def about_us(request):
    return render(request, 'index2.html')
def date_now(request):
    dict_ = {
        'date' : now
    }

    return render(request, 'data.html', context=dict_)