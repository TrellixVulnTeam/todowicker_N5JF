"""todowicker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from wicker import views

urlpatterns = [
    #auth
    path('admin/', admin.site.urls),
    path('signup/',views.signupuser,name='signupuser'),
    path('logout/',views.logoutuser,name='logoutuser'),
    path('login/',views.loginuser,name='loginuser'),

    #wicker

    path('',views.home,name='home'),
    path('current/',views.currentwicker,name='currentwicker'),
    path('create/',views.createwicker,name='createwicker'),
    path('complete/',views.completewicker,name='completewicker'),
    path('<int:wicker_pk>/delete',views.delete,name='delete'),
    path('wicker/<int:wicker_pk>',views.viewwicker,name='viewwicker'),
    path('<int:wicker_pk>/comlete',views.complete,name='complete')
]
