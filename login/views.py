from django.http import HttpResponse
from login.models import User
import json

def index(request):
    return HttpResponse('Hello world')

def auth(request):
    print(request.method)
    if request.method == 'POST':
        return HttpResponse('POST')
    try:
        data = json.loads(request.body)
        username = data['username']
        password = data['password']
        print(username, password)
        try:
            foundUsername = User.objects.get(username=username)
            try:
                foundpass = User.objects.get(username=username, password=password)
                return HttpResponse('OK')
            except:
                return HttpResponse('Wrong pass')
        except:
            return HttpResponse('Wrong username')
    except:
        print('nope')
        return HttpResponse('Bad Request')
