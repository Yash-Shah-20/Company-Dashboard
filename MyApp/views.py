from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
# Create your views here.

def Login(req):
    if req.POST:
        em=req.POST['email']
        password=req.POST['password']
        try:
            obj=CompanyRegister.objects.get(email=em)
            if obj.password==password:         
                req.session['user']=obj.id
                return redirect('Dashboard/')                             
            else:
                return HttpResponse('<h1>Either email or password id incorrect</h1>')
        except:
            return HttpResponse('<h1>Some Error Occured</h1>')            
    return render(req,'Company_Login/Login.html')

def Register(req):
    if req.POST:
        fname=req.POST['fname']
        lname=req.POST['lname']
        em=req.POST['email']
        password1=req.POST['password1']
        password2=req.POST['password2']
        canAdd=False

        try:
            obj=CompanyRegister.objects.get(email=em)
            canAdd=False
            return HttpResponse('<h1>User Already Exists..</h1>')
        except:
            canAdd=True

        if canAdd:
            if fname=="" or lname=="" or em=="" or password1=="":
                return HttpResponse('<h1>Some Error Occured</h1>')   
            if password1==password2:
                ob=CompanyRegister()
                ob.fname=fname
                ob.lname=lname
                ob.email=em
                ob.password=password1
                ob.save()
                return redirect('Login/')
            else:
                return HttpResponse('<h1>Both passwords not Matched</h1>')
    return render(req,'Company_Login/Register.html')

def Dashboard(req):
    if 'user' in req.session.keys():
        User=CompanyRegister.objects.get(id=int(req.session['user']))
        return render(req,'Company_Dashboard/index.html',{'USER':User})
    else:
        return redirect('Login/')

def Logout(req):
    if 'user' in req.session.keys():
        del req.session['user']
    return redirect('Login/')
    
def ViewCustomer(req):
    if 'user' in req.session.keys():
        User=CompanyRegister.objects.get(id=int(req.session['user']))
        Customer=Customers.objects.filter(company=User)
        return render(req,'Company_Dashboard/ViewCustomer.html',{'USER':User,'Customer':Customer})
    else:
        return redirect('Login/')

def AddCustomer(req):
    if 'user' in req.session.keys():
        User=CompanyRegister.objects.get(id=int(req.session['user']))
        if req.POST:
            company=User
            fn=req.POST['custfname']
            ln=req.POST['custlname']
            em=req.POST['custemail']
            password="123"
            canAdd=False

            try:
                obj=Customers.objects.get(email=em)
                canAdd=False
                return HttpResponse('<script>alert("Customer Already Exists..")</script>')
            except:
                canAdd=True

            if canAdd:
                if fn=="" or ln=="" or em=="" or password=="":
                    return HttpResponse('<h1>Some Error Occured</h1>') 
                ob=Customers()
                ob.company=company
                ob.fname=fn
                ob.lname=ln
                ob.email=em
                ob.password=password
                ob.save()
                # return redirect('UpdateCustomer/')   
                return redirect('ViewCustomer/')  
            else:
                return redirect('ViewCustomer/')              
                
            
        return render(req,'Company_Dashboard/AddCustomer.html',{'USER':User})
    else:
        return redirect('Login/')

def DeleteCustomer(req,id):
    if 'user' in req.session.keys():
        cust=Customers.objects.get(id=id)
        cust.delete()
        return redirect('ViewCustomer/')
    else:
        return redirect('Login/')

def UpdateCustomer(req,id):
    if 'user' in req.session.keys():
        User=CompanyRegister.objects.get(id=int(req.session['user']))
        cust=Customers.objects.get(id=id)
        if req.POST:
            fn=req.POST['custfname']
            ln=req.POST['custlname']
            em=req.POST['custemail']
          
            canAdd=True

            if canAdd:
                if fn=="" or ln=="" or em=="":
                    return HttpResponse('<h1>Some Error Occured</h1>')              
                cust.fname=fn
                cust.lname=ln
                cust.email=em             
                cust.save()
            return redirect('ViewCustomer/')
        return render(req,'Company_Dashboard/UpdateCustomer.html',{'USER':User,'Cust':cust})
    else:
        return redirect('Login/')

def Orders(req):
    return render(req,'Orders/orders.html')