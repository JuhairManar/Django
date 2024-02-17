from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *

# Create your views here.


def home(request):
    electric_cars = ElectricCar.objects.all()
    gas_cars = GasCar.objects.all()
    
    context = {
        'electric_cars': electric_cars,
        'gas_cars': gas_cars,
    }

    return render(request, 'car_display.html', context)

def add_cars(request):
    if not request.user.is_authenticated:
        messages.error(request, "You need to be Signup in to add cars.")
        return redirect('signup')

    if request.method == 'POST':
        car_type = request.POST.get('carType')
        name = request.POST.get('name')
        model = request.POST.get('model')
        year = request.POST.get('year')
        user = request.user  # Get the currently logged-in user

        if car_type == 'Electric':
            battery_capacity = request.POST.get('batteryCapacity')
            ElectricCar.objects.create(
                user=user,
                name=name,
                model=model,
                year=year,
                battery_capacity=battery_capacity
            )
        elif car_type == 'Gas':
            fuel_efficiency = request.POST.get('fuelEfficiency')
            GasCar.objects.create(
                user=user,
                name=name,
                model=model,
                year=year,
                fuel_efficiency=fuel_efficiency
            )

        # Redirect to 'car_display'
        return redirect('car_display')

    return render(request, 'add_cars.html')

def signup(request):
    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == 'POST':
        form = Registerform(request.POST)
        if form.is_valid():
            # Log the user in
            user = form.save()
            login(request, user)

            # Add a success message
            messages.success(request, "Account Created Successfully")

            # Redirect to the profile page
            return redirect('profile')

    else:
        form = Registerform()

    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            print("valid")
            name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username=name, password=user_pass)
            # print("valid")
            # user_email = form.cleaned_data['email']
            # user_pass = form.cleaned_data['password']
            # print(user_email)
            # print(user_pass)
            # user = authenticate(email=user_email, password=user_pass)
            if user is not None:
                #print("User Exist")
                login(request, user)
                return redirect('profile')
            else:
                print("User not Exist")
                form = AuthenticationForm()
                messages.error(request, "Invalid username or password")
                return render(request, "login.html", {'form': form})
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def profile(request):
    return render(request, 'profile.html', {'user': request.user})

        