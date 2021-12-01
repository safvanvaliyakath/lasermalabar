from django.db import models
from django.urls import reverse

# Create your models here.

class category(models.Model):
    name=models.CharField(max_length=100)
    slug=models.CharField(max_length=100)
    def get_url(self):
        return reverse('product_categ',args=[self.slug])
    def __str__(self):
        return self.name

class products(models.Model):
    title=models.CharField(max_length=100)
    slug=models.CharField(max_length=100)
    categ=models.ForeignKey(category,on_delete=models.CASCADE)
    desc=models.TextField()
    img=models.ImageField(upload_to='images')
    dfile=models.FileField(upload_to='files')
    def __str__(self):
        return self.title