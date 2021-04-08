from django.shortcuts import render,HttpResponseRedirect
from todo.models import  Todo
from .forms import TodoForm
from django.http import HttpResponseRedirect
# Create your views here.
def basic(request):
    if request.method=="POST":
        fm = TodoForm(request.POST)
        if fm.is_valid():
            fm.save()
            fm = TodoForm()
    else:
        fm = TodoForm()
    sab =Todo.objects.all()
    return render(request,"todo/base.html",{'sab':sab,'fm':fm})


def delete(request,id):
    getuser = Todo.objects.filter(pk=id)
    getuser.delete()
    return HttpResponseRedirect('/app/base/')

def update(request,id):
    if request.method=="POST":
        pi = Todo.objects.get(pk=id)
        fm=TodoForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/app/base/')
    else:
        pi = Todo.objects.get(pk=id)
        fm=TodoForm(instance=pi)
    return render(request,'todo/update.html',{'form':fm})
