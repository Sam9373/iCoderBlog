from django.shortcuts import render,HttpResponse,redirect
from . models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from blog.models import Post

# Create your views here.
def home(request):
    return render(request,'home/home.html')
    # return HttpResponse('This is home')

def contact(request):
    # in [] we have used name field in html page
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content=request.POST['content']
        # print(name,email,phone,content)
        # django msg framework
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "Please fill the form correctly")
        else:    
            contact=Contact(name=name,email=email,phone=phone,content=content)
            contact.save()
            messages.success(request, "your message is successfully sent")
    return render(request,'home/contact.html')

def about(request):
    return render(request,'home/about.html')

def search(request):
    # allPosts=Post.objects.all()
    query=request.GET.get('query')
    if len(query)>80:
        # empty query set
        allPosts=Post.objects.none()
    else:
        allPostsTitle=Post.objects.filter(title__icontains=query)
        allPostsAuthor= Post.objects.filter(author__icontains=query)
        # allPostsContent=Post.objects.filter(content_icontains=query)
        allPosts=  allPostsTitle.union(allPostsAuthor)
        
    if allPosts.count() == 0:
        messages.warning(request, "No search results found.Please refine your queries")
        
    params={'allPosts':allPosts,'query':query}
    # return HttpResponse('This is search')
    return render(request,'home/search.html',params)


def handleSignup(request):
    if request.method=='POST':
        # get the post parameters
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        
        # check for errornous input
        # usrname must contains only 10 letters
        if len(username)>10:
             messages.success(request," Your user name must be under 10 characters")
        return redirect('home')
    
        # passwords should match
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('home')
         
        # username must be alphanumeric 
        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('home')
            
            
        
        #Create the user
        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request,"Your account has been suceessfully created")
        return redirect('home')
            
    else:
        return HttpResponse('404-Not found')
    
def handleLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")

    return HttpResponse("404- Not found")
    # return HttpResponse('This is login')

def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')
    # return HttpResponse('This is logout')
    

