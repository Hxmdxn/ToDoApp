from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *




def list(request):
    tasks=Task.objects.all()
    form=TaskForm()
    if request.method=="POST":
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect ("/")
    context= {'tasks':tasks,'form':form}
    return render(request,"tasks/list.html",context)

def update(request,pk):
    tasks=Task.objects.get(id=pk)
    form=TaskForm(instance=tasks)
    
    if request.method=="POST":
        form=TaskForm(request.POST,instance=tasks)
        if form.is_valid():
            form.save()
        return redirect ("/")
    data={
        'form':form
    }
        
    return render(request,"tasks/update.html",data)

def delete(request, pk):
    item=Task.objects.get(id=pk)
    if request.method=="POST":
        item.delete()
        return redirect('/')
    
    data  = {
    'item':item}
    return render(request,"tasks/delete.html",data)
    
    