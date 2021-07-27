from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate
from .forms import WickerForm
from .models import Wicker
from django.utils import timezone
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'wicker/home.html')

def signupuser(request):
    if request.method == 'GET':
     return render(request, 'wicker/signupuser.html',{'form':UserCreationForm()})
    else:
     if request.POST['password1']==request.POST['password2']:
        try:
            user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
            user.save()
            login(request,user)
            return redirect('currentwicker')
        except IntegrityError:
            return render(request, 'wicker/signupuser.html',{'form':UserCreationForm(),'error':'user name already exists,please chose something else'})
     else:
         return render(request, 'wicker/signupuser.html',{'form':UserCreationForm(),'error':'password did not match'})




def loginuser(request):
    if request.method == 'GET':
        return render(request, 'wicker/loginuser.html',{'form':AuthenticationForm()})
    else:
     user = authenticate(request,username=request.POST['username'],password=request.POST['password'])
     if user is None:
         return render(request, 'wicker/loginuser.html',{'form':AuthenticationForm(),'error':'Invalid username or password'})
     else:
          login(request,user)
          return redirect('currentwicker')
@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


@login_required
def createwicker(request):
    if request.method == 'GET':
     return render(request, 'wicker/createwicker.html',{'form':WickerForm()})
    else:
        try:
            form =WickerForm(request.POST)
            newwicker =form.save(commit=False)
            newwicker.user = request.user
            newwicker.save()
            return redirect('currentwicker')
        except ValueError:
         return render(request, 'wicker/createwicker.html',{'form':WickerForm(),'error': 'value exceeded the maximum limit'})
@login_required
def currentwicker(request):
    wickers=Wicker.objects.filter(user=request.user,date_completed__isnull=True)
    return render(request, 'wicker/currentwicker.html',{'wickers':wickers})

@login_required
def completewicker(request):
    wickers=Wicker.objects.filter(user=request.user,date_completed__isnull=False).order_by('-date_completed')
    return render(request, 'wicker/completewicker.html',{'wickers':wickers})

@login_required
def viewwicker(request,wicker_pk):
     wicker=get_object_or_404(Wicker,pk=wicker_pk,user=request.user)
     if request.method == 'GET':
          form=WickerForm(instance=wicker)
          return render(request, 'wicker/viewwicker.html',{'wicker':wicker,'form':form})
     else:
            try:
                 form=WickerForm(request.POST,instance=wicker)
                 form.save()
                 return redirect('currentwicker')  
            except ValueError:
                 return render(request, 'wicker/viewwicker.html',{'wicker':wicker,'form':form,'error':'error while saving'})

@login_required
def complete(request,wicker_pk):
    wicker=get_object_or_404(Wicker,pk=wicker_pk,user=request.user)
    if request.method == 'POST':
        wicker.date_completed=timezone.now()
        wicker.save()
        return redirect('currentwicker')  

@login_required
def delete(request,wicker_pk):
    wicker=get_object_or_404(Wicker,pk=wicker_pk,user=request.user)
    if request.method == 'POST':
        wicker.delete()
        return redirect('currentwicker')  