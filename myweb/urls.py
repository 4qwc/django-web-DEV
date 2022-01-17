from django.contrib import admin
from django.urls import path, include # เพิ่ม include ลิ้งค์ project กับ app

from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('mywebsite.urls')), # ลิ้งค์กับแอพและให้เข้าถึงไฟล์ urls.py ที่สร้างขึ้นมา
    path('login/', views.LoginView.as_view(template_name='company/login.html'),name='login'),
    path('logout/', views.LogoutView.as_view(template_name='company/logout.html'),name='logout'),
]
