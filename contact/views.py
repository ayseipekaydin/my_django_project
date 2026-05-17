from django.shortcuts import render, redirect
from .models import ContactMessage


# 1. Senin o dünkü muazzam ana sayfanı ayağa kaldıran fonksiyon
def index(request):
    return render(request, 'index.html')


# 2. En alta eklediğimiz formdan gelen mesajları veritabanına kaydeden motor fonksiyon
def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Verileri veritabanı tablosuna yazıyoruz
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        # Mesaj kaydedilince sayfayı pürüzsüzce ana sayfaya geri atıyoruz
        return redirect('index')

    return redirect('index')