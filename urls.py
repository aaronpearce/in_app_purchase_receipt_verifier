from django.conf.urls import include, url
from django.http import HttpResponse

from app import views

urlpatterns = [
    url(r'^verify_sandbox', views.verify_sandbox_receipt),
    url(r'^verify', views.verify_receipt),
    
]

