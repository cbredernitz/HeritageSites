from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import HeritageSite
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

def index(request):
	return HttpResponse("Hello, world. You're at the UNESCO Heritage Sites index page.")


class AboutPageView(generic.TemplateView):
	template_name = 'heritagesites/about.html'


class HomePageView(generic.TemplateView):
	template_name = 'heritagesites/home.html'


class SiteListView(generic.ListView):
	model = HeritageSite
	context_object_name = 'sites'
	template_name = 'heritagesites/site.html'
	paginate_by = 50

	def get_queryset(self):
		return HeritageSite.objects.all()\
                                    .select_related('heritage_site_category')\
                                    .order_by('site_name')

class SiteDetailView(generic.DetailView):
	model = HeritageSite
	context_object_name = 'site'
	template_name = 'heritagesites/site_detail.html'


from .models import CountryArea

@method_decorator(login_required, name='dispatch')
class CountryAreaListView(generic.ListView):
	model = CountryArea
	context_object_name = 'country'
	template_name = 'heritagesites/country_area.html'
	paginate_by = 20

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def get_queryset(self):
		return CountryArea.objects.all()\
								  .select_related('dev_status', 'location')\
								  .order_by('country_area_name')

@method_decorator(login_required, name='dispatch')
class CountryAreaDetailView(generic.DetailView):
	model = CountryArea
	context_object_name = 'c'
	template_name = 'heritagesites/country_area_detail.html'

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)
