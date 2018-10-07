from django.shortcuts import render, redirect
import datetime
from .forms import LoginForm, ProfileForm
from .models import Profile1, Dreamreal

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
            password = MyLoginForm.cleaned_data['password']
    else:
        MyLoginForm = LoginForm()

    return render(request, 'loggedin.html', {"username": username,"password":password})


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
