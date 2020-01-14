




from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth import authenticate,login,get_user_model,logout


def index(request):
    return render(request,"index/index.html",{})