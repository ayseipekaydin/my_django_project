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
    # Adamın videoda eklediği detaylı alan özellikleri:
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Name',
        help_text='This is variable'
    )
    description = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Description'
    )
    parameter = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Parameter'
    )
    updated_date = models.DateTimeField(
        blank=True,
        auto_now=True
    )
    created_date = models.DateTimeField(
        blank=True,
        auto_now_add=True
    )

    # Panelde "General Setting: site_title" şeklinde görünmesini sağlayan kısım:
    def __str__(self):
        return f"General Setting: {self.name}"

    # Sıralama ve çoğul isim ayarları:
    class Meta:
        verbose_name = 'General Setting'
        verbose_name_plural = 'General Settings'
        ordering = ('name',)