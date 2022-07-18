from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm, EditUserForm 
from .forms import PasswordChangeForm,ForgotPasswordForm,UserValidate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import auth
from .models import User
# from .forms import CUserCreationForm

# Create your views here.


def signup(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("login")
            return render(request, "signup.html", {'form': form})
        else:
            form = CustomUserCreationForm()
            return render(request, "signup.html", {'form': form})
    else:
        return render(request, "error.html", {'error': '401 Unauthorized (RFC 7235)'})


def login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = CustomAuthenticationForm(request.POST)
            email = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                print("login success")
                auth.login(request, user)
                return redirect("index")
            else:
                print("********** USER IS NONE ************")
                messages.error(request, 'Invalid Credentials')
                return redirect("login")
        else:
            form = CustomAuthenticationForm()
            return render(request, 'login.html', {'form': form})
    else:
        return render(request, "error.html", {'error': '401 Unauthorized (RFC 7235)'})


def logout(request):
    auth.logout(request)
    return redirect('index')


def UserProfile(request):
    if request.user.is_authenticated:
        return render(request, "user_profile.html")
    else:
        return redirect("index")


def ChangeUserDetails(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = EditUserForm(request.POST, instance=request.user)
            if fm.is_valid():
                fm.save()
                messages.success(request, 'Details are Updated')
            else:
                messages.error(
                    request, 'User Name already exist choose another one')
        else:

            fm = EditUserForm(instance=request.user)
        return render(request, 'changeuserform.html', {'form': fm})
    else:
        return redirect('login')


def ChangePassword(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
        else:
            fm = PasswordChangeForm(user=request.user)
        return render(request, 'changepasswordform.html', {'form': fm})
    else:
        return render(request, "error.html", {'error': '404 Page Not found '})


def ValidateUser(request):
    if request.method == 'POST':
        fm=UserValidate(request.POST)
        if fm.is_valid():            
            phone=request.POST['phone']
            email=request.POST['email']
            result=User.objects.filter(phone=phone,email=email).exists()
            if result==False:
                messages.error(request,'Uable to Validate your account , please enter correct details')
            else:
                userobj=User.objects.get(phone=phone,email=email)
                fm=ForgotPasswordForm(user=userobj,initial={'phone':phone,'email':email})
                return render(request,'forgotpasswordform.html', {'form':fm})
        else:
            messages.error(request,'kindly provide valid details')          
    else:
        fm = UserValidate()
    return render(request,'uservalidator.html',{'form':fm})




def ForgotPassword(request):
    if request.method=='POST':
        phone=request.POST['phone']
        email=request.POST['email']

        if User.objects.filter(phone=phone,email=email).exists():
            userobj=User.objects.get(phone=phone,email=email)
            fm=ForgotPasswordForm(data=request.POST,user=userobj)
            if fm.is_valid():
                fm.save()
                messages.success(request, ' Password Changed ')
                return redirect('login')
            else:
                return render(request,'forgotpasswordform.html',{'form':fm})
        else:
            messages.error(request, 'User not found ')
    else:
        return render(request, "error.html", {'error': '404 Page Not found '})

    