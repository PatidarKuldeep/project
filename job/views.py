from django.contrib.auth.models import User
from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth import authenticate,login
from django.urls import reverse
from .models import Category, JobApplication, Jobs
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required




def home(request):
    return render(request,'home.html')

def aboutpage(request):
    return render(request,'about.html')
def contactus(request):
    return render(request,'contact.html')

def signin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        userpass=request.POST.get('password')
        user=authenticate(request,username=username,password=userpass)
        if user is not None:
            login(request,user)
            return redirect('homepage')
        else:
            return HttpResponse("User details are not correct")
    return render(request,'signin.html')

def signup(request):
    if request.method=='POST':
        uname=request.POST.get('name')
        uemail=request.POST.get('email')
        unumber=request.POST.get('number')
        upass=request.POST.get('password')
        upass1=request.POST.get('password1')
        if upass!=upass1:
            return HttpResponse("Please enter same password.....")
        if User.objects.filter(username=uname).exists():
            return HttpResponse("Username already exists. Please choose a different username.")
        else:
            my_user=User.objects.create_user(uname,uemail,upass)
            my_user.save()
            return redirect('signin')
    return render(request, 'signup.html')

def home1(request):   #after login
    object=Jobs.objects.all()
    return render(request,'home1.html',{'object':object})

def aboutfirst(request):    #after login
    return render(request,'about1.html')

def contactfirst(request):    #after login
    return render(request,'contact1.html')

def profile(request):
    if request.method == 'POST':
        user = request.user
        user_info={
            'username: ':user.username,
            'email: ':user.email,
        }
        return redirect('update')
    else:
        user = request.user
        user_info = {
            'username': user.username,
            'email': user.email,
            
        }
        return render(request, 'myprofile.html', {'user_info': user_info})

def update(request):
    if request.method == 'POST':    
        username = request.POST.get('username')
        email = request.POST.get('email')
        user = request.user
        user.username = username
        user.email = email
        user.save()
        login(request, user)  # Log the user in with the updated data

        return redirect('profile')
    else:
        user = request.user
        user_info = {
            'username': user.username,
            'email': user.email,
            
        }
        return render(request, 'update-profile.html', {'user_info': user_info})
    
def result(request):      #Job search by category
    if request.method == 'POST':
        job_category = request.POST.get('job_category')
        category = Jobs.objects.filter(job_category__categoryname=job_category)
        
        return render(request, 'result.html', {'category': category , 'job_category':job_category})
    return HttpResponse("Invalid request")

def job_application_form(request, job_id):        #After apply
    job = Jobs.objects.get(id=job_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        skills = request.POST.get('skills')
        cv = request.FILES.get('cv')

        job_application = JobApplication(
            name=name,
            email=email,
            address=address,
            skills=skills,
            cv=cv,
            job=job 
        )
        job_application.save()

        fs = FileSystemStorage()
        filename = fs.save(cv.name, cv)

        homepage_url = reverse('homepage')
        response_content = """
        <html>
        <head>
        <title>Application Submitted</title>
        </head>
        <body>
        <p>Application submitted successfully</p>
        <a href="{}"><button>Back to Home</button></a>
        </body>
        </html>
        """.format(homepage_url)
        return HttpResponse(response_content)
    return render(request, 'job_application_form.html', {'job': job})


@login_required
def job_applications_by_category(request, category_name):
    user_email = request.user.email
    applications = JobApplication.objects.filter(job__job_category__categoryname=category_name , email=user_email)
    return render(request, 'job_applications_by_category.html', {'applications': applications, 'category_name': category_name})


def job_application_details(request, application_id):
    application = JobApplication.objects.get(id=application_id)
    return render(request, 'job_application_details.html', {'application': application})


def user_logout(request):
    logout(request)
    return redirect('home')



