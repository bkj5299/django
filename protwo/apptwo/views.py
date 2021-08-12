from django.shortcuts import render
from apptwo.models import user
# Create your views here.
from apptwo.forms import Newuser
def index(request):
    return render(request,'apptwo/index.html')

def users(request):
    user_list=user.objects.order_by('first_name')
    user_dict={'user_list':user_list}
    return render(request,'apptwo/user.html',context=user_dict)
def signup(request):

    form=Newuser()
    if request.method=="POST":
        form=Newuser(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return users(request)
        else:
            return index(request)
    return render(request,'apptwo/signup.html',{'form':form})
