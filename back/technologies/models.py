from django.db import models

class Technology(models.Model):
    title = models.CharField(max_length=225, blank=False)
    image = models.ImageField(upload_to='technologies')

    class Meta:
        verbose_name = 'Technology'
        verbose_name_plural = 'Technologies'

    def __str__(self):
        return self.title
