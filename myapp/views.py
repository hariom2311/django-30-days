from django.shortcuts import render,redirect
from django.http import JsonResponse
from myapp.utils import is_strong_password
# Create your views here.
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from myapp.models import Customer, PurchasedDetails, BusinessProfile
from django.db.models import Sum, F, FloatField
from decimal import Decimal
from datetime import datetime

@login_required(login_url='/login/')
def home(request):
    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        phone_number=request.POST.get('phone_number')
        email=request.POST.get('email')
        Customer.objects.create(user=request.user, first_name=first_name, last_name=last_name, phone_number=phone_number,email=email)
        return redirect('/')
    customers = Customer.objects.filter(user=request.user)

    # Calculate total purchased amount and total pending amount for each customer
    customers_with_totals = []
    for customer in customers:
        total_purchased_amount = PurchasedDetails.objects.filter(customer=customer).aggregate(total=Sum(F('total_amount'), output_field=FloatField()))['total'] or Decimal('0.00')
        total_pending_amount = PurchasedDetails.objects.filter(customer=customer).aggregate(total=Sum(F('pending_amount'), output_field=FloatField()))['total'] or Decimal('0.00')
        customers_with_totals.append({
            'customer': customer,
            'total_purchased_amount': total_purchased_amount,
            'total_pending_amount': total_pending_amount,
        })
    return render(request, 'myapp/customer-form.html', {'customers': customers_with_totals})


@login_required(login_url='/login/')
def update_customer(request, id):
    customer = Customer.objects.get(id=id)
    if request.method=="POST":
        product_purchased = request.POST.get("product_purchased")
        total_amount = float(request.POST.get("total_amount"))
        paid_amount = float(request.POST.get("paid_amount"))
        pending_amount = total_amount-paid_amount
        PurchasedDetails.objects.create(user=request.user,
            customer=customer, 
            product_purchased=product_purchased,
            total_amount=total_amount,
            paid_amount=paid_amount,
            pending_amount=pending_amount
        )
        return redirect(f'/update-customer/{id}')
    customer_previous_purchased_details = PurchasedDetails.objects.filter(customer=customer)
    return render(request, "myapp/update-customer.html", {"customer_previous_purchased_details": customer_previous_purchased_details})

@login_required(login_url='/login/')
def update_profile(request):
    try:
        # Attempt to get the existing profile for the user
        business_profile = BusinessProfile.objects.get(user=request.user)
    except BusinessProfile.DoesNotExist:
        # If the profile does not exist, create a new one
        business_profile = BusinessProfile(user=request.user)
    if request.method=="POST":
        business_profile.business_name = request.POST.get("business_name")
        business_profile.business_type = request.POST.get("business_type")
        business_profile.street_address = request.POST.get("street_address")
        business_profile.city = request.POST.get("city")
        business_profile.state = request.POST.get("state")
        business_profile.postal_code = request.POST.get("postal_code")
        business_profile.country = request.POST.get("country")
        business_profile.contact_email = request.POST.get("contact_email")
        business_profile.phone_number = request.POST.get("phone_number")
        business_profile.website = request.POST.get("website")
        if request.POST.get("established_date"):
            business_profile.established_date = datetime.strptime(request.POST.get("established_date"), "%Y-%m-%d").date()
        business_profile.description = request.POST.get("description")
        if request.POST.get("start_hour"):
            business_profile.start_hour = request.POST.get("start_hour")
        if request.POST.get("end_hour"):
            business_profile.end_hour = request.POST.get("end_hour")
        business_profile.off_day = request.POST.get("off_day")
        if request.FILES:
            business_profile.profile_picture = request.FILES.get("profile_picture")
        business_profile.save()
        return redirect("/")
    return render(request, "myapp/profile.html")

@login_required(login_url='/login/')
def view_profile(request):
    try:
        business_profile = BusinessProfile.objects.get(user=request.user)
    except:
        return JsonResponse({"Message": "Profile is not available for thi user"})
    return render(request, "myapp/view-profile.html", {"business_profile": business_profile})
@login_required(login_url='/login/')
def delete_customer(request, id):
    return JsonResponse({"Message": "Customer Deleted succesfully!"})

@login_required(login_url='/login/')
def about(request):
    return JsonResponse({"AboutMe": "Hey I am Hariom"})

@login_required(login_url='/login/')
def products(request):
    return JsonResponse({
        "product1": "abc",
        "product2": "def",
        "product3": "ght"
    })

@login_required(login_url='/login/')
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