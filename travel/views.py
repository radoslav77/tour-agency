from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate 
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseNotFound
import requests, datetime
from django.urls import reverse


from .forms import *
from .models import *

'''
url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/referral/v1.0/%7Bcountry%7D/%7Bcurrency%7D/%7Blocale%7D/%7Boriginplace%7D/%7Bdestinationplace%7D/%7Boutboundpartialdate%7D/%7Binboundpartialdate%7D"

querystring = {"shortapikey":"ra66933236979928","apiKey":"{shortapikey}"}

headers = {
    'x-rapidapi-key': "34cb6159c3msheb04ec7d529d2d8p1d889djsn1e930d12a11b",
    'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
'''
# Create your views here.

history = []

def index(request):
    country = Country.objects.all()
    
    cat = []
    
    for p in country:
        cat.append({
            p.country:p.country})    
    #cat = list(dict.fromkeys(cat)) 
    #print(cat)  
    return render(request, "travel/index.html",{
        "country":country,
        "cat":cat,
        "form":SearchForm()
        })

def contact(request):
    return render(request, "travel/contact.html")
    

def blog(request):
    country = Country.objects.all()
    cat = []
    
    for p in country:
        cat.append(p.categories)    
    cat = list(dict.fromkeys(cat))
     
    post = Blog.objects.all()
    archive = Archive.objects.all()
    return render(request, "travel/blog.html",{
       "posts":post,
       "country":cat,
       "archive":archive      
   })

def category(request, categories):
    post = Country.objects.filter(categories=categories) 
    
    return render(request, "travel/category.html",{
        "posts":post,
        "category":categories
    })

def offers(request):
    country = Country.objects.all() 
    return render(request, "travel/offers.html",{
        "country": country
        
    })

def hot_tours(request):
    coun = Country.objects.all()
   
    return render(request, "travel/tours.html",{
        "coun": coun
    })


def blogdetails(request, blog_id):
    post = Blog.objects.get(id=blog_id)
    
    return render(request, "travel/blogdetails.html",{
        "detail":post 
        
    })
def country(request, counrty_id):
    country = Country.objects.filter(id=counrty_id)
    name =[country for country in Country.objects.filter(id=counrty_id)]

    return render(request, "travel/country.html",{
        "posts":country,
        "name":name[0] 
    })

def register(request):
    

    if request.method == "POST":
            form = registrationForm(request.POST or None)
            #Check if form is valid 
            if form.is_valid():
                user = form.save()
                
                # Get user password
                raw_password = form.cleaned_data.get('password1')
                
                #authenticate user 
                user = authenticate(username=user.username, password= raw_password)
                #login user
                login(request,user)
                return redirect('index')
    else:
        form = registrationForm()
    return render(request, 'travel/register.html',{'form':form}) 

def login_user(request):
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            
            #Check credential
            user = authenticate(username=username,password=password)
            
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('index')
                else:
                    return render(request, 'travel/login.html',{
                        'error':"Your account has been desaibled."
                        })
                
            else:
                return render(request, 'travel/login.html',{
                    'error':'Invalid username or password. Try Again.'
                    })
                
        return render (request, 'travel/login.html')

def logout_user(request):
    if request.user.is_authenticated:
        
        logout(request)
        return redirect('login')
    else:
        return redirect('login')

def profile(request):
    if request.user.is_authenticated:
        history = Checkout.objects.filter(user=request.user)
        for h in history:
            holidays = h.title 
        return render(request, "travel/profile.html",{
            "history":holidays
        })

    else:
        return redirect('index')  

def add_post(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
        
    
            if request.method == "POST":
                form = PostForm(request.POST or None) 
                
                
               #check if form is valid or not 
                if form.is_valid():
                    data = form.save(commit=False)
                    data.save()
                    return redirect('index')
            else:
                form = PostForm()
            return render(request, 'travel/post.html', {
                'form':form,
                'controller':"Add new holiday packedge!"
                })
        #if they are not admin
        else:
            return redirect('index')
            
    #if they are n login 
    return redirect('login')

def search(request):
    if request.method == "POST":
        counrty_id = request.POST["Choose_country"]
        date = request.POST["When_would_you_travel"]
        people = request.POST["How_many_people"]

       
        if not counrty_id:
            form = SearchForm()
            return redirect(request, "travel/index.html", {
                "form":form
            })
        else:                
            return redirect("country", counrty_id)       

    return HttpResponseRedirect("offers")


def booking(request, title):

    if request.user.is_authenticated:
        if request.method =="GET":
            name = Blog.objects.filter(title=title)
            
            return render(request, "travel/booking.html",{
               
                "name":title,
                "controller": "Please fill the form!"
            })
        elif request.method == "POST":
            holiday = Blog.objects.filter(title=title)
      
            for price in holiday:
                cost=float(price.price)
               
            holiday = title
            from_date = request.POST["from"]
            till_date = request.POST["till"]
            travelers = request.POST["travelers"]
            people = float(travelers) * cost 
            total = people + 25 + 20    

            book = Booking(holiday=holiday,from_date=from_date,till_date=till_date,travelers=travelers)
            book.save()
            
            history.append(title)
            return render(request, "travel/checkout.html",{
                "title":title,
                "name":cost,
                "travelers":people,
                "number":travelers,
                "total":total
            })
    else:
        msg = "Please Login in order to make a booking!"
        return render(request, "travel/booking.html",{
               
        "name":title,
        "controller": "Please fill the form!",
        "msg":msg
        })
        
      

def checkout(request):
 
    if request.method == "POST":
        title = history
        name = request.POST["firstname"]
        email = request.POST["email"]
        address = request.POST["address"]
        city = request.POST["city"]
        card_name = request.POST["cardname"]
        card_number = request.POST["cardnumber"]
        expmonth = request.POST["expmonth"]
        expyear = request.POST["expyear"]
        cvv = request.POST["cvv"]
        post_code = request.POST["post_code"]

        pay = Checkout(title=title,user= request.user,user_name=name,email=email,address=address,city=city,card_name=card_name,card_number=card_number,expmonth=expmonth,expyear=expyear,cvv=cvv,post_code=post_code)
        pay.save()
        message = "Check your details! "

 
        return render(request, "travel/confirmation.html",{
            "msg": message,
            "detail":pay
        })    

    return render(request, "travel/checkout.html") 
