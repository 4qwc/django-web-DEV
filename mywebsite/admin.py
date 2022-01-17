from django.contrib import admin

from .models import * 
# Register your models here.

admin.site.register(Product) # ทำให้เห็นในหน้า admin
admin.site.register(Note)
admin.site.register(ContactList)# เพิ่ม model ใหม่อีกรายการ
admin.site.register(Car)
admin.site.register(Profile)