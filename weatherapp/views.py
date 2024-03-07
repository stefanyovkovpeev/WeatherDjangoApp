import json
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from weatherapp.app import App
from weatherapp.models import RandomCityData



def home(request):
    try:
        return render(request, "base.html")
    except Exception as e:
        raise Http404("Service Unavailable Currently.")

def randomcities(request):
    try:
        function = App()
        if request.method == "POST":
            action = request.POST.get("action")
            if action == "generate":
                RandomCityData.objects.all().delete()
                function.random_cities_generator()
                function.get_weather(function.cities)
                cities_data = function.get_weather_data()
                return render(request, "randomcities.html", {"cities": cities_data})
            elif action == "refresh":
                function.get_weather(function.cities)
                cities_data = function.get_weather_data()
                RandomCityData(data=cities_data).save()
                if RandomCityData.objects.count() > 10:
                    oldest_instance = RandomCityData.objects.order_by('date').first()
                    oldest_instance.delete()
                return render(request, "randomcities.html", {"cities": cities_data})
        elif request.method == "GET":
            function.get_weather(function.cities)
            cities_data = function.get_weather_data()
            return render(request, "randomcities.html", {"cities": cities_data})
    except Exception as e:
        raise Http404("Service Unavailable Currently.")

def search_city(request):
    try:
        function = App()
        if request.method == "POST":
            search_query = request.POST.get("search_query")
            cities_data = function.search_city(search_query)
            return render(request, "searchedcity.html", {"city_info": cities_data})
        else:
            return redirect(reverse('home'))
    except Exception as e:
        raise Http404("Service Unavailable Currently.")

def comparelast10(request):
    try:
        function = App()
        if request.method == "GET":
            last_10_results, last_10_stamps = function.get_last_10()
            zipped_results = zip(last_10_results, last_10_stamps)
            return render(request, "comparelast10.html", {"zipped_results": zipped_results})
    except Exception as e:
        raise Http404("Service Unavailable Currently.")

def refresh_data(request):
    try:
        function = App()
        if request.method == "GET":
            last_10_results, last_10_stamps = function.get_last_10()
            zipped_results = zip(last_10_results, last_10_stamps)
            return render(request, "comparelast10.html", {"zipped_results": zipped_results})
        elif request.method == "POST":
            last_10_results, last_10_stamps = function.get_last_10()
            zipped_results = zip(last_10_results, last_10_stamps)
            return render(request, "comparelast10.html", {"zipped_results": zipped_results})
    except Exception as e:
        raise Http404("Service Unavailable Currently.")