import datetime
import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


from .models import Cabinet
from .forms import CabinetForm, UpdateForm
#from .gmap_req import get_current_loc


# Create your views here.

def index(request):
    
    recent_cabinets_list = Cabinet.objects.order_by('pub_date')
    cabinet_loc = []
    for cabinet in recent_cabinets_list:
        cabinet_loc_local = {'cabinet_id' : cabinet.id, 'data' : {'lat' : float(cabinet.lat), 'lng' : float(cabinet.lng)}}
        cabinet_loc.append(cabinet_loc_local)
    

    return render(request, 'cabinets/index.html', {'recent_cabinets_list' : recent_cabinets_list, 'cabinet_loc' : json.dumps(cabinet_loc)})


def detail(request, cabinet_id):

    if request.method == 'POST':
        request.POST = request.POST.copy()
        #giving the ommited fields values
        request.POST['pub_date'] = datetime.datetime.now()
        request.POST['cabinet'] = get_object_or_404(Cabinet, pk=cabinet_id)
        form = UpdateForm(request.POST or None, request.FILES or None)
        print(request.POST)
       
        if form.is_valid():
            try:
                form.save()
            except:
                HttpResponse('some error occurred')
        else:
            form = UpdateForm()
        
        return HttpResponseRedirect(reverse('cabinets:detail', args=(cabinet_id,)))

    elif request.method == 'GET':
        cabinet = get_object_or_404(Cabinet, pk=cabinet_id)
        latest_updates_list = cabinet.update_set.order_by('-pub_date')[:5]
        form = UpdateForm(initial = {'cabinet': cabinet_id })
        context = {
            'form' : form,
            'cabinet': cabinet,
            'latest_updates_list': latest_updates_list,
        }

        
        return render(request, 'cabinets/detail.html', context,)

    else:
        HttpResponse('think your code is brokwen bro')

    
            

def new_cabinet(request):
    if request.method == 'POST':
        form = CabinetForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            form.save()
            try:
                cabinet = Cabinet.objects.last()
                latest_updates_list = cabinet.update_set.order_by('-pub_date')[:5]
                context = {
                    'cabinet': cabinet,
                    'latest_updates_list': latest_updates_list,
                        }
                return render(request, 'cabinets/detail.html', context,)

            except:
                HttpResponse('some error occured.')
            
    else:
        form = CabinetForm()
    return render(request, 'cabinets/new_cabinet.html', {'form': form})