from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage, GeneralSetting, ImageSetting, Experience, Education, Skill, SocialMedia


def index(request):
    settings = GeneralSetting.objects.all()

    settings_dict = {}
    for setting in settings:
        settings_dict[setting.name] = setting.parameter

    context = {
        'settings': settings_dict,
        'images': ImageSetting.objects.all(),
        'experiences': Experience.objects.all(),
        'educations': Education.objects.all(),
        'skills': Skill.objects.all(),
        'social_medias': SocialMedia.objects.all(),
    }
    return render(request, 'index.html', context=context)


def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('index')

    return redirect('index')