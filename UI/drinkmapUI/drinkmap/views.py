# -*- coding: utf-8 -*-
from django.shortcuts import render
from .test import dummy, dummy_storeq, dummy_drink_revise, dummy_store_list
from .test import dummy_drinktype_list, dummy_topping_list
import json

import os
import sys
print(os.getcwd())
sys.path.append('SQL')
import sqlMain
# Create your views here.

def validation():
    return "y"

def index(request):
    return render(request, 'homepage.html')

def store(request):
    context = {}
    context_revise_drink = {}
    input_dict = {}
    store_list = dummy_store_list()
    sm = sqlMain.SQLMain()
    context['store_list']=sm.GetShopList()
    global_store_id = 0
    context['drinktype_list'] = sm.GetDrinkList()
    if request.method == 'POST':
        context['request'] = request.POST
        if 'select_store' in request.POST:
            store_number = request.POST.get('select_store')
            context['store_number'] = int(store_number[0])
            df = sm.GetDrink(int(store_number[0]))
            # parsing the DataFrame in json format.
            json_records = df.to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context['d'] = data
        
        elif 'd_drinkname' in request.POST:
            store_id = request.POST.get('storeid')
            drink_name = request.POST.get('d_drinkname')
            drink_type = request.POST.get('drinkclass')
            drink_price = request.POST.get('cost')
            input_dict = {'storeid':store_id, 'drinkname':drink_name, 'drinkclass':drink_type ,'cost':drink_price}
            sm.DeleteDrink(input_dict, confirm_callback = lambda:validation())
            df = sm.GetDrink(store_id)
            # parsing the DataFrame in json format.
            json_records = df.to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context['d'] = data
            context['store_number'] = store_id
        
        elif 'drinkname' in request.POST:
            store_id = request.POST.get('storeid')
            drink_name = request.POST.get('drinkname')
            drink_type = request.POST.get('drinkclass')
            drink_price = request.POST.get('cost')
            input_dict = {'storeid':store_id, 'drinkname':drink_name, 'drinkclass':drink_type ,'cost':drink_price}
            sm.AddDrink(input_dict, confirm_callback = lambda:validation())
            df = sm.GetDrink(store_id)
            # parsing the DataFrame in json format.
            json_records = df.to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context['d'] = data
            context['store_number'] = store_id
            
        elif 'storename' in request.POST:
            store_name = request.POST.get('storename')
            if "'" in store_name:
                i = store_name.index("'")
                store_name = store_name[:i] + "'" + store_name[i:]
            store_time1 = request.POST.get('storetime1')
            store_time2 = request.POST.get('storetime2')
            store_phone = request.POST.get('storephone')
            store_address = request.POST.get('storeaddress')
            input_dict = {'storename':store_name, 'storetime1':store_time1 ,
                            'storetime2':store_time2, 'storephone':store_phone, 'storeaddress':store_address}
            df = sm.AddShop(input_dict, confirm_callback = lambda:validation())
        
        context.update(context_revise_drink)
    return render(request, 'store.html', context)
    
def user(request):
    context = {}
    input_dict = {}
    sm = sqlMain.SQLMain()
    context['drinktype_list'] = sm.GetDrinkList()
    context['topping_list'] = sm.GetItemList()
    if request.method == 'POST':
        price_high = None
        price_low = None
        store_name = None
        # get data
        select1 = request.POST.get('select1')
        select2 = request.POST.get('select2')
        if select1 == 'n':
            select1 = None
        if select2 == 'n':
            select2 = None
        else:
            shop_list = sm.GetShopListByItem(select2)
            context['topping'] = select2
            context['shop'] = shop_list
        if 'price_high' in request.POST:
            price_high = request.POST.get('price_high')
        if 'price_low' in request.POST:
            price_low = request.POST.get('price_low')
        if 'store_name' in request.POST:
            store_name = request.POST.get('store_name')
            if store_name == '':
                store_name = None
        
        input_dict = {'select1':select1,'select2':select2,'price_low':price_low,'price_high':price_high,'store_name':store_name}
        
        df = sm.Query(input_dict)
        # parsing the DataFrame in json format.
        json_records = df.to_json(orient ='records')
        data = []
        data = json.loads(json_records)
        context['d'] = data
    
    return render(request, 'user.html', context)
