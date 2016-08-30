from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.

def main(request):
    return render(request,'main.html',{})

def doTest(request):
    print(request.headers)
    return HttpResponse('just a test')
    #cookies = request.COOKIES
    cookies = {'JSESSIONID':request.COOKIES.get('JSESSIONID'),'OFBiz.Visitor':request.COOKIES.get('OFBiz.Visitor')}
    cookies = dict(cookies)
    #print(cookies)

    #headers = {'user-agent': request.META.get('HTTP_USER_AGENT'),'cookies':cookies}
    #session = requests.session()
    #response = session.post('http://121.199.57.227:8080/webtools/control/login',{'USERNAME':'liyufeng','PASSWORD':'fbcf321b45e1a457'})
    
    #print(session.headers)
    #print(session.cookies)
    #response1 = session.get('http://121.199.57.227:8080/webtools/control/LogView')
    #print(response1.request.headers)

    cookie = 'JSESSIONID='+request.COOKIES.get('JSESSIONID')+'; OFBiz.Visitor='+request.COOKIES.get('OFBiz.Visitor')

    headers = {'User-Agent': request.META.get('HTTP_USER_AGENT'),'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Accept-Encoding':'gzip, deflate, sdch','Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6','Cache-Control':'max-age=0','Connection':'keep-alive','Host':'121.199.20.78:8080','Upgrade-Insecure-Requests':'1','Cookie':cookie}
    #r = requests.get('http://121.199.57.227:8080/webtools/control/LogView',headers=headers)
    r = requests.get('http://121.199.20.78:8080/tabletpos/control/findProductWebPos',{'viewIndex':'0','viewSize':'10'},headers=headers)
    
    #print(r.request.headers)
    print(r.text)
    return HttpResponse('just a test.')
