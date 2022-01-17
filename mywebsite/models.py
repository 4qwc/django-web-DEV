from django.db import models
from django.contrib.auth.models import User # แยก User

# แยก User
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	usertype = models.CharField(max_length=100, default='member')
	point = models.IntegerField(default=0)

	def __str__(self):
		return self.user.username



class Product(models.Model):
	title = models.CharField(max_length=200) #กำหนดตัวหนังสือ200ตัว
	description = models.TextField(null=True, blank=True) #กำหนด ไม่กรอกข้อมูลก็ได้ ใส่ null=True, blank=True
	price = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)  #กำหนดบรรจุได้10ตัว max_digits=10 คือจำนวนตัวเลข/decimal_places=2 คือ ทศนิยม 2 ตำแหน่ง
	quantity = models.IntegerField(default=1,null=True,blank=True)# default=1 ค่าเริ่มต้นมีสินค้า 1
	instock = models.BooleanField(default=True)

	# เพิ่ม ฟังก์ชั่นนี้เพื่อให้ title แสดงผลในหน้าเว็บ
	def __str__(self):
		return self.title


'''
รัน 2 คำสั่งนี้ หากมีการแก้ไข models
python manage.py makemigrations
python manage.py migrate
'''

class Note(models.Model):
	detail = models.TextField(null=True, blank=True)
	def __str__(self):
		return self.detail


# สร้างโมเดล
class ContactList(models.Model):
	title = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	detail = models.TextField(null=True, blank=True)
	complete = models.BooleanField(default=False)


	# เพิ่ม ฟังก์ชั่นนี้เพื่อให้ title แสดงผลในหน้าเว็บ หลังบ้าน
	def __str__(self):
		return self.title # สามารถใส่ + self.email ได้



class Car(models.Model):
	name = models.CharField(max_length=255)
	price = models.DecimalField(max_digits=5, decimal_places=2)
	photo = models.ImageField(upload_to='static/image')
	def __str__(self):
		return self.name
