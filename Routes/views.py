from django.shortcuts import render

from Routes.models import CircuitData, LoadData, TransformerData, earthFaultData, phFaultData

def disclaimer(request):
    return render(request, 'disclaimer.html',{
        'nav':'disclaimer'
    })

def platform(request):
    return render(request, 'platform.html',{
        'nav':'platform'
    })

def inputs(request):

    return render(request,'inputs.html',{
        'nav':'inputs',
        'year': range(2022,2070)
    })

def index(request):
    arr = CircuitData.objects.all()    
    context = {}
    context['wan_tool'] = arr
    context['nav'] = 'data'
    return render(request, 'index.html',context)

def transformer_data(request):
    arr = TransformerData.objects.all()    
    context = {}
    context['wan_tool'] = arr
    context['nav'] = 'transformer'
    return render(request, 'transformer_data.html',context)

def load_data(request):
    arr = LoadData.objects.all()    
    context = {}
    context['wan_tool'] = arr
    context['nav'] = 'load'
    return render(request, 'load_data.html',context)

def ph_fault_data(request):
    arr = phFaultData.objects.all()    
    context = {}
    context['wan_tool'] = arr
    context['nav'] = 'ph'
    return render(request, 'ph_faultdata.html',context)

def earth_fault_data(request):
    arr = earthFaultData.objects.all()    
    context = {}
    context['wan_tool'] = arr
    context['nav'] = 'earth'
    return render(request, 'earth_faultdata.html',context)




