from django.shortcuts import render,redirect
from .forms import AccountForm
from .models import Account
from django.contrib.auth import logout,login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def register_user(request):
    
    if request.method == 'POST':
        form = AccountForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            print("New user has been created")
            return redirect('home')
    
    return render(request, 'register.html')

def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = Account.objects.get(email=email)
        except Account.DoesNotExist:
            messages.info(request, 'User does not exists with this email')
            user = None
        
        if user is not None:
            is_correct_pass = user.check_password(password)
            if is_correct_pass:
                login(request,user=user)
                return redirect('home')
            else:
                messages.error(request, 'Wrong Password')
                return redirect('login_user')
        else:
            print('refresh')
            return redirect('login_user')

    return render(request, 'login.html')

@login_required(redirect_field_name='login_user')
def logout_user(request):
    logout(request)
    return redirect('login_user')

def profile_user(request):
    return render(request, 'profile.html')