from django.urls import path
from authentication.views import login,logout

app_name = 'authentication'

urlpatterns = [
    path('logout/', logout, name='logout'),
    path('login/', login, name='login'),
]

