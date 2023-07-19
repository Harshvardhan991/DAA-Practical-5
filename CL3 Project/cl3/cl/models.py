from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

class Admission(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='admissionuser',null=True,blank=True)
    regno = models.CharField(max_length = 50)
    sname = models.CharField(max_length = 100)
    classes = models.CharField(max_length = 30)
    branch = models.CharField(max_length = 30)
    doa = models.DateField(auto_now=False, auto_now_add=False)
    semester =  models.PositiveIntegerField()

    def __str__(self):
        return '%s' % (self.regno)

class Student(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    sname = models.CharField(max_length = 70)
    regno = models.ForeignKey(Admission,related_name='regno_Student_set', on_delete=models.CASCADE)
    address = models.CharField(max_length = 100)
    taluka = models.CharField(max_length = 30)
    district = models.CharField(max_length = 30)
    state = models.CharField(max_length = 30)
    pincode = models.PositiveIntegerField()
    

class Marks(models.Model):
    regno =  models.ForeignKey(Admission,related_name='mregno_Student_set', on_delete=models.CASCADE)
    subject = models.CharField(max_length = 50)
    mark = models.CharField(max_length = 50)
    semester = models.CharField(max_length = 50)
    year = models.CharField(max_length = 10)

# class Collect(models.Model):
#     name = models.CharField(max_length = 70)
#     email = modelsCharField(max_length=70)
#     age = models.CharField(max_length=40)
#     phone = models.CharField(max_length=40)
#     amount = models.CharField(max_length=100)
#     # regno = models.CharField(max_length=100)
#     order_id = models.CharField(max_length=100,blank=True)
#     # razorpay_payment_id = models.CharField(max_length=100,blank=True)
#     paid = models.BooleanField(default=False)

class Registration(models.Model):
    name = models.CharField(max_length = 70)
    email = models.CharField(max_length=70)
    age = models.CharField(max_length=40)
    phone = models.CharField(max_length=40)
    amount = models.CharField(max_length=100)
    # regno = models.CharField(max_length=100)
    order_id = models.CharField(max_length=100,blank=True)
    # razorpay_payment_id = models.CharField(max_length=100,blank=True)
    paid = models.BooleanField(default=False)

# class User(models.Model):
#     name = models.CharField(max_length=70)
#     email = models.CharField(max_length=70)
#     pass1 = models.CharField(max_length=20)
    


    
           
 





