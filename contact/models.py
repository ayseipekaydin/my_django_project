from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"


class GeneralSetting(models.Model):
    name = models.CharField(default='', max_length=254, blank=True)
    description = models.CharField(default='', max_length=254, blank=True)
    parameter = models.CharField(default='', max_length=254, blank=True)
    updated_date = models.DateTimeField(blank=True, auto_now=True)
    created_date = models.DateTimeField(blank=True, auto_now_add=True)

    def __str__(self):
        return f"General Setting: {self.name}"

    class Meta:
        verbose_name = 'General Setting'
        verbose_name_plural = 'General Settings'
        ordering = ('name',)


class ImageSetting(models.Model):
    name = models.CharField(default='', max_length=254, blank=True)
    description = models.CharField(default='', max_length=254, blank=True)
    file = models.ImageField(upload_to='img/', blank=True)
    updated_date = models.DateTimeField(blank=True, auto_now=True)
    created_date = models.DateTimeField(blank=True, auto_now_add=True)

    def __str__(self):
        return f"Image Setting: {self.name}"

    class Meta:
        verbose_name = 'Image Setting'
        verbose_name_plural = 'Image Settings'
        ordering = ('name',)


class Experience(models.Model):
    company_name = models.CharField(max_length=254)
    title = models.CharField(max_length=254)
    description = models.TextField(blank=True)
    start_date = models.CharField(max_length=100)
    end_date = models.CharField(max_length=100)
    created_date = models.DateTimeField(blank=True, auto_now_add=True)

    def __str__(self):
        return f"{self.company_name} - {self.title}"

    class Meta:
        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'


class Education(models.Model):
    school_name = models.CharField(max_length=254)
    major = models.CharField(max_length=254)
    description = models.TextField(blank=True)
    start_date = models.CharField(max_length=100)
    end_date = models.CharField(max_length=100)
    created_date = models.DateTimeField(blank=True, auto_now_add=True)

    def __str__(self):
        return f"{self.school_name} - {self.major}"

    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Educations'


class Skill(models.Model):
    name = models.CharField(max_length=100)
    icon_class = models.CharField(max_length=100, blank=True)
    created_date = models.DateTimeField(blank=True, auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'


class SocialMedia(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField()
    icon_class = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Social Media'
        verbose_name_plural = 'Social Medias'