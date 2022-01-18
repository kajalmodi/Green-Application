from django.shortcuts import render,redirect
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User, auth
from django.http import HttpResponse,JsonResponse
import requests
import pymysql
from django.contrib.auth.forms import UserCreationForm 
from .models import esp11, esp12,esp21,esp22,esp31,esp32,esp41,esp42

# Create your views here.
#code for create new account for user
def createaccount(request):
    if request.method == 'POST':
        #taking values form htnl form with id.
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        password = request.POST['password']
        repassword = request.POST['re-password']
        if password == repassword:
            if User.objects.filter(username=username).exists():
                return redirect('createaccount')
            else:
                #uploading users details  intouser database
                user = User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name)
                user.save()# save all details given by user into database
                return redirect('login')
    else:   
        return render(request,'createaccount.html')
# Code for login form
def login(request):
    #taking data form user html
    userlog = request.POST.get('usernamelog')
    passlog = request.POST.get('passwordlog')
    if request.method== 'POST':
        user = auth.authenticate(username=userlog,password=passlog)
        if user is not None:# checking that user is authenticatied of not
            auth.login(request,user)
            request.session['is_login'] = True # here we are starting a session
            return redirect("camera")#if user is authenticate user then redirect him to camera page
        else:
            return redirect('login')
    else:
        return render(request,'login.html') # else redirect user into login page dont get him loged in

def controlmotor(request):# For controlmotor page
    if request.session.has_key('is_login'):
        return render(request,'controlmotor.html')
    else:
        return redirect('login')
    

def camera(request):#For Camera page
    if request.session.has_key('is_login'):
        return render(request,'camera.html')
    else:
        return redirect('login')
    

def row1(request):# For Row1 page
    if request.session.has_key('is_login'):
        return render(request,'row1.html')
        
    else:
        return redirect('login')
  
def row2(request):# For Row2 page
    if request.session.has_key('is_login'):
        return render(request,'row2.html')
    else:
        return redirect('login')
 
def temperature(request):# For temperature page
    if request.session.has_key('is_login'):
        return render(request,'temperature.html')
    else:
        return redirect('login')

def airdust(request):#For airdust page
    if request.session.has_key('is_login'):
        return render(request,'airdust.html')
    else:
        return redirect('login')
    
def history(request):#For history page 
    if request.session.has_key('is_ogin'):
        #code for accessing the data in the database 
        esp_11=esp11.objects.all() 
        esp_12=esp12.objects.all()
        esp_21=esp21.objects.all()
        esp_22=esp22.objects.all()
        esp_31=esp31.objects.all()
        esp_32=esp32.objects.all()
        esp_41=esp41.objects.all()
        esp_42=esp42.objects.all()     
        return render(request,'history.html',
        {'esp_11':esp_11,
        'esp_12':esp_12,
        'esp_21':esp_21,
        'esp_22':esp_22,
        'esp_31':esp_31,
        'esp_32':esp_32,
        'esp_41':esp_41,
        'esp_42':esp_42,
        })
    else:
        return redirect('login')
    
def logout(request):# session is complete, deleting session key
    del request.session['is_login']
    return redirect('login')

def temp(request):#temp is for taking data form api and storing it to the data base
    url = "http://127.0.0.1:8080/data" # data coming with this url
    response = requests.get(url)
    data = response.json()
    copydata = data
    #block_1/esp11
    esp11Data=esp11(status=copydata['block_1']['esp11']['status'],
    topic=copydata['block_1']['esp11']['topic'],
    moisturevalue=copydata['block_1']['esp11']['SoilMoistureSensor']['value'])
    esp11Data.save()
    #block_1/esp12
    esp12Data=esp12(status=copydata['block_1']['esp12']['status'],
    topic=copydata['block_1']['esp12']['topic'],
    moisturevalue=copydata['block_1']['esp12']['SoilMoistureSensor']['value'])
    esp12Data.save()
    #block_2/esp21
    esp21Data=esp21(status=copydata['block_2']['esp21']['status'],
    topic=copydata['block_2']['esp21']['topic'],
    moisturevalue=copydata['block_2']['esp21']['SoilMoistureSensor']['value'])
    esp21Data.save()
    #block_2/esp22
    esp22Data=esp22(status=copydata['block_2']['esp22']['status'],
    topic=copydata['block_2']['esp22']['topic'],
    moisturevalue=copydata['block_2']['esp22']['SoilMoistureSensor']['value'])
    esp22Data.save()
    #block_3/esp31
    esp31Data=esp31(status=copydata['block_3']['esp31']['status'],
    topic=copydata['block_3']['esp31']['topic'],
    moisturevalue=copydata['block_3']['esp31']['SoilMoistureSensor']['value'])
    esp31Data.save()
    #block_3/esp32
    esp32Data=esp32(status=copydata['block_3']['esp32']['status'],
    topic=copydata['block_3']['esp32']['topic'],
    moisturevalue=copydata['block_3']['esp32']['SoilMoistureSensor']['value'])
    esp32Data.save()
    #block_4/esp41
    esp41Data=esp41(
    status=copydata['block_4']['esp41']['status'],
    topic=copydata['block_4']['esp41']['topic'],
    moisturevalue=copydata['block_4']['esp41']['SoilMoistureSensor']['value'],
    pm03=copydata['block_4']['esp41']['AirSensor']['PM03'],
    pm05=copydata['block_4']['esp41']['AirSensor']['PM05'],
    pm10=copydata['block_4']['esp41']['AirSensor']['PM10'],
    pm25=copydata['block_4']['esp41']['AirSensor']['PM25'],
    pm50=copydata['block_4']['esp41']['AirSensor']['PM50'],
    pm100=copydata['block_4']['esp41']['AirSensor']['PM100'],
    humidity=copydata['block_4']['esp41']['AirSensor']['humidity'],
    temperatureEsp=copydata['block_4']['esp41']['AirSensor']['temperature'],
    soiltempC=copydata['block_4']['esp41']['TemperatureSensor']['temperatureC'],
    soiltempF=copydata['block_4']['esp41']['TemperatureSensor']['temperatureF'])
    esp41Data.save()
    #block_4/esp42
    esp42Data=esp42(status=copydata['block_4']['esp42']['status'],
    topic=copydata['block_4']['esp42']['topic'],
    moisturevalue=copydata['block_4']['esp42']['SoilMoistureSensor']['value'])
    esp42Data.save()
    return JsonResponse(data)# returning json reponse to the HTMl 



