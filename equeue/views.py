from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseForbidden
import datetime
from django.utils.timezone import now

# Create your views here.
def renderIndex(request):
    return HttpResponse('go go go')


# Create your views here.
def renderIndex2(request):
    today = datetime.date.today()
    time = now()
    return render(request, 'index.html', {'name': 'Shahin',
                                          'today': today,
                                          'time' : time})