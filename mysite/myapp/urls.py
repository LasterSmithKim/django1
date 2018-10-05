from django.conf.urls import url
from . import views
from .models import Dreamreal
from django.views.generic import TemplateView,ListView


urlpatterns = [

    url(r"hello/",views.hello,name="hello"),
    url(r"index/",views.index,name="index"),
    url(r"detail/(\d+)/",views.viewsArticle,name="article"),
    url(r"details/(\d{2})/(\d{4})",views.viewsArticles, name="articles"),
    url(r"redirect/outer",views.viewRedirect,name="redirect"),
    url(r"generic/static",TemplateView.as_view(template_name = "static.html")),

    #通用模块 ListView导入，调用as_view方法，导入model中的类名Dreamreal，获取数据库中的object_list，传递给template渲染返回给浏览器
    url(r'dreamreals/', ListView.as_view(model=Dreamreal, template_name = "dreamreal_list.html")),

    url(r'connection/', TemplateView.as_view(template_name='login.html')),
    url(r'login/', views.login, name='login'),




    url(r"^$",views.hello,name="hello"),
]