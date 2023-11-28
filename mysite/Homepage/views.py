from django.shortcuts import render, redirect
from .models import Registration
from .forms import UserForm, LoginForm
from django.http import HttpResponse
from django.contrib import messages


# Create your views here.
def home(request):
    user_id = request.session.get("user_id", None)

    if user_id is not None:
        try:
            user_data = Registration.objects.get(pk = user_id)
        except Registration.DoesNotExist:
            user_data = None

        context = {
            "user_id" : user_data
        }
        return render(request, "home.html", context)
    else:
        return redirect("login")


def registration(request):

    if request.method == "POST":
        form = UserForm(request.POST)
        print('form-->',form)
        print('form not valid')
        if form.is_valid():
            print('form valid')
            user = form.save()  # save method will return an id
            request.session["user_id"] = user.user_id
            return redirect("home")
        else:
            return render(request, "registration.html", {'form' : form}) # register is a url name

    form = UserForm()
    reg_form={
        "form" : form
    }
    return render(request, "registration.html", reg_form) # form is passing as context that as key value pires


def login(request):

    if request.method == "POST":
        form = LoginForm(request.POST)
        log_email = form['Email'].value()
        log_password = form["password"].value()

        try:
            log_info = Registration.objects.filter(Email = log_email) # log_info = [[userid : 1, firstname : "asrith"]]
            print(log_info)
            if(log_info):
                user_id = log_info[0].user_id
                # user_id = None
                # for x in info:
                #     user_id = x.user_id
                if log_email == log_info[0].Email and log_password == log_info[0].password:
                    request.session["user_id"] = user_id
                    return redirect("home")
            else:
                log_form={
                    "form" : form,
                }
                messages.info(request, 'Invalid Email or Password')
                return render(request, "login.html", log_form)
            
        except Registration.DoesNotExist:
            return HttpResponse("Invalid Email or Password")

    form = LoginForm()
    log_form={
        "form" : form
    }
    return render(request, "login.html", log_form)


def log_out(request):
    
    if request.method == "POST":
        del request.session["user_id"]
        return redirect("login")