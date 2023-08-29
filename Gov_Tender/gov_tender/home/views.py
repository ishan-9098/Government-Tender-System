from django.shortcuts import get_object_or_404, render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from home.models import feedback
from home.models import Company_profile
from home.models import tender
from home.models import create_progress
from home.models import applications
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.exceptions import ValidationError

# Create your views here.

def index(request):
    # return HttpResponse("This is home page")
    return render(request,'index.html')

# def handlesignup(request):
#     if request.method =='POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         password1 = request.POST['password1']
#         password2 = request.POST['password1']

#         # checks for error
#         if password1 != password2:
#             messages.error(request,"Password do not match")
#             return redirect('home')
#         #create the user
#         myuser = User.objects.create_user(username,email,password1)
#         myuser.save()
#         messages.success(request,'Company is Registered successfull...!')
#         return redirect('home')
#     else:
#         return HttpResponse('404 - Not Found')

def handlesignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']  

    
        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect('home')

        
        try:
            UnicodeUsernameValidator()(password1)
        except ValidationError as e:
            messages.error(request, f"Invalid password: {', '.join(e.messages)}")
            return redirect('home')

    
        myuser = User.objects.create_user(username, email, password1)
        myuser.save()
        messages.success(request, 'Company is registered successfully!')
        return redirect('home')
    else:
        return HttpResponse('404 - Not Found')



def handlelogin(request):
    if request.method =='POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpass']
     
        user = authenticate(username =loginusername, password=loginpassword)

        if user is not None:
            login(request,user)
            messages.success(request,"Successfully logged In")
            return render(request,'company.html')
            # return redirect('home')
        else:
            messages.error(request,"Invalid Credentials, Please try again")
           
            return redirect('home')

def handlelogout(request):
    logout(request)
    messages.success(request,'Successfully logout')
    return redirect('home')

    return HttpResponse('hendlelogout')

def feedback(request):
    if request.method =="POST":
        name = request.POST.get('name')
        suggestion = request.POST.get('suggestions')
        rating = request.POST.get('rating')
        Feedback = feedback(name=name, suggestions=suggestion, rating=rating)
        Feedback.save()
    return render(request,'feedback.html')

def company(request):
    return render(request,'company.html')

def c_profile(request):
    if request.method =="POST":
        comp_id = request.POST.get('company_id')
        comp_name = request.POST.get('company_name')
        comp_phno = request.POST.get('company_phone')
        comp_add = request.POST.get('company_add')
        comp_email = request.POST.get('company_email')
        comp_Username = request.POST.get('company_name')
        Profile = Company_profile(C_id=comp_id,C_name = comp_name,C_phone=comp_phno,C_add=comp_add,C_email=comp_email,C_username=comp_Username)
        Profile.save()
        return render(request,'company.html')


def progress(request):
    return render(request,'progress.html')



def govlogin(request):
    if request.method =="POST":
        username = request.POST.get('loginusername')
        password = request.POST.get('loginpass')
        if username =="govind" and password =="govind":
            return render(request,'govofficial.html')
        else:
            return render(request,'index.html')

       
def managet(request):
    allTenders = tender.objects.all()
    return render(request,'managet.html',{"allTenders":allTenders})

def addtender(request):
    if request.method == "POST":
        t_id = request.POST.get('tender_id')
        sector_name = request.POST.get("sector_name")
        time = request.POST.get("time")
        price = request.POST.get("price")
        s_date = request.POST.get("start_date")
        e_date = request.POST.get("end_date")
        address = request.POST.get("address")
        city = request.POST.get("city")
        state = request.POST.get("state")
        pin = request.POST.get("pin")
        Descreption = request.POST.get("descreption")
       
        tenders = tender(t_id = t_id,sector_name = sector_name,Time_dur = time,
        price = price,Start_date =s_date, end_date = e_date, Address = address,
        city = city,state = state, pin = pin , descreption = Descreption)
        tenders.save()

        return render(request,'managet.html')

def viewtender(request):
    if request.method == "POST":
        t_id = request.POST.get("tid")
        tend = tender.objects.get(t_id=t_id)
        return render(request,'viewtender.html',{'tend':tend})

     
def handletender(request):
    alltenders = tender.objects.all()
    return render(request,'tenders.html',{"alltenders":alltenders})
     
def comp_apply(request):
     if request.method == "POST":
        t_id = request.POST.get("tid")

     alert_message = "You have applied successfully."
     response_content = f"""
        <html>
        <head>
            <script>
                window.onload = function() {{
                    alert("{alert_message}");
                }};
            </script>
        </head>
        <body>
            <p>{alert_message}</p>
        </body>
        </html>
    """
     return HttpResponse(response_content, status=200)

     
def create_progress(request):
    if request.method == "POST":
        tid_value = request.POST.get("tid")
        desc = request.POST.get("desc")
        
        progres = create_progress(tid = tid_value,descreption = desc)
        progres.save()
        return render(request,'tender.html')
    

def application(request):
    if request.method == "POST":
        t_id=request.POST.get("tid")
        c_name=request.POST.get("c_name")

        apply = applications(tid=t_id, company_name=c_name)
        apply.save()
        return render(request,'tenders.html')

def comp_apply(request):
    allapplis = applications.objects.all()
    return render(request,'Comp_appli.html',{"allapplis":allapplis})

def deltender(request):
    
    

    if request.method =="POST":
        id = request.POST.get("tid")
        obj = get_object_or_404(tender,pk=id)
        obj.delete()
        return render(request,'managet.html')
