from django.shortcuts import render,redirect
from django.http import JsonResponse
# Create your views here.

def home(request):
    return JsonResponse({"PageName": "Hey I am home page"})

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