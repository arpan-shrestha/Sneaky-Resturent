from django.db import models

# Create your models here.
class Offer(models.Model):
    title = models.CharField(max_length=50)
    off = models.CharField(max_length=10)
    image = models.ImageField(upload_to='home/')

    class Meta:
        verbose_name = 'Offer'
        verbose_name_plural = 'Offers'

    def __str__(self):
        return self.title

    