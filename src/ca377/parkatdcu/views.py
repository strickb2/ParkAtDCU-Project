from django.shortcuts import render
from django.http import HttpResponse

from .models import Campus, Carpark
import requests

# Create your views here.
def index(request):
    context = {}
    return render(request,"parkatdcu/index.html",context)

def carparks(request):
    context = {}
    webservice_base_url = "http://jfoster.pythonanywhere.com/carparks/"

    campus_name = request.GET['campus']

    campus = Campus.objects.get(name=campus_name)

    carparks = Carpark.objects.filter(campus_id=campus)


    carpark_info = []
    for carpark in carparks:

        webservice_url = webservice_base_url + carpark.name

        realtime_info = requests.get(webservice_url).json()

        if 'spaces_available' in realtime_info:
            spaces_available = realtime_info['spaces_available']
        else:
            spaces_available = 'not available'

        carpark_info.append({
                             'name': carpark.name,
                             'spaces': carpark.spaces,
                             'disabled_spaces': carpark.disabled_spaces,
                             'spaces_available': spaces_available
                             }
                            )

    context['campus'] = campus_name
    context['carparks'] = carpark_info

    return render(request,"parkatdcu/carparks.html",context)
