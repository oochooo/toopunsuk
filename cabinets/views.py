import datetime
import json
import requests
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


from .models import Cabinet
from .forms import CabinetForm, UpdateForm

def index(request):
    
    recent_cabinets_list = Cabinet.objects.order_by('pub_date')
    cabinet_loc = []
    for cabinet in recent_cabinets_list:
        cabinet_loc_local = {'cabinet_id' : cabinet.id, 'data' : {'lat' : float(cabinet.lat), 'lng' : float(cabinet.lng)}}
        cabinet_loc.append(cabinet_loc_local)
    

    return render(request, 'cabinets/index.html', {'recent_cabinets_list' : recent_cabinets_list, 'cabinet_loc' : json.dumps(cabinet_loc)})

def privacy_policy(request):
    return render(request, 'cabinets/privacy_policy.html')

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
            try:
                form.save()
                cabinet = Cabinet.objects.last()
                context = {
                    'cabinet': cabinet,
                        }
                return redirect('cabinets:detail', cabinet_id = cabinet.id)

            except:
                HttpResponse('encountered an error while saving your form. soz. plz try again...')
            
    else:
        print('else block')
        form = CabinetForm()
    return render(request, 'cabinets/new_cabinet.html', {'form': form})

def covid_dashboard(request):
    #try to infitinity scroll this using paginating ?

    if request.method == 'GET':
    
        try:
            resp = requests.get('https://covid19.th-stat.com/api/open/cases')
            covid_dict2 = resp.json()['Data']
            covid_list_to_print = []
            for x in covid_dict2:
                if x['StatQuarantine']:
                    state_q = 'In state q'
                elif not x['StatQuarantine']:
                    state_q = 'Community'
                covid_list_to_print.append(f"Patient #{x['No']} -- {x['GenderEn']}, {x['Age']}  --  positive {x['ConfirmDate'][5:10]} -- {x['ProvinceEn']} -- {x['NationEn']} -- {state_q}")
            last_api_date = f"Updated: {covid_dict2[0]['ConfirmDate']}. Showing [:200]. Source: https://ddc.moph.go.th/viralpneumonia/index.php"
            #avg_age = (sum([x['Age'] for x in covid_dict2]) / len(covid_dict2))
            context = {
                'covid_list_to_print' : covid_list_to_print[:200],
                'last_api_date' : last_api_date
            }

        except requests.exceptions.RequestException as e:
            raise SystemExit(e)


        return render(request, 'cabinets/covid_dashboard.html', context,)