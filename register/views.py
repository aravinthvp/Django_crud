from django.shortcuts import render,redirect
from .forms import UserForm
from .models import Users
# Create your views here.
def users_list(request):
    context = {'users_list':Users.objects.all()}
    return render(request,'register/users_list.html',context)

def users_form(request,id=0):
    if request.method == "GET":
        if id == 0:
            form = UserForm()
        else:
            users = Users.objects.get(pk=id)
            form = UserForm(instance=users)
        return render(request,'register/users_form.html',{'form':form})
    else:
        if id == 0:
            form = UserForm(request.POST)
        else:
            users = Users.objects.get(pk=id)
            form = UserForm(request.POST,instance= users)
        if form.is_valid():
            form.save()
        return redirect('/users/list')



def users_delete(request,id=0):
    users = Users.objects.get(pk=id)
    users.delete()
    return redirect('/users/list')
