from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from home.forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView
from home.forms import CreateUserForm
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def register_page(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()

            subject = 'Welcome to Our Platform'
            message = f'Hi {user.username}, thank you for registering!'
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = [user.email]

            try:
                send_mail(subject, message, from_email, to_email)
            except Exception as e:
                messages.error(request, f'Error sending email: {e}')


            messages.success(request, 'Account succesfully register')
            return redirect('login')


    context = {
        'form':form
    }
    return render(request,'register.html',context)


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username,password=password) 

        if user is not None:
            login(request, user)
            return redirect('event_list')
        else:
            messages.info (request, 'Username or password is incorect')
    context = {}
    return render(request,'login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')


# class RegisterView(CreateView):
#     form_class = CreateUserForm
#     template_name = 'register.html'

