from django.shortcuts import render
from .test import dummy
import json
# Create your views here.

def index(request):
    return render(request, 'homepage.html')

def store(request):
    return render(request, 'store.html')
    
def user(request):
    context = {}
    if request.method == 'POST':
        price_high = int(request.POST.get('price_high'))
        price_low = int(request.POST.get('price_low'))
        print(request.POST)
        df = dummy(price_low, price_high)
        # parsing the DataFrame in json format.
        json_records = df.to_json(orient ='records')
        data = []
        data = json.loads(json_records)
        context = {'d': data}
    
    return render(request, 'user.html', context)
