from django.shortcuts import render,HttpResponse , redirect
from home.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from blog.models import Post
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render (request,"home/home.html")

def about(request):
    messages.success(request,'This is my about')
    return render (request,"home/about.html")

def contact(request):
    
    if request.method=='POST':
        name=request.POST['name']                     
        email= request.POST['email']
        phonenumber=request.POST['phone']
        content=request.POST['content']
        print(name,email,phonenumber,content)
        if len(name)<2 or len(email)<3 or len(phonenumber)<10 or len(content)<4:
            messages.error(request,'Please fill the from correctly')
        else:
            contact=Contact(Name=name,Email=email,Phonenumber=phonenumber,Content=content)
            contact.save()
            messages.success(request,"Your message is succefully sent")
        
    return render (request,"home/contact.html")

def search(request):
    query=request.GET['query']
    if len(query)>90:
        allPosts=[]
    else:
        allPostsTitle=Post.objects.filter(title__icontains=query)
        allPostsContent=Post.objects.filter(content__icontains=query)
        allPosts=allPostsTitle.union(allPostsContent)
    if len(allPosts) == 0:
        messages.warning(request,'No suerch result found:...')
    parms={"allPosts":allPosts,'query':query}
    return render(request,"home/search.html",parms)

def handleSignup(request):
    
    if request.method == 'POST':
        username= request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        
        if len(username) > 10:
            messages.error(request,"Username must be under 10 Character")
            return redirect('home')
        
        if not username.isalnum():
            messages.error(request,"Username contains only numbers and character")
            return redirect('home')
        
        if pass1 != pass2:   
           messages.error(request,"Password do not match")
           return redirect('home')
       
                 
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,"Your account is created succfully ")
        return redirect("home")
    else:
        return HttpResponse('404 - not found')
    
def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        
        user = authenticate(username=loginusername,password=loginpassword)
        
        if user is not None:
            login(request,user)
            messages.success(request,"Succesfully Logged in")
            return redirect('home')
        else:
            messages.error(request,"Invalid user . try again")
            return redirect("home")

    return HttpResponse("It is login page")

def handleLogout(request):
    logout(request)
    messages.success(request,"you have sussecfully logout")
    return redirect("home")
