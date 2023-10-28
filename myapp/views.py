from django.shortcuts import render,redirect
from django.http import JsonResponse
from myapp.utils import is_strong_password
# Create your views here.
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

def home(request):
    # if request.method=="POST":
    #     customer_data = {}
    #     customer_data["first_name"]=request.POST.get('first_name')
    #     customer_data["last_name"]=request.POST.get('last_name')
    #     customer_data["phone_number"]=request.POST.get('phone_number')
    #     customer_data["email"]=request.POST.get('email')
    #     customer_data['status_code'] = 201
    #     return JsonResponse(customer_data)
    return render(request, 'myapp/customer-form.html')

def about(request):
    return JsonResponse({"AboutMe": "Hey I am Hariom"})

def products(request):
    return JsonResponse({
        "product1": "abc",
        "product2": "def",
        "product3": "ght"
    })

def get_product(request, pname):
    products_dict = {
        "product1": "abc",
        "product2": "def",
        "product3": "ght"
    }
    return JsonResponse(
        {
            "YourProduct": products_dict[pname]
        })

def register(request):
    if request.method=="POST":
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        if User.objects.filter(email=email).exists():
            return render(request, "myapp/register.html", context={"messages": "User with this email Exists."})
        if password!=confirm_password:
            return render(request, "myapp/register.html", context={"messages": "Password and Confirmed Password are not same."})
        if not is_strong_password(password):
            return render(request, "myapp/register.html", context={"messages": "Password is not strong."})
        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = firstname
        user.last_name = lastname  # Move the username to the first name field
        user.save()
        messages.info(request, "User Registered Successfully!")
        return redirect('/login/')
    return render(request, "myapp/register.html")

def login_user(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid Credentials!")
            return render(request, "myapp/login.html")
    return render(request, "myapp/login.html")
    
def customer(request):
    if request.method=="POST":
        customer_data = {}
        customer_data["first_name"]=request.POST.get('first_name')
        customer_data["last_name"]=request.POST.get('last_name')
        customer_data["phone_number"]=request.POST.get('phone_number')
        customer_data["email"]=request.POST.get('email')
        customer_data['status_code'] = 201
        return JsonResponse(customer_data)

    return render(request, 'myapp/customer-form.html')