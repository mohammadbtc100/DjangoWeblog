from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from . import models

# Create your views here.
def articleslist(request):
    articles=models.Article.objects.all().order_by("date")
    args={'articles':articles}
    return render(request,'articles/articlelist.html',context=args)

