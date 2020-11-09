from django.shortcuts import render
from django.http import HttpResponse
import requests
from .models import Carpark, Campus

# Create your views here.
def index(request):
    carpark_data = Carpark.objects.all()
    campus_data = Campus.objects.all()
    nullcarparks = Campus.objects.filter(campus=None)
    json = []
    for park in carpark_data:
        url = "https://jfoster.pythonanywhere.com/carparks/" + str(park)
        res = requests.get(url)
        json_data = res.json()
        if "error_msg" in json_data:
            json.append([park, "real time info not available"])
        else:
            json.append([park, str(json_data["spaces_available"]) + " spaces available"])

    context = {
        "carpark_data" : carpark_data,
        "campus_data" : campus_data,
        "nullcarparks" : nullcarparks,
        "json" : json
    }

    # retrieve carpark information from the database
    # add it to the context dictionary
    
    return render(request,"parkatdcu/index.html",context)
