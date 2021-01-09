from django.http import HttpResponse
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .forms import NameForm, NewPlaceForm
import os
from twilio.rest import Client
import csv
from datetime import datetime
from datetime import date


def entrance(num,location):
        f=open("guestlist.csv","a+",newline="\n")
        #import phone number and location from website input
        x=csv.writer(f)
        dt=date.today()
        now=datetime.now()
        entime=now.strftime("%H:%M:%S")
        l=[num,location,dt,entime,'false']
        print (l)
        x.writerow(l)
        f.close()

def exit(phone):
        f=open("D:\\guestlist.csv","a")
        x=csv.reader(f)
        y=csv.writer(f)
        for line in x:
                if line[0]==phone:
                        now=datetime.now()
                        line[4]=now.strftime("%H:%M")

# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
def send_mssg(number, message):
    account_sid = 'AC6b46521ddc9d177f3f6e23d3b5e87191'
    auth_token = '4d6b6cbe9cdbefd455c45773b68c9e02'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
             body=message,
             from_='+19284874293',
             to= '+1'+str(number)
         )

    print(message.sid)

def retrieve(phone):
    f=open("D:\\guestlist.csv","r")
    x=csv.reader(f)
    lists = list()
    for line in x:
        if phone==line[0]:
            y=line[2]
            a=y.year
            b=y.month
            c=y.day

            z=line[3]
            m=z.hour
            n=z.minute
            o=(m*60)+n

            p=line[4]
            d=p.hour
            e=p.minute
            f=(d*60)+e

            entx=(entime[3]*60)+entime[4]
            entime=[a,b,c,entx]

            extx=(extime[3]*60)+extime[4]
            extime=[a,b,c,extx]

            restaurant=line[1]

    inf2=[restaurant, entime, extime] #'restaurant' must be replaced by the restaurant name variable
    for line in x:
        if line[1]==inf2[0]:
            y=line[2]
            a=y.year
            b=y.month
            c=y.day

            z=line[3]
            m=z.hour
            n=z.minute
            o=(m*60)+n

            p=line[4]
            d=p.hour
            e=p.minute
            f=(d*60)+e

            if o<=entx and f>=extx:
                lists.append(line[0])
            elif o<=entx and f>entx and f<extx:
                lists.append(line[0])
            elif o>entx and f<extx:
                lists.append(line[0])
            elif o>entx and o<extx and f>extx:
                lists.append(line[0])
            else:
                break
    f.close()



def checkin(request):
        # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            entrance(form['your_name'].value(),'happy_burger')
            send_mssg(form['your_name'].value(),'Thank you for checking in, you may now enter. Please be sure to checkout at this link: http://192.168.1.93:8000/happy_burger_checkout')
            return render(request,'checkin_landing.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
    return render(request, 'checkin_page.html',{'form': form})

def checkout(request):
        # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print(form['your_name'].value())
            # send_mssg(form['your_name'].value(),'Thank you for checking out, you may now leave')
            return render(request,'checkout_landing.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
    return render(request, 'checkout_page.html',{'form': form})

def report_case(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            #print(retrieve(form['your_name'].value()))
            return render(request,'report_case_landing.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
    return render(request, 'report_case.html',{'form': form})

def submitted(request):
    return HttpResponse("Thank you for submitting")

def homepage(request):
    return render(request, 'mainpage.html')
