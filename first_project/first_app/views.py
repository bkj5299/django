from django.shortcuts import render
from django.http import HttpResponse
from  first_app.models import Topic,Accessrecord,Webpage
# Create your views here.

from django.contrib.auth import login,logout,authenticate
from django.urls import reverse
from django.http import  HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from first_app import forms

def help(request):
    return HttpResponse("<em>i am king</em>")
def index(request):
    webpage_list=Accessrecord.objects.order_by('date')
    date_dict={'access_records':webpage_list}
    return render(request,'first_app/index.html',context=date_dict)
def form_name_view(request):
    form=forms.formname()
    if request.method== 'POST':
        form=forms.formname(request.POST)

        if form.is_valid():
            print('Valid')
            print(form.cleaned_data['name'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['text'])


    return render(request,'first_app/form.html',{'form':form})

def temp(request):
    return render(request,'first_app/templtag.html')

def register(request):
    registered=False
    if request.method== 'POST':
        user_form=forms.Userform(data=request.POST)
        profile_form=forms.Userprofileinfoform(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user=user_form.save()
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user
            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']
            profile.save()

            registered=True

        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form=forms.Userform()
        profile_form=forms.Userprofileinfoform()
    return render(request,'first_app/register.html',{'Userform':user_form,
                                             'Userprofile':profile_form,
                                               'registered':registered,})

def user_login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('first_app:index'))
            else:
                return HttpResponse('Account Not Active')
        else:
            return HttpResponse('Invalid login details')
    else:
        return render(request,"first_app/login.html")
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('first_app:index'))
