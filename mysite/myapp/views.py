from django.shortcuts import render, redirect
import datetime
from .forms import LoginForm, ProfileForm
from .models import Profile1, Dreamreal
from django.template import RequestContext
from django.http import HttpResponse


# Create your views here.




def hello(request):
    today = datetime.datetime.now().date()
    str = '''kjf;djsMMMMMMMMMMMfj;sdak'''
    arr = [1,2,3]
    return render(request, "hello.html", {"today": today,"str":str,"arr":arr})

def index(request):
    dreamreal = Dreamreal(
        website="www.polo.com", mail="sorex@polo.com",name="sorex", phonenumber="002376970")
    dreamreal.save()
    objects = Dreamreal.objects.all()
    return render(request, "index.html", {"name": "Tom","date":objects})


def viewsArticle(request, articleId):
    return render(request,"detail.html",{"id": articleId})

def viewsArticles(request, month, year):
    return render(request, "details.html", {"month": month,"year":year})


def viewRedirect(request):
    #return redirect("https://www.djangoproject.com")
    return redirect(hello)

#class StaticView(TemplateView):
   #template_name = "static.html" 也可以将这个name直接当做参数传递给 urls，但是这个类需要 pass结束
#    pass
    #在urls中都可以直接引入通用试图，直接调用 as_view 方法，类都不用创建了


#登录处理
def login(request):
    username = "not logged in"
    password = "***"

    if request.method == "POST":
        # Get the posted form
        MyLoginForm = LoginForm(request.POST)

        if MyLoginForm.is_valid():
            username = MyLoginForm.cleaned_data['user']
            request.session['username'] = username


    else:
        MyLoginForm = LoginForm()
    response = render(request, 'loggedin.html', {"username": username})
    #response.set_cookie('last_connection', datetime.datetime.now())
    #response.set_cookie('username', username)
    return response


def formView(request):
    #if 'username' in request.COOKIES and 'last_connection' in request.COOKIES:
    if request.session.has_key('username'):
        username = request.COOKIES['username']

        #last_connection = request.COOKIES['last_connection']
        #last_connection_time = datetime.datetime.strptime(last_connection[:-7],"%Y-%m-%d %H:%M:%S")
        return render(request, 'loggedin.html', {"username": username})

        #if (datetime.datetime.now() - last_connection_time).seconds < 10:
        #    return render(request, 'loggedin.html', {"username": username})
        #else:
        #    return render(request, 'login.html', {})

    else:
        return render(request, 'login.html', {})



def SaveProfile(request):
    saved = False

    if request.method == "POST":
        # Get the posted form
        MyProfileForm = ProfileForm(request.POST, request.FILES)

        if MyProfileForm.is_valid():
            profile = Profile1()
            profile.name = MyProfileForm.cleaned_data["name"]
            print(profile.name)
            profile.picture = MyProfileForm.cleaned_data["picture"]
            print(profile.picture)
            profile.save()
            saved = True
            print(saved)
        else:
            MyProfileForm = ProfileForm()

    return render(request, 'saved.html', locals())

def logout(request):
   try:
      del request.session['username']
   except:
      pass
   return HttpResponse("<strong>You are logged out.</strong>")
