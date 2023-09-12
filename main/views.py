from django.shortcuts import render
from .models import Product

# Create your views here.
def show_main(request):
    
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
    }

    return render(request, "main.html", context)