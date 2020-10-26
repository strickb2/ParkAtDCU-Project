from django.shortcuts import render
from django.http import HttpResponse
from .models import Carpark, Campus

# Create your views here.
def index(request):
    carpark_data = Carpark.objects.all()
    campus_data = Campus.objects.all()
    nullcarparks = Campus.objects.filter(campus=None)

    context = {
        "carpark_data" : carpark_data,
        "campus_data" : campus_data,
        "nullcarparks" : nullcarparks
    }

    # retrieve carpark information from the database
    # add it to the context dictionary
    
    return render(request,"parkatdcu/index.html",context)
