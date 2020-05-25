from django.db import models
import datetime



# Create your models here.

class Cabinet(models.Model):
    #coordinate = models.cooorodinasdadsa
    name_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=datetime.datetime.now())
    image = models.ImageField(upload_to='cabinets', null=True)

    def __str__(self):
        return self.name_text

class Update(models.Model):
    cabinet = models.ForeignKey(Cabinet, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField(default=datetime.datetime.now())
    need_refill = models.BooleanField(default=True)
    image_update = models.ImageField(upload_to='cabinets/uploads', blank=True, null=True)

    def __str__(self):
        return self.comment_text
