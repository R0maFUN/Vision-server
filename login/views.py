from django.http import HttpResponse
from login.models import User
import json
from django.views.decorators.csrf import csrf_exempt
import enum

class ResponseCode(enum.Enum):
    success           = "200"
    badRequest        = "400"
    wrongUsername     = "418"
    wrongPassword     = "419"
    usernameDuplicate = "420"
    mailDuplicate     = "421"


@csrf_exempt
def index(request):
    return HttpResponse('Hello world')

@csrf_exempt
def auth(request):
    print("method: " + request.method)
    if request.method != 'GET':
        return HttpResponse(ResponseCode.badRequest.value)
    try:
        data     = json.loads(request.body)
        username = data['username']
        password = data['password']
        print(username, password)
        try:
            foundUsername = User.objects.get(username__iexact=username)
            try:
                foundpass = User.objects.get(username__iexact=username, password=password)
                return HttpResponse(ResponseCode.success.value)
            except:
                return HttpResponse(ResponseCode.wrongPassword.value)
        except:
            return HttpResponse(ResponseCode.wrongUsername.value)
    except:
        print('nope')
        return HttpResponse(ResponseCode.badRequest.value)

@csrf_exempt
def checkLoginForDuplicating(request):
    if request.method != 'GET':
        return HttpResponse(ResponseCode.badRequest.value)
    try:
        data     = json.loads(request.body)
        username = data['username']
        try:
            foundUsername = User.objects.get(username__iexact=username)
            return HttpResponse(ResponseCode.usernameDuplicate.value)
        except:
            return HttpResponse(ResponseCode.success.value)
    except:
        return HttpResponse(ResponseCode.badRequest.value)

@csrf_exempt
def registration(request):
    if request.method != 'POST':
        return HttpResponse(ResponseCode.badRequest.value)
    try:
        data     = json.loads(request.body)
        username = data['username']
        password = data['password']
        email    = data['email']
        print(username + " " + password + " " + email)
        User(username=username, password=password, email=email).save()
        return HttpResponse(ResponseCode.success.value)
    except:
        return HttpResponse(ResponseCode.badRequest.value)