from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
from django.contrib.auth.models import User
from cl.models import  Student,Admission,Marks,Registration
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

import razorpay
from cl3.settings import RAZOPAY_API_KEY, RAZOPAY_API_SECRET_KEY

# Create your views here.
def signupPage(request):
    if request.method=='POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if(pass1!=pass2):
            return HttpResponse('Password Not Matched')
        else:
            my_user=User.objects.create_user(name,email,pass1)
            my_user.save()
           
            return redirect('login')

    return render(request,'signup.html')

def loginPage(request):
    if request.method == "POST":
        username=request.POST.get('username')
        pass1 = request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password Incorrect")

    return render(request,'login.html')

def logoutPage(request):
    logout(request)
    return redirect('login')
           

@login_required(login_url='login') 
@csrf_exempt      
def home(request):
    return render(request,'homepage.html')

@login_required(login_url='login') 
def student(request):
    if request.method == "POST":
        sname = request.POST.get('name')
        regno = request.POST.get('regno')
        address = request.POST.get('address')
        taluka = request.POST.get('taluka')
        district = request.POST.get('district')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        en=Student(sname=sname,regno=Admission.objects.get(regno=regno),address=address,taluka=taluka,district=district,state=state,pincode=pincode)
        en.save()
        # Student.objects.create(sname=sname,regno=regno,address=address,taluka=taluka,district=district,state=state,pincode=pincode)

        return  redirect('do_payment')
    # render(request,"student.html")
    elif request.method=="GET":
        return render(request,"student.html")

@login_required(login_url='login') 
def admission(request):
    if request.method == "POST":
        regno = request.POST.get('regno')
        sname = request.POST.get('sname')
        classes = request.POST.get('classes')
        branch = request.POST.get('branch')
        doa = request.POST.get('doa')
        semester = request.POST.get('semester')
        en=Admission(regno=regno,sname=sname,classes=classes,branch=branch,doa=doa,semester=semester)
        en.save()
        # Admission.objects.create(regno=regno,sname=sname,classes=classes,branch=branch,doa=doa,semester=semester)

    return render(request,"admission.html")

@login_required(login_url='login') 
def marks(request):
    dict={}
    if request.method == "POST":
        regno = request.POST.get('regno')
        subject = request.POST.get('subject')
        mark = request.POST.get('mark')
        semester = request.POST.get('semester')
        year = request.POST.get('year')
        en=Marks(regno=Admission.objects.filter(regno=regno).first(),subject=subject,mark=mark,semester=semester,year=year)
        en.save()
        # Marks.objects.all(user=user,regno=regno,subject=subject,mark=mark,semester=semester,year=year)
    
    return render(request,"marks.html")
        
@login_required(login_url='login') 
def feedback(request):
    context={}
    adm = Student.objects.all()
    m = Marks.objects.all()
    a = Admission.objects.all()
    context = {'data': adm,
     'mdata': m,
     'adata': a
        }
    return render(request,"feedback.html",context)

@login_required(login_url='login') 
def search(request):
    context = {}
    adta = [];
    if request.method == "POST":
       sname = request.POST.get('sname')
       regno = request.POST.get('regno')
       branch = request.POST.get('branch')

       ad = Admission.objects.all();
       if sname:
            adata = ad.filter(sname__icontains=sname)
       if regno:
            adata = ad.filter(regno__icontains=regno)
       if branch:
            adata = ad.filter(branch__icontains=branch)
       context = {
        "adata":adata
       }
       return render(request,'feedback.html',context)

  # elif request.method == 'GET':              this can be written or not
    return render(request,'search.html')
 
@login_required(login_url='login') 
@csrf_exempt  
def thank(request):
    dict={
    'message':"Congrats you are admited"
    }
    return render(request,"thank.html",dict)

@login_required(login_url='login') 
def do_payment(request):
    return render(request,"do_payment.html")


client = razorpay.Client(auth=(RAZOPAY_API_KEY, RAZOPAY_API_SECRET_KEY))
@login_required(login_url='login') 
def payment(request):
    if request.method == 'POST':
       name=request.POST.get('username')
       email=request.POST.get('email')
       age=request.POST.get('age')
       phone=request.POST.get('phone')  
       amount=request.POST.get('amount') 

       order_amount = int(amount)*100
       order_currency = "INR"
       payment_order=client.order.create(dict(amount=order_amount,currency=order_currency,payment_capture=1))   
       payment_order_id=payment_order['id']
       order_status = payment_order['status']

       if order_status == 'created':
        en = Registration(
            name=name,
            email=email,
            age=age,
            phone=phone,
            amount=order_amount,
            order_id=payment_order_id,
            paid = True
        )
        en.save()
        
        context={
           'amount':amount, 
           'api_key':RAZOPAY_API_KEY,
           'order_id':payment_order_id
        }
        return render(request,'payment.html',context)
       
    return render(request,'payment.html')
    