from django.shortcuts import render,redirect,HttpResponse
from datetime import datetime
from gamers.models import Contact,Game,Question,Matchpt
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
ggid=''
ggname=''

# Create your views here.
def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login") 
    return render(request, 'index.html')

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")

        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")


def about(request):
    return render (request,'about.html')
    #return HttpResponse("This is about page")
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your feedback has been sent.')
    return render (request,'contact.html')
    #return HttpResponse("This is contact page")
def services(request):
    return render (request,'services.html')
    #return HttpResponse("This is services page")

def pubg(request):
    return render (request,'pubg.html')
def home(request):
    r={}
    r['games']=Game.get_all_games()
    print(r)
    gid=request.GET.get('game')
    print(gid)
    global ggid
    ggid=gid
    
    #print(gamename)
    if gid:
      gamename=Game.get_game(gid)
      #print(gamename('waiting_list'))
      print(gamename[0])
      global ggname
      ggname=gamename[0]
      context={
          'gg':gamename[0]
      }

      return render(request,'findmatch.html',context)
    else:
      return render(request,'home.html',r)
def matching(request):
    if request.method=="POST":
        gameid = request.POST.get('gameid')
        email=request.POST.get('email')
        name=request.POST.get('name')
        print(gameid)
        print(email)
        print('HI')
        print(ggid)
        waiting=Game.get_wl((ggid))
        if waiting == 0:
           obj=Game.objects.get(id=ggid)
           obj.waiting_list=1
           obj.save()
           obj1=Question(game=ggname,ign=name,igid=gameid,email=email)
           obj1.save()
           return HttpResponse("We will inform you when a match is found")
        else:
            k={}
            k['users']=Question.get_users(ggid)
            print(k)
            return render(request,'matches.html',k)
            users=Question.get_users(ggid)
            print(users)
            return render(request,'matches.html',users)

def matchpt(request):
    if request.method=="POST":
        name=request.POST.get('name')
        gameid=request.POST.get('gameid')
        email=request.POST.get('email')
        #opt11=request.POST.get('opt11')
        option=int(request.POST.get('opt1'))+int(request.POST.get('opt2'))+int(request.POST.get('opt3'))*(2**8)+int(request.POST.get('opt4'))*(2**9)+int(request.POST.get('opt5'))*(2**10)+int(request.POST.get('opt6'))*(2**11)+int(request.POST.get('opt7'))*(2**12)+int(request.POST.get('opt8'))*(2**13)+int(request.POST.get('opt9'))*(2**14)+int(request.POST.get('opt10'))*(2**15)+int(request.POST.get('opt11'))*(2**16)
        matchpt=Matchpt(name=name,gameid=gameid,email=email,option=option)
        matchpt.save()
        n=Matchpt.objects.count()
        b=Matchpt.objects.all()[n-1].option
        m=0
        x=0
        for i in range(0,n-1):
            a=Matchpt.objects.all()[i].option
            a=a&b
            r=0
            while(a>0):
                a=(a&(a-1))
                r=r+1
            if(r>m):
               m=r
               x=i
        m='%.2f'%((m/11)*100)
        print(Matchpt.objects.all()[x])
        print(m)
        context={
            'var1':m,
            'var2':Matchpt.objects.all()[x].name
        }
        messages.success(request, ' % match with ')
        return render (request,'findmatch.html',context)
    return render (request,'findmatch.html')  