from django.urls import path,re_path
from . import views

urlpatterns = [
    path("",views.msgproc),
    path("ajax/<str:receiver>",views.msg_ajax),
]