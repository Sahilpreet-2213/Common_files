from django.shortcuts import render
import json ,os 
from .models import *

with open('conf.json','r') as file:
    param=json.load(file)['data']

def index(request):
    return render(request,'first.html',param)

def img_submition(request,methods=["POST"]):
    if (request.method == 'POST') and (request.POST.get('post_submit',' ') != ''):
        images=request.POST.get('post_submit',' ')
        data=Images(images=images)
        if data != None:
            data.save()
    
    elif request.method == 'POST':
        images=request.POST.get('post_del',' ')
        Images.objects.filter(images=images).delete()
        print('process executed')
    return render(request,'img_submition.html')

def message(request,methods=['POST']):
    if request.method == 'POST':
        name=request.POST.get('name','')
        phone=request.POST.get('phone','')
        mail=request.POST.get('mails','')
        msg=request.POST.get('message','')
        # print(name,phone,mail,msg)
        contact=Contact(name=name,phone=phone,mail=mail,message=msg)
        contact.save()
    return render(request,'message.html')

def sign_in(request,methods=['POST']):
    username = request.POST.get('user')
    password = request.POST.get('pass')
    print(f' Username: {username} \nPassword: {password}')
    if (username==param['admin_user'] and (password==param['admin_pass'])):
        return render(request,'img_submition.html',param)
    return render(request,'sign_in.html',param)

def images(request):
    data=Images.objects.all()
    params={'images':data}
    return render(request,'images.html',params)