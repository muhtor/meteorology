from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from .models import Forecast
from .utils import WeatherController
from .forms import CityForm


class DashboardView(View):
    template_name = 'index.html'

    def get(self, request):
        # return render(request, self.template_name)
        return redirect('list')


class AddNewRegionView(View, WeatherController):
    template_name = 'weather/add-region.html'
    form = CityForm

    def get(self, request):
        context = {'form': self.form(), 'is_added': False}
        return render(request, 'weather/add-region.html', context)

    def post(self, request):
        form = self.form(request.POST)
        city = form.save()
        city_weather = self.fetch_one(city=city)
        context = {'city_weather': city_weather, 'form': form, 'is_added': True}
        return render(request, 'weather/add-region.html', context)


class WeatherListView(ListView):
    template_name = 'weather/list.html'
    queryset = Forecast.objects.all()
    context_object_name = 'object_list'

    def get_queryset(self):
        query = self.request.GET.get('name', None)
        qs = Forecast.objects.all()
        if query:
            qs = qs.filter(city__name__icontains=query)
        return qs

