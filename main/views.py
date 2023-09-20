from django.shortcuts import render
from .models import Product
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
from main.models import Product
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_main(request):
    products = Product.objects.all()
    
    product_deskmate = Product(
        name = 'Deskmate',
        amount = 10,
        price = 150000,
        description = 'dengan DESKMATE yang sesuai dengan seleramu, membuat kamu nyaman saat nugas di atas meja'
    )
   
    product_lightbar = Product(
        name = 'Monitor Lightbar',
        amount = 20,
        price = 200000,
        description = 'dengan MONITOR LIGHTBAR memberikan estetika pada set up komputer atau laptop di meja Anda'
    )

    
    context = {
        'product_deskmate': product_deskmate,
        'product_lightbar': product_lightbar,
        'product1': 'Decor Mini Painting',
        'amount1': '13',
        'product2': 'Miniatur Figure',
        'amount2': '10',
        'products': products
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
