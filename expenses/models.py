from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from datetime import datetime


class Expenses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    #receiver = models.ForeignKey(Receivers, on_delete=models.PROTECT)
    description = models.TextField(blank=True, null=True)
    date = models.DateTimeField(default=datetime.now)
    payed = models.BooleanField(default=False)
    payment_date = models.DateTimeField(null=True, blank=True)
    slug = models.SlugField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.user} | {self.name}"

    def save(self, *args, **kwargs):
        if not self.id:
            slug = f'{self.user}-{slugify(self.name)}'
            self.slug = slug

        if self.payed == True:
            self.payment_date = models.DateTimeField(default=datetime.now)
        super().save(*args, **kwargs)