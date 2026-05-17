from django.urls import path
from .views import index, contact_form

urlpatterns = [
    # Biri siteye düz girdiğinde senin o turuncu özgeçmiş sayfan açılacak
    path('', index, name='index'),

    # Biri formu doldurup gönderdiğinde bu fonksiyon arka planda çalışacak
    path('contact_form/', contact_form, name='contact_form'),
]