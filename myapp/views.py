from django.shortcuts import render
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
    breakpoint()
    products_dict = {
        "product1": "abc",
        "product2": "def",
        "product3": "ght"
    }
    return JsonResponse(
        {
            "YourProduct": products_dict[pname]
        })

    
