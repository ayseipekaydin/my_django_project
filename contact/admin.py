from django.contrib import admin
from .models import ContactMessage, GeneralSetting, ImageSetting, Experience, Education, Skill, SocialMedia

admin.site.register(ContactMessage)

@admin.register(GeneralSetting)
class GeneralSettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'parameter', 'updated_date']
    search_fields = ['name', 'description', 'parameter']
    list_editable = ['description', 'parameter']

@admin.register(ImageSetting)
class ImageSettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'file', 'updated_date']
    search_fields = ['name', 'description']
    list_editable = ['description']

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['id', 'company_name', 'title', 'start_date', 'end_date']
    search_fields = ['company_name', 'title']

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['id', 'school_name', 'major', 'start_date', 'end_date']
    search_fields = ['school_name', 'major']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'icon_class']
    search_fields = ['name']

@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'link', 'icon_class']
    search_fields = ['name']