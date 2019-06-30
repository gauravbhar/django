from django.shortcuts import render
from django.http import HttpResponse
from .models import Reported,Article


# Create your views here.
def index(request):
    return HttpResponse("hello")

def heading(request,Reported_id):
	return HttpResponse("todays headline%s",Reported_id)

def year_achieve(request,year):
	alist = Article.objects.filter(pub_date=year)
	context={"year":year,"article_list":alist}
	return render(request,"project1/index.html",context)







