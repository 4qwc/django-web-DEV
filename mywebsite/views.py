from django.shortcuts import render
from django.http import HttpResponse
from .models import *

from django.contrib.auth import authenticate, login
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from songline import Sendline # ส่งไลน์



# def HomePage(request):
# 	return HttpResponse('<h1>Hello  Welcome MyWebSite</h1>')

def Home(request):
	allproduct = Product.objects.all() # เลือกทั้งหมกใน from Product
	context = {'allproduct':allproduct}
	return render(request, 'company/home.html', context)


def AboutUs(request):
	car = Car.objects.all()
	context = {'car':car}

	now = datetime.now()
	time = now.strftime('%H:%M:%S')
	context['time'] = time
	return render(request, 'company/about.html', context)


def ContactUs(request):
	context = {} # สร้างดิกชันนารี่เก็บข้อมูล]

	if request.method == 'POST':
		data = request.POST.copy()
		title = data.get('title') # ดึงข้อมูลที่เป็น title ออกมา
		email = data.get('email')
		detail = data.get('detail')
		print(title)
		print(email)
		print(detail)
		print('----------------')

		# ถ้าไม่กรอกข้อมูลให้ใส่ if ใน ฟังก์ชั่น 
		if title == '' and email == '':
			context['message'] = 'กรุณากรอกขัอความและอีเมล์ที่ต้องการติอต่อ'
			return render(request, 'company/contact.html', context)
 		
 		# ถ้า return ในนี้ทำงานแล้ว return ด้านล่างจะไม่ทำต่อ


		# เมื่อได้ข้อมูลที่ได้มา ทำการ code บันทึกข้อมูล
		# record_note = Note()
		# record_note.detail = detail
		# record_note.save()


		new_record = ContactList()
		new_record.title = title
		new_record.email = email
		new_record.detail = detail
		new_record.save()

		context['message'] = 'admin ได้รับข้อความแล้ว รอติดต่อกลับภายใน 24 ชั่วโมง'

		# ส่งไลน์
		# token =  'KIkEeNfW20s0geXlrqLYj5N292dHQrkal4ZM6IWo3zI'
		# m = Sendline(token)
		# m.sendtext('หัวข้อที่ติดต่อ:{} \nอีเมล์ติดต่อ:{} \nรายละเอียด: {}'.format(title,email,detail))


	return render(request, 'company/contact.html', context) # แนบ ข้อความใน context



def Login(request):
	context = {}
	if request.method == 'POST':
		data = request.POST.copy()
		username = data.get('username')
		password = data.get('password')

		try:
			user = authenticate(username=username, password=password)
			login(request,user)
		except:
			context['message'] = 'username หรือ password ไม่ถูกต้อง'

	return render(request, 'company/login.html', context)




