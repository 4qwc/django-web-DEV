# django-web-DEV

����� Django

�Դ��� virtualenv
pip install virtualenv
python3 -m pip install virtualenv

��������ҧ environment
virtualenv venv
python3 -m virtualenv venv

Activate
.\venv\scripts\activate  // windows
source ./venv/bin/activate # for mac

�Դ��� django
pip install django==3.2
pip3 install django==3.2

���ҧ��ਤ �djangoschool�
django-admin startproject djangoschool

cd djangoschool ���� �ѹ server ������� localhost:8000
python manage.py runserver

����觷����㹡�����ҧ�ҹ�����Ţͧ admin �����á
python manage.py migrate

--------------------------------
���ҧ user �ͧ admin
python manage.py createsuperuser
*** user: admin
*** password: ���������� ��������

�����ѧ django admin ��ҹ webbrowser
localhost:8000/admin
