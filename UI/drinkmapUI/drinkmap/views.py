from django.shortcuts import render
from .test import dummy, dummy_storeq, dummy_drink_revise, dummy_store_list
import json

import os
import sys
print(os.getcwd())
sys.path.append('SQL')
import sqlMain
# Create your views here.

def index(request):
    return render(request, 'homepage.html')

def store(request):
    context = {}
    context_revise_drink = {}
    context_insert_store = {}
    input_dict = {}
    store_list = dummy_store_list()
    context['store_list']=store_list
    if request.method == 'POST':
        if 'select_store' in request.POST:
            store_number = request.POST.get('select_store')
            df = dummy_storeq(int(store_number[0]))
            # parsing the DataFrame in json format.
            json_records = df.to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            
        elif 'drinkname' in request.POST:
            drink_name = request.POST.get('drinkname')
            drink_type = request.POST.get('drinktype')
            drink_price = request.POST.get('cost')
            input_dict = {'drinkname':drink_name, 'drinktype':drink_type ,'cost':drink_price}
            df = dummy_drink_revise(input_dict)
            print(df)
            # parsing the DataFrame in json format.
            json_records = df.to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context_revise_drink = {'r': data}
            
        elif 'store_name' in request.POST:
            store_name = request.POST.get('storename')
            store_time1 = request.POST.get('storetime1')
            store_time2 = request.POST.get('storetime2')
            store_phone = request.POST.get('storephone')
            input_dict = {'storename':store_name, 'storetime1':store_time1 ,'storetime2':store_time2, 'storephone':store_phone}
            df = dummy_drink_revise(input_dict)
            print(df)
            # parsing the DataFrame in json format.
            json_records = df.to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context_insert_store = {'e': data}
        
        context.update(context_revise_drink)
        context.update(context_insert_store)
    return render(request, 'store.html', context)
    
def user(request):
    context = {}
    sm = sqlMain.SQLMain()
    if request.method == 'POST':
        #price_high = int(request.POST.get('price_high'))
        #price_low = int(request.POST.get('price_low'))
        #print(request.POST)
        df = sm.Query(request.POST)
        # parsing the DataFrame in json format.
        json_records = df.to_json(orient ='records')
        data = []
        data = json.loads(json_records)
        context = {'d': data}
    
    return render(request, 'user.html', context)
