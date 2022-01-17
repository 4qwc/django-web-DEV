from django.urls import path
from .views import * # ฟังก์ชั่น HomePage

urlpatterns = [
    path('', Home, name = 'home'),
    path('about/', AboutUs, name = 'about-page'),
    path('contact/', ContactUs, name='contact-page'),
    path('login/', Login, name='login-page')
    #path('index', index, name="index"),
	#path('<int:year>/<str:month>', views.home, name="home"),
]