from django.contrib import admin
from .models import MsgBoard
# Register your models here.
"""
注册管理员
python manage.py createsuperuser
"""
admin.site.register(MsgBoard)