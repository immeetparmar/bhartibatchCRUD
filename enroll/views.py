from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Sum, Max, Min, Avg, Count
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
           return HttpResponseRedirect("/")
    else:
        form = Productform()
    
    # Get all products
    all_products = Product.objects.all().order_by('-id')
    
    # Calculate statistics
    stats = Product.objects.aggregate(
        total_count=Count('id'),
        total_value=Sum('price'),
        max_price=Max('price'),
        min_price=Min('price'),
        avg_price=Avg('price')
    )
    
    # Get most expensive and least expensive products
    most_expensive = Product.objects.order_by('-price').first()
    least_expensive = Product.objects.order_by('price').first()
    
    # Pagination - 12 products per page
    paginator = Paginator(all_products, 12)
    page_number = request.GET.get('page')
    prod = paginator.get_page(page_number)
    
    stud = Student.objects.all()
    
    context = {
        "prod": prod,
        "form": form,
        "stud": stud,
        "stats": stats,
        "most_expensive": most_expensive,
        "least_expensive": least_expensive,
    }
    
    return render(request, "enroll/home.html", context)


def product_detail(request, id):
    """Display detailed view of a single product"""
    product = get_object_or_404(Product, pk=id)
    return render(request, "enroll/detail.html", {"product": product})


def update(request, id):
    if request.method == "POST":
        pi = Product.objects.get(pk=id)
        fm = Productform(request.POST, request.FILES, instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect("/")
    else:
        pi = Product.objects.get(pk=id)
        fm = Productform(instance=pi)
    return render(request, "enroll/update.html", {"form": fm, "product": pi})


def delete(request, id):
    if request.method == "POST":
        pi = Product.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect("/")


def about(request):
    """View for the About Us page."""
    return render(request, "enroll/about.html")


def contact(request):
    """View for the Contact Us page."""
    return render(request, "enroll/contact.html")
