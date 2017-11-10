from django.shortcuts import render, HttpResponse, redirect

def register(req):
    response = "placeholder for users to create a new user record"

    return HttpResponse(response)

def login(req):
    response = "placeholder for users to login"

    return HttpResponse(response)

def new(req):
    return redirect('users/register')

def show(req):
    response = "placeholder to later display all the list of users"

    return HttpResponse(response)
