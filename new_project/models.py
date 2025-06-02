from django.db import models

# Create your models here.

class Word(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    meaning = models.TextField(blank=True, null=True)
    sinonym = models.TextField(blank=True, null=True)
    keywords = models.TextField(blank=True, null=True)
    rus_meaning = models.TextField(blank=True, null=True)
    uzb_latin_meaning = models.TextField(blank=True, null=True)
    uzb_kiril_meaning = models.TextField(blank=True, null=True)
    en_meaning = models.TextField(blank=True, null=True)
    turk_meaning = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Word"
        verbose_name_plural = "Words"
        ordering = ['name']
        db_table = 'words'
