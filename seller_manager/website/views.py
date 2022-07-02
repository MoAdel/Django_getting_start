from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from product.models import Product

# Create your views here.
def welcome(request):
    return render(request,"website/index.html",
                  {'products':Product.objects.all()})

def date(request):
    return HttpResponse("this page was served at " + str(datetime.now()))