from django.db import models


class Pic(models.Model):

    Img = models.ImageField(upload_to='images/')

