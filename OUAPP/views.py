from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect 
from .models import *
from .config import *

# Create your views here.

def index(request, ):
    # Search_Results = search_results.objects.order_by()
    glogo = app_name.objects.all()
    return render(request, 'OUTempl/index.html', {'glogo': glogo})



def feed(request):
    return render(request, 'OUTempl/feed.html')