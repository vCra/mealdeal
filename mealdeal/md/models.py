from django.db import models
from django.db.models import Model


class Category(Model):
    name = models.CharField(max_length=256)
    def __str__(self):
        return self.name

class Item(Model):
    title = models.CharField(max_length=512)
    image = models.URLField()
    price = models.DecimalField(decimal_places=2, max_digits=4)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title