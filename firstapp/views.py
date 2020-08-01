from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from firstapp.models import *
@csrf_exempt
def index(request):
	return render(request,'index.html')
@csrf_exempt
def save(request):
	if request.method=="POST":
		name=request.POST.get('name')
		password=request.POST.get('password')
		a=Registration(name=name,password=password)
		a.save()
		return render(request,"index.html")
	


# Create your views here.
