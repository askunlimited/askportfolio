from django.db import models

# Create your models here.

class Tag(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title



class Project(models.Model):
    title = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=False)
    image = models.ImageField(upload_to='projects')
    url = models.URLField(blank=True)
    tag = models.ManyToManyField('Tag', blank=True)
    github_url = models.URLField(blank=True)
    date = models.DateField(blank=False)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.title
