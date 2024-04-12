from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name= request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        password_confirmation = request.POST.get('password2')
        if password == password_confirmation:
            if User.objects.filter(username=username).exists():
                messages.error(request,"Username already taken, choose another")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,"Email already exists, please login")
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, email=email,
                                        first_name=first_name, last_name=last_name,
                                        password=password)
                    user.save()
                    messages.success(request,"Registration success, please login")
                    return redirect('login')
        else:
            messages.error(request,"Password do not match")
            return redirect('register')
    else:
        return render(request, 'registration/register.html')
    
    
    

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('dashboard')
        else:
            messages.error(request,"Invalid credentials")
            return redirect('login')
    else:
        return render(request, 'registration/login.html')
    

def dashboard(request):
    return render(request, 'registration/dashboard.html')