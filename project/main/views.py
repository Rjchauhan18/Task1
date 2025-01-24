from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User,Group
from django.contrib import messages
from .form import CreateForm
from django.contrib.auth.decorators import login_required


# def signup(request):
#     if request.method == 'POST':
#         form = CreateForm(request.POST, request.FILES)
#         if form.is_valid():
#             user = form.save()
#             username = form.cleaned_data.get('username')

            
#             role = request.POST.get('role')  
#             if role == 'patient':
#                 user.groups.add(Group.objects.get(name='Patient'))
#             elif role == 'doctor':
#                 user.groups.add(Group.objects.get(name='Doctor'))

#             messages.success(request, 'Account was created for ' + username)
#             return redirect('login')
#     else:
#         messages.error(request, "User account not created.")

#         form = CreateForm()
#     return render(request, 'auth/signup.html', {'form': form})
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib import messages
from .form import CreateForm
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        form = CreateForm(request.POST, request.FILES)  # Include request.FILES to handle file uploads
        if form.is_valid():

            user = form.save(commit=False)  # Don't save to the database yet
            user.set_password(form.cleaned_data.get('password1'))  # Hash the password
            user.save()  # Save the user
            print("Uploaded file:", request.FILES.get('photo'))


            # Assign role to the user
            role = form.cleaned_data.get('role')
            if role == 'Patient':
                group, _ = Group.objects.get_or_create(name='Patient')
                user.groups.add(group)
            elif role == 'Doctor':
                group, _ = Group.objects.get_or_create(name='Doctor')
                user.groups.add(group)

            messages.success(request, f'Account was created for {user.username}')
            return redirect('login')  # Redirect to login page after successful signup
        else:
            print(form.errors)
            messages.error(request, "Please correct the errors below.")
    else:
        form = CreateForm()

    return render(request, 'auth/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.role == 'Doctor':
                return redirect('doctor_dashboard')
            elif user.role == 'Patient':
                return redirect('patient_dashboard')
            else:
                messages.error(request, "User does not have a valid role.")
                return redirect('login')
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'auth/login.html')

    return render(request, 'auth/login.html')


# Logout View
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def doctor_dashboard(request):
    return render(request, 'doctor/dashboard.html')

@login_required(login_url='login')
def patient_dashboard(request):
    return render(request, 'patient/blog_page.html')
