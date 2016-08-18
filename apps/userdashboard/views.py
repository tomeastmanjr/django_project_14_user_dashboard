from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.db.models import Count
from django.core.urlresolvers import reverse

def index(request):
    return render(request, 'userdashboard/index.html')
    # show the test app home page

def signin(request):
    return render(request, 'userdashboard/signin.html')
    # show the signin page

def register(request):
    return render(request, 'userdashboard/register.html')
    # show the register page

def show(request):
    return render(request, 'userdashboard/user.html')
    # display a particular user

def dashboard(request):
    return render(request, 'userdashboard/dashboard.html')
    #shows all users

def admin(request):
    context = {
        "users": User.objects.all()
    }
    return render(request, 'userdashboard/admin.html', context)
    #shows the users and the actions for the admin

def new(request):
    return render(request, 'userdashboard/new.html')
    # display a form to create a new user

def create(request):
    User.objects.create(first_name=request.POST["first_name"])
    return redirect('dashboard')
    # this is to process the new user information

def edit(request):
    return render(request, 'userdashboard/edit_user.html')
    # display a form to update a user


def update(request, user_id):
    u = User.objects.get(id=user_id)
    u.first_name = request.POST["first_name"]
    u.save()
    return redirect('dashboard')
    # process information from the edit form and update the particular user

def delete(request):
    return render(request, 'userdashboard/destroy.html')

def destroy(request, user_id):
    u = User.objects.get(id=user_id)
    u.delete()
    return redirect('dashboard')
    # remove a product
#
# def users(request):
#     pass
#     #only needed to make the specific routing from the wireframe work
