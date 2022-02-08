from django.shortcuts import render

from Routes.models import CircuitData

def disclaimer(request):
    return render(request, 'disclaimer.html',{
        'nav':'disclaimer'
    })

def platform(request):
    return render(request, 'platform.html',{
        'nav':'platform'
    })

def index(request):
    arr = CircuitData.objects.all()    
    context = {}
    context['wan_tool'] = arr
    context['nav'] = 'data'
    return render(request, 'index.html',context)

def substation(request,id):
    arr = CircuitData.objects.filter(id= id)    
    context = {}
    context['wan_tool'] = arr
    context['nav'] = 'data'
    return render(request, 'substation.html',context)



