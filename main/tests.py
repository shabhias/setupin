from django.test import TestCase
from django.test import TestCase, Client
from .models import Product

# Create your tests here.
class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')
    
    def setUp(self):
        self.deskmate = Product.objects.create(
            name='Deskmate',
            amount=10,
            price=150000,
            description='dengan DESKMATE yang sesuai dengan seleramu, membuat kamu nyaman saat nugas di atas meja'
        )
        self.lightbar = Product.objects.create(
            name='Monitor Lightbar',
            amount=20,
            price=200000,
            description='dengan MONITOR LIGHTBAR memberikan estetika pada set up komputer atau laptop di meja Anda'
        )

    def test_deskmate_amount(self):
        self.assertEqual(self.deskmate.amount, 10)

    def test_lightbar_amount(self):
        self.assertEqual(self.lightbar.amount, 20)
        
    