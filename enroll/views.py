from django.shortcuts import render, HttpResponseRedirect
from .models import Product, Student
from .forms import Productform
# Create your views here.

def home(request):
    if request.method == "POST":
       form = Productform(request.POST, request.FILES)
       if form.is_valid():
           nm = form.cleaned_data["name"]
           dc = form.cleaned_data["desc"]
           pr = form.cleaned_data["price"]
           img = form.cleaned_data.get("image")
           reg = Product(name=nm, desc=dc, price=pr, image=img)
           reg.save()
           form = Productform()
    else:
        form = Productform()
    prod = Product.objects.all()
    stud = Student.objects.all()
    return render(request, "enroll/home.html", {"prod":prod, "form":form, "stud":stud})

def update(request, id):
    if request.method == "POST":
        pi = Product.objects.get(pk=id)
        fm = Productform(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Product.objects.get(pk=id)
        fm = Productform(instance=pi)
    return render(request, "enroll/update.html", {"form":fm})


def delete(request, id):
    if request.method == "POST":
        pi = Product.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect("/")



