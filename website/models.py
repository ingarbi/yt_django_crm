from django.db import models


class Record(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    region = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
