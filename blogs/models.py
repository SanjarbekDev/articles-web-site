from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings

# Create your models here.

class Articls(models.Model):
    title = models.CharField(max_length=100)
    contents = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pub_date = models.DateField(auto_now_add=True)
    id = models.AutoField(primary_key=True)

    def get_absolute_url(self):
        return reverse('content_article',kwargs={'id':self.id})



    def __str__(self) -> str:
        return self.title