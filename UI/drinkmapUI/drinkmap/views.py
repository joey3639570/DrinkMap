from django.shortcuts import render
from .test import dummy
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
    input_dict = {}
    if request.method == 'POST':
        print(request.POST)
        if 'new_store_submit' in request.POST:
            store_name = request.POST.get('store_name')
            store_address = request.POST.get('store_address')
            store_phone = request.POST.get('store_phone')
            input_dict = {'STORE_NAME':store_name, 'STORE_ADDRESS':store_address, 'STORE_PHONE':store_phone}
            
        elif 'new_drink_submit' in request.POST:
            drink_name = request.POST.get('drink')
            drink_price = request.POST.get('price')
            input_dict = {'DRINK_NAME':drink_name, 'DRINK_PRICE':drink_price}
            
        print(input_dict)
        
    return render(request, 'store.html')
    
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
