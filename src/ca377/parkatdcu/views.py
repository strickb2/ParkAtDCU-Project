from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import SearchForm
from .models import Campus, Carpark
import requests

# Create your views here.
def index(request):
    context = {}
    return render(request, "parkatdcu/index.html", context)

def get_name(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/thanks")
    else:
        form = SearchForm()
    return render(request, "parkatdcu/index.html", {"form" : form})

def carparks(request):
    context = {}
    webservice_base_url = "http://jfoster.pythonanywhere.com/carparks/"

    campus_name = request.GET['campus'].lower()
    campuses = Campus.objects.all()
    identified = False
    for campus in campuses:
        if campus.name.lower() == campus_name:
            identified = True
            break
    if identified is False:
        return render(request, "parkatdcu/notfound.html")

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

    context['campus'] = campus
    context['carparks'] = carpark_info

    return render(request,"parkatdcu/carparks.html",context)