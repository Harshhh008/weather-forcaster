from django.shortcuts import render
import json
import urllib.request
# Create your views here.
API_KEY = '884c625e0d73441686c0129000d9aaba'
def index(request):
    if request.method == "POST":
        city = request.POST['city']
        url = urllib.request.urlopen(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}')
        json_data = json.load(url)
        data = {
            'country_code' : str(json_data['sys']['country']),
            'coordinate': str(json_data['coord']['lon'])+' '+str(json_data['coord']['lat']),
            'temp': str(round(json_data['main']['temp']-273.15,2)),
            'pressure': str(json_data['main']['pressure']),
            'humidity': str(json_data['main']['humidity'])
        }
    else:
        data = {}
        city = ''
    return render(request,'index.html',{'data':data,'city':city})
