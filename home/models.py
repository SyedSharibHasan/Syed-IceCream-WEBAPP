from django.db import models



class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    country = models.CharField(max_length=12)
    phone = models.CharField(max_length=12)
    subject = models.TextField(max_length=5000)
    date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.country}"







