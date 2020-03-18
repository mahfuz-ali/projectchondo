from django.http import JsonResponse
from django.shortcuts import render

from .models import *

def home(request):
    return render(request, template_name='search.html')


def data(request):
    context = {

        'division': list(Divisions.objects.values()),
        'category': list(Category.objects.values()),
    }
    return JsonResponse(context, safe=False)


def chondokotha(request):
    query = Chondokotha.objects

    if request.GET.get('division'):
        query = query.filter(district__division=request.GET.get('division'))

    if request.GET.get('district'):
        query = query.filter(district=request.GET.get('district'))

    if request.GET.get('category'):
        query = query.filter(district=request.GET.get('category'))

    context = {

        'chondokotha': list(query.values('id','title','district__division_id','district__division__bn_name','district_id','district__bn_name','category_id','category__bn_name')),

    }

    return JsonResponse(context, safe=False)


def district(request):

    print(request.GET.get('division'))
    query = District.objects
    if request.GET.get('division'):
        query = query.filter(division=request.GET.get('division'))

    context = {
        # 'district': list(District.objects.values()),
        'District': list(query.values()),

    }
    return JsonResponse(context, safe=False)

