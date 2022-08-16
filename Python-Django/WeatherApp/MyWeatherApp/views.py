from django.shortcuts import render
from django.http import HttpResponse

#Request to API returns json file
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        # https: // api.openweathermap.org / data / 2.5 / weather?q = North & Carolina, us & APPID = bd887c19b926086fe67de0e4e872eee9
        res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+
                                     '&APPID=bd887c19b926086fe67de0e4e872eee9').read()
        json_data = json.loads(res)
        print('Json Data: ',json_data)
        # print('Json data: ',json.dump(json_data))
        data = {
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon']) + ' ' +
            str(json_data['coord']['lat']),
            "temp": str(json_data['main']['temp']) + 'k',
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
        }

        print('data: ',data)
    else:
        city = ''
        data = {}
    print('data: ',data)
    # print('json_data: ',json_data)
    return render(request, 'index.html', {'city': city, 'data': data})
    # return HttpResponse('<h1>Hey, Welcome</h1>')

