"""newnew URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cl import views

urlpatterns = [
    path('admin/', admin.site.urls,name="ad"),
    path('',views.signupPage,name='signup'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutPage,name='logout'),
    path('home/',views.home,name='home'),
    path('student/',views.student,name="stu"),
    path('admission/',views.admission,name="adm"),
    path('marks/',views.marks,name="mar"),
    path('feedback/',views.feedback),
    #path('Image/',views.Image),
    path('do_payment',views.do_payment,name="do_payment"),
    path('thank/',views.thank,name="thanks"),
    path('search_stu',views.search,name="search_stu"),
    path('pay/',views.payment,name="payi"),
]
