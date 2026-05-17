from django.contrib import admin
from .models import ContactMessage, GeneralSetting

admin.site.register(ContactMessage)
admin.site.register(GeneralSetting)