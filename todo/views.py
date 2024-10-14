from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.views.decorators.http import require_POST
from .models import Task
from django.urls import reverse
from django.contrib.auth.decorators import login_required
 
@login_required
def index(request:HttpRequest): 
    user=request.user
    tasks=Task.objects.filter(owner=user)
    # return HttpResponse("<h1> hello world </h1>")
    # return JsonResponse({"messsage": "kanto sarobidy"})
    return render(request,"index.html",{"tasks":tasks})

def login_view(request=HttpRequest):
    if request.method== "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(username=username,password=password)

        if user:
            login(request,user)
            return redirect("/")
        return render(request,"login.html",{"error":"user not found"}) 

    return render(request,"login.html")

def complete_task(request:HttpRequest):
    pass

@require_POST
def add_task(request: HttpRequest):
    title=request.POST.get("title")
    task=Task(
        title=title,
        owner =request.user
    )
    # enregister et editer
    task.save()   
    return redirect(reverse("home"))