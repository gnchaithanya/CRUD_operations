from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
from django.db.models.functions import Length
# Create your views here.
def Insert_Topic(request):
    tn=input('Enter TopicName: ')
    to=Topic.objects.get_or_create(Topic_Name=tn)[0]
    to.save()
    QSTO=Topic.objects.all()
    d={'QSTO':QSTO}
    return render(request,'display_Topic.html',d)
    
    # return HttpResponse('<center><h1>Data Inserted Successfully!!!!</h1></cntner>')

def Insert_Webpage(request):
    tn=input('Enter TopicName: ')
    to=Topic.objects.get_or_create(Topic_Name=tn)[0]
    to.save()
    na=input("Enter Name : ")
    ur=input("Enter Url : ")
    wo=Webpage.objects.get_or_create(Topic_Name=to,Name=na,Url=ur)[0]
    wo.save()
    QSWO=Webpage.objects.all()
    d={'QSWO':QSWO}
    return render(request,'display_Webpage.html',d)
    # return HttpResponse('<center><h1>Data Inserted Successfully!!!!</h1></cntner>')

def Insert_AR(request):
    tn=input('Enter TopicName: ')
    to=Topic.objects.get_or_create(Topic_Name=tn)[0]
    to.save()
    na=input("Enter Name : ")
    ur=input("Enter Url : ")
    wo=Webpage.objects.get_or_create(Topic_Name=to,Name=na,Url=ur)[0]
    wo.save()
    au=input("Enter AuthorName : ")
    da=input("Enter Date : ")
    em=input("Enter Email : ")
    ao=AccessRecords.objects.get_or_create(Name=wo,Author=au,Date=da,Email=em)[0]
    ao.save()
    QSAO=AccessRecords.objects.all()
    d={'QSAO':QSAO}
    return render(request,'display_AR.html',d)
    # return HttpResponse('<center><h1>Data Inserted Successfully!!!!</h1></cntner>')
def display_Topic(request):
    QSTO=Topic.objects.all()
    d={'QSTO':QSTO}
    return render(request,'display_Topic.html',d)

def display_Webpage(request):
    QSWO=Webpage.objects.all()
    QSWO=Webpage.objects.all().order_by('Topic_Name')#Ascending Order
    QSWO=Webpage.objects.all().order_by('-Topic_Name')#Descending Order
    QSWO=Webpage.objects.filter(Topic_Name='Cricket').order_by('Topic_Name')#Ascendind order
    QSWO=Webpage.objects.filter(Topic_Name='Cricket').order_by('-Topic_Name')
    QSWO=Webpage.objects.all().order_by('Name')
    QSWO=Webpage.objects.all().order_by('Topic_Name')[2:9:1]
    QSWO=Webpage.objects.all().order_by('Topic_Name')[6:7]
    QSWO=Webpage.objects.all().order_by(Length('Name'))#Ascending order
    QSWO=Webpage.objects.all().order_by(Length('Name').desc())#Descending Order
    
    d={'QSWO':QSWO}
    return render(request,'display_Webpage.html',d)

def display_AR(request):
    QSAO=AccessRecords.objects.all()
    d={'QSAO':QSAO}
    return render(request,'display_AR.html',d)

def Update_Topic(request):
    QSTO=Topic.objects.all()
    
    d={'QSTO':QSTO}
    return render(request,'display_Topic.html',d)
def Update_Webpage(request):
     QSWO=Webpage.objects.all()
     #Updating singlr row
     Webpage.objects.filter(Name='Dhoni').update(Url='https://msd.com')
     QSWO=Webpage.objects.all()
     #Updating multiple rows
     Webpage.objects.filter(Topic_Name='Cricket').update(Name='Rohith Sharma')
     QSWO=Webpage.objects.all()
     #Updating Foreign key column
     Webpage.objects.filter(Name='Ronaldo').update(Topic_Name='Cricket')
     QSWO=Webpage.objects.all()
    
    
    #No rows are satisfies
     Webpage.objects.filter(Topic_Name='Rugby').update(Name='chaithu')
     QSWO=Webpage.objects.all()


     #update or create method
     #modify multiple rows
    #  Webpage.objects.update_or_create(Topic_Name='Cricket',defaults={'Name':'Dhoni'})
    #  QSWO=Webpage.objects.all()
     #one row
     Webpage.objects.update_or_create(Name='PV Sindhu',defaults={'Url':'http://pvsindhuja.com'})
     QSWO=Webpage.objects.all()

     #no rows satisfies(We need to provide instances of paren table)
     RTO=Topic.objects.get(Topic_Name='Running')
     Webpage.objects.update_or_create(Name='Chaithu',defaults={'Topic_Name':RTO,'Url':'http://chaithu.in'})
     QSWO=Webpage.objects.all()

     #Foreign key cloumn(We need to provide instances of paren table)
     BTO=Topic.objects.get(Topic_Name='Badminton')
     Webpage.objects.update_or_create(Name='Supraja',defaults={'Topic_Name':BTO,'Url':'http://supraja.com'})
     QSWO=Webpage.objects.all()

     d={'QSWO':QSWO}
     return render(request,'display_Webpage.html',d)
def delete_Webpage(request):
    QSWO=Webpage.objects.all()
    Webpage.objects.filter(Name='Supraja').delete()
    Webpage.objects.filter(Topic_Name='Cricket').delete()
    Webpage.objects.all().delete()
    d={'QSWO':QSWO}
    return render(request,'display_Webpage.html',d)


   
    





    
                        