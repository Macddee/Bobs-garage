from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.auth import logout as django_logout
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .models import Products
# Create your views here.
# def Home(request):
#     return render(request, "home.html", {})

def Home(request):
    
    products = Products.objects.all()
   
    searchQuiry = request.GET.get("search")

    if searchQuiry:
        found = Products.objects.get(title=searchQuiry)
        if found:
            products = found
        else:
            return Response(status.HTTP_404_NOT_FOUND)

    allProducts = {
        'products': products
    }   
    
    return render(request, 'home.html', allProducts)
    
def About(request):
    return render(request, 'about.html', {})

def Buy(request, id):
    product = Products.objects.get(id=id)
    categ = Products.objects.filter(category=product.category).exclude(title=product.title)

    purchase = {
        "product": product,
        "category": categ
    }
    print(purchase)
    return render(request, 'buy.html', purchase)


def Specials(request):
    return render(request, 'specials.html', {})

def SignUp(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Hi {username}, your aaccount was successfuly created")
            return HttpResponseRedirect("../")
        else:
            messages.success(request, f"Account not successfuly created, recheck your details")
            form = UserCreationForm()

    form = UserCreationForm
    context={
        "form": form
    }
    return render(request, 'sign_up.html', context)

def logout(request):
    django_logout(request)
    return HttpResponseRedirect("../")

def Search(request):
    if request.method == "GET":
        queryStr = request.GET.get('query')

        if queryStr:
            found = Products.objects.filter(title__icontains=queryStr)
            results = {
                "product": found
            }
            return render(request, 'search.html', results)
        else:
            return render(request, 'search.html', {})





