from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def login(request):
    return render(request,'login.html',{})

def doLogin(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    data = {'USERNAME':username,'PASSWORD':password}
    response = requests.post("http://121.199.20.78:8080/tabletpos/control/doLogin",data=data)
    set_cookies = response.headers.get('Set-Cookie')
    webResponse = render(request,'main.html',{})
    if 'JSESSIONID=' in set_cookies:
        jsessionid = set_cookies[set_cookies.index('JSESSIONID=')+11:]
        webResponse.set_cookie('JSESSIONID',jsessionid[:jsessionid.index(';')])

    if 'OFBiz.Visitor=' in set_cookies: 
        visitor = set_cookies[set_cookies.index('OFBiz.Visitor=')+14:]
        webResponse.set_cookie('OFBiz.Visitor',visitor[:visitor.index(';')])

    return webResponse

