from django.contrib import admin
from cl.models import  Student,Admission,Marks,Registration
import razorpay
# Register your models here.
class student_admin(admin.ModelAdmin):
    
    list_display=('sname','regno','address','taluka','district','state','pincode','pincode')
admin.site.register(Student,student_admin) 

class Admission_admin(admin.ModelAdmin):
    list_display=('regno','sname','classes','branch','doa','semester')
admin.site.register(Admission,Admission_admin)

class marks_admin(admin.ModelAdmin):
    list_display=('regno','subject','mark','semester','year')
admin.site.register(Marks,marks_admin)

# class Collect_admin(admin.ModelAdmin):
#     list_display=('sname','amount','regno','order_id','razorpay_payment_id','paid')
# admin.site.register(Collect,Collect_admin)

class register_admin(admin.ModelAdmin):
        list_display=('name','email','age','phone','amount','order_id','paid')
admin.site.register(Registration,register_admin)

# class user_admin(admin.ModelAdmin):
#     list_display=('name','email','pass1')
# admin.site.register(User,user_admin)

