from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import HttpResponse
from tba_app.models import registration
from tba_app.models import admin
from tba_app.models import contact
from datetime import date,timedelta,datetime

# Create your views here.
def register(request):
    if request.method=='POST':
        name=request.POST.get('name')
        mobileno=request.POST.get('mobileno')
        email=request.POST.get('email')
        types=request.POST.get('types')
        officeadd=request.POST.get('officeadd')
        residenceadd=request.POST.get('residenceadd')
        joiningdate=request.POST.get('joiningdate')
        duration=request.POST.get('duration')
        password=request.POST.get('password')

        a=registration(name=name, mobileno= mobileno,email=email,types=types,officeadd=officeadd,residenceadd=residenceadd,joiningdate=joiningdate,duration=duration,status='pending',password=password)
        a.save()
        return render(request,'reg.html')

def regview(request):
    queryset=registration.objects.all()
    return render(request,'adminhome1.html',{'authors':queryset})

#def approval(request):
   # if request.method=='POST':
       # id=request.POST.get('id')
       # today = str(date.today())
       # registration.objects.filter(id=id).update(status='approved',approvedate=today)
       # return regview(request)
def approval(request):
    if request.method=='POST':
        id=request.POST.get('id')
        q=registration.objects.all().filter(id=id)[0]
        dur=q.duration
        join=q.joiningdate
        if dur=='3 months':
            dd=90
        elif dur=='6 months':
            dd=180
        elif dur=='1 Year':
            dd=365
        elif dur=='5 Years':
            dd=1825
        d=timedelta(dd)
        exp=join+d
        today = str(date.today())
        registration.objects.filter(id=id).update(status='Approved',approvedate=today,expirydate=exp)
        return regview(request)

#def authentication(request):
    #if request.method=='POST':
       # email=request.POST.get('email')
       # password=request.POST.get('password')
       # email=str(email)
       # password=str(password)
       # u=admin.objects.filter(email=email,password=password)

       # if u.count()==1:
          # return render(request,'adminhome.html') 
       # else:
           # u=registration.objects.filter(email=email,password=password,status='approved')
            #if u.count()==1:
               # request.session['email']=email
               # qry=registration.objects.all().filter(email=email)
               # return render(request,'memberhome.html')
            #else:
                #return HttpResponse('login unsuccesful')

def authenticate(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        u=admin.objects.all().filter(email=email,password=password)
        if u.count()==1:
            #request.session['id']=u.id
            return render(request,'adminhome.html')
        else:
            u=registration.objects.all().filter(email=email,password=password,status='approved')
            if u.count()==1:
                request.session['email']=email
                qry=registration.objects.all().filter(email=email)
                return render(request,'memberhome.html')
            else:
                return HttpResponse('Login Failed')   

def membersview(request):
    querysett=registration.objects.all().filter()
    return render(request,'member.html',{'authorss':querysett})

def detailsview(request):
    querysettt=registration.objects.all().filter(email=request.session['email'])
    return render(request,'profileview.html',{'authorsss':querysettt})


def editprofile(request):
    QuerySetttt    = registration.objects.all().filter(email=request.session['email'])
    return render(request,'profileedit.html',{'authorssss':QuerySetttt})

def contactadmin(request):
    if request.m1ethod=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')

        b=contact(name=name,email=email,subject=subject,message=message,status='off')
        b.save()
    return render(request,'adminhome.html')

def editsave(request):
    if request.method=='POST':
     
        name=request.POST.get('name')
        mobileno=request.POST.get('mobileno')
        email=request.POST.get('email')
        types=request.POST.get('types')
        officeadd=request.POST.get('officeadd')
        residenceadd=request.POST.get('residenceadd')
        
        duration=request.POST.get('duration')
        
       
        password=request.POST.get('password')
        registration.objects.filter(email=request.session['email']).update(name=name,mobileno=mobileno,email=email,types=types,officeadd=officeadd,residenceadd=residenceadd,duration=duration,password=password)
    return render(request,'memberhome.html')

def viewmsg(request):
    queryset=contact.objects.all().filter(status='off')
    return render(request,'contact.html',{'authors':queryset})

def readmsg(request):
    if request.method=='POST':
        id=request.POST.get('id')
        contact.objects.filter(id=id).update(status='on')
        return viewmsg(request)