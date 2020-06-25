from django.db import models

# Create your models here.
class Dataset(models.Model):
    lbp_hist = models.CharField(max_length=255)
    image = models.CharField(max_length=100)
    label = models.CharField(max_length=50)
    directory = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return "{}. {}".format(self.id, self.label)