from django.db import models
from account.models import User
from django.utils.translation import ugettext_lazy as _
# Create your models here.
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError

order_status = (
    ('cancelled', 'cancelled'),
    ('pending', 'pending'),
    ('accepted', 'accepted'), 
    ('picked', 'picked'),
    ('completed', 'completed')
)


def validatepincode(value):
    value = int(value)
    if value > 110001 and value < 110096 :
        return value
    else:
        raise ValidationError(" Ensure that pin code is of Delhi ")  
   
def validatephone(value):
    if value > 1000000000 and value < 9999999999:
        return value
    else:
        raise ValidationError(" Please enter a valid phone number")    


class OrderDB(models.Model):
    order_id = models.IntegerField(primary_key=True)

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='Customer')
    agent = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='delivery_agent', null=True)

    pick_address = models.CharField(max_length=250)
    pick_pincode = models.IntegerField(
        validators=[validatepincode])
    pick_phone = models.IntegerField(
        validators=[validatephone])
    pick_note = models.CharField(max_length=250, blank=True)
    pick_name = models.CharField(max_length=30)

    delivery_address = models.CharField(max_length=250)
    delivery_pincode = models.IntegerField(
        validators=[validatepincode])
    delivery_phone = models.IntegerField(
        validators=[validatephone])
    delivery_note = models.CharField(max_length=250, blank=True)
    delivery_name = models.CharField(max_length=30)

    status = models.CharField(choices=order_status,
                              default="pending", max_length=20)

    order_time = models.DateTimeField(auto_now_add=True)
    cancelled_time = models.DateTimeField(auto_now=False, null=True)
    accepted_time = models.DateTimeField(auto_now=False, null=True)
    picked_time = models.DateTimeField(auto_now=False, null=True)
    completed_time = models.DateTimeField(auto_now=False, null=True)

    weight = models.IntegerField()
    distance = models.IntegerField(null=True)
    bill = models.IntegerField(validators=[MinValueValidator(1)], null=True)
    pamyment_time = models.DateTimeField(auto_now=False, null=True)


class FeedbackDB(models.Model):
    order_id = models.OneToOneField(OrderDB, on_delete=models.CASCADE)
    feedback = models.CharField(max_length=250)
    datetime = models.DateTimeField(auto_now=False)
    lastmodified = models.DateTimeField(auto_now=True)
