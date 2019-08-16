from django.shortcuts import render, redirect
from .models import user
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages

# Create your views here.


def homepage(request):
    return render(request = request,
                  template_name='home/home.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        con_password = request.POST.get('con-password')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        question = request.POST.get('question')
        answer = request.POST.get('answer')
        if user.objects.filter(username = username).exists() :
            messages.error(request, 'username already exists')
            return render(request, "home/register.html")
        if password != con_password :
            messages.error(request, "Passwords didnot match.")
            return render(request, "home/register.html")
        elif question == '0':
            messages.error(request, "Please choose a question")
            return render(request, "home/register.html")
        s=user(username=username, password=password, email=email, phone=phone, question=question, answer=answer)
        s.save()
        return render(request, "home/register.html")

    return render(request, "home/register.html")
 
def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("home:homepage")

def login_request(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if user.objects.filter(username = username, password = password).exists() :
            messages.success(request, 'Login Successfully')
            return render(request, "home/home.html")
        else :
            messages.error(request, "Username or password incorrect")
            return render(request, "home/login.html")
    return render(request = request,
                    template_name = "home/login.html")