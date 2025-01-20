from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User
# Create your views here.



# def register(request):
#     if request.method =="POST":
#         email=request.POST.get('email')
#         username=request.POST.get('username')
#         password_re=request.POST.get('password_re')


#         user=authenticate(password=password_re)
#         if not user:
#             messages.warning(request,'password not matching')
#             return redirect('user/register')

#         user= User.objects.filter(email = email)
#         if user.exists():
#             messages.info(request,'email already exist')
#             return redirect('/users/register/')



#         user= User.objects.filter(username=username)
#         if user.exists():
#             messages.info(request,'username already exists')
#             return redirect('/users/register/')

#         user =User.objects.create_user(
#             email=email,
#             username=username,
#             password_re=password_re

            
#         )
#         # for encripting the pass word wee ca use this 
#         user.set_password(password)
#         user.save()
        
#         return redirect('user/login' )
#     return render(request,'user/signup.html')


# def login_page(request):
#     if request.method == "POST":
#         email = request.POST.get('email')
#         password=request.POST.get('password')



#         user=User.objects.filter(email=email)

#         if not user.exists():
#             messages.warning(request,'account not found ')
#             return redirect('user/login/')
#         user=authenticate(email=email,password=password )
#         if user:
#             messages.success(request,'succesfully login ')
#             login(request,user)
#             return redirect ('/')
#         messages.warning(request,"invalid credential")
#         return redirect(request,'user/login')

#     return render(request,'user/signin.html')

# def register(request):
#     if request.method == "POST":
#         email = request.POST.get('email')
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         password_re = request.POST.get('password_re')

#         # Check if passwords match
#         if password != password_re:
#             messages.warning(request, 'Passwords do not match')
#             return redirect('user/register')

#         # Check if email already exists
#         if User.objects.filter(email=email).exists():
#             messages.warning(request, 'Email already exists')
#             return redirect('/users/register/')

#         # Check if username already exists
#         if User.objects.filter(username=username).exists():
#             messages.warning(request, 'Username already exists')
#             return redirect('/users/register/')

#         # Create user
#         user = User.objects.create_user(
#             email=email,
#             password=password,
#             password_re=password_re,
#         )

#         messages.success(request, 'Account created successfully. Please log in.')
#         return redirect('/admin')

    # return render(request, 'user/signup.html')
def register(request):
    if request.method == "POST":
        email = request.POST.get('email')
        username = request.POST.get('username')  # Uncomment if needed
        password = request.POST.get('password')
        password_re = request.POST.get('password_re')

        # Check if passwords match
        if password != password_re:
            messages.warning(request, 'Passwords do not match')
            return redirect('/user/register/')  # Redirect to the correct URL

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.warning(request, 'Email already exists')
            return redirect('/user/register/')  # Redirect to the correct URL
        if User.objects.filter(username=username).exists():
            messages.warning(request, 'Username already exists')
            return redirect('/users/register/')

        
        # Create user
        user = User.objects.create_user(
            email=email,
            username=username,
            
        )
        user.set_password(password)
        user.save()

        messages.success(request, 'Account created successfully. Please log in.')
        return redirect('/user/login/')  # Redirect to login page after successful registration

    return render(request, 'user/signup.html')

def login_page(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if user exists
        user = User.objects.filter(email=email).first()
        if not user:
            messages.warning(request, 'Account not found')
            return redirect('/user/login/')
        username=user.username
        # Authenticate user
        user = authenticate( username=user[0].username, password=password)
        if user :
            messages.success(request, 'Successfully logged in.')
            login(request, user)
            return redirect('/')
        
        messages.warning(request, 'Invalid credentials')
        return redirect('/user/login')
    return render(request, 'user/signin.html')







def home_page(request):
    return render(request,'sample.htm')