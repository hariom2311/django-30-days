from django.db import models
from django.contrib.auth.models import User

class BusinessProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='business_profile')
    business_name = models.CharField(max_length=255)
    business_type = models.CharField(max_length=255)
    
    # Address Parts
    street_address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    
    profile_picture = models.ImageField(upload_to='business_profiles/', null=True, blank=True)
    
    # Additional Fields
    contact_email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    website = models.URLField(max_length=200, blank=True, null=True)
    established_date = models.DateField()
    description = models.TextField(blank=True, null=True)
    
    # Separate fields for start and end hours
    start_hour = models.TimeField(blank=True, null=True)
    end_hour = models.TimeField(blank=True, null=True)
    
    # Field for off day
    off_day = models.CharField(max_length=15, blank=True, null=True)  # You can use CharField for the day of the week, e.g., "Sunday"

    def __str__(self):
        return self.business_name


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customers')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email}"

class PurchasedDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchases_made')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='purchases')
    product_purchased = models.CharField(max_length=255)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    pending_amount = models.DecimalField(max_digits=10, decimal_places=2)
    purchased_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer} - {self.product_purchased}"