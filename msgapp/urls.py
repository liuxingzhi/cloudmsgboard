from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.msgproc),
    path("ajax/<str:receiver>/unread", views.unread_msg_ajax),
    path("ajax/<str:receiver>/all", views.all_msg_ajax),
]
