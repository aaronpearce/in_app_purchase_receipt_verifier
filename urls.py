from django.conf.urls import include, url
from django.http import HttpResponse

from app import views

urlpatterns = [
    url(r'^sandbox_verify', views.verify_sandbox_receipt),
    url(r'^verify', views.verify_receipt),
    
]

