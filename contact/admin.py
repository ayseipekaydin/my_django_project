from django.contrib import admin
from .models import ContactMessage, GeneralSetting

admin.site.register(ContactMessage)

# Genel ayarlar için arama kutulu ve sütunlu yeni admin yapısı:
@admin.register(GeneralSetting)
class GeneralSettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'parameter', 'updated_date', 'created_date']
    search_fields = ['name', 'description', 'parameter']
    list_editable = ['description', 'parameter']

    class Meta:
        model = GeneralSetting