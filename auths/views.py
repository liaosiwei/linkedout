# coding=UTF-8
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from .forms import SignUpForm
# Create your views here.

def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password1"])
            if user is not None and user.is_active:
                login(request, user)
            return HttpResponseRedirect("/")
    else:
        form = SignUpForm()
    return render_to_response("auths/register.html", {'form': form}, context_instance=RequestContext(request))

def login_user(request):
    username = request.POST['username']
    password = request.POST['passwd']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect("/")
    return HttpResponseRedirect("/")