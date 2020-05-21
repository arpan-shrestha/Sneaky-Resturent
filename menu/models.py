from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=5 , decimal_places=2)
    image = models.ImageField(upload_to='menu/')

    class Meta:
        verbose_name = 'menu'
        verbose_name_plural = 'menus'

    def __str__(self):
        return self.name
    