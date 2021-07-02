from django.shortcuts import render
from .models import Product,Payment
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def index(request):
    products=Product.objects.all()
    return render(request,'index.html',{'products':products})


def payment(request,foodname,price,image):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        address=request.POST['address']
        nameoncard=request.POST['nameoncard']
        creditcardnumber=request.POST['creditcardnumber']
        cvv=request.POST['cvv']
        date=request.POST['date']
        Price=request.POST['price']
        if not Price or int(Price)!=price:
            messages.success(request,'Fill right amount of item as it is mentioned')
            return render(request,'index1.html',{'price':price})
       
        payment=Payment(name=name,email=email,address=address,nameoncard=nameoncard,creditcardnumber=creditcardnumber,cvv=cvv,date=date,price=price,foodname=foodname)
        payment.save()
        subject='Thank you for your response'
        message='Welcome to FoodVilla {}. We got your email for {} having price Rs. {}. We will reach out to you as soon as possible on the address {}. Thank You'.format(name,foodname,price,address)
        from_email=settings.EMAIL_HOST_USER
        to_list=[email,from_email]
        send_mail(subject,message,from_email,to_list,fail_silently=True)

        return render(request,'index2.html',{'name':name})


    else:
         return render(request,'index1.html',{'price':price,'foodname':foodname,'image':image})