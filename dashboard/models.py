from django.db import models
from django.contrib.auth.models import User
from django.db.models import F

# Create your models here.

class companies(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock_name = models.CharField(null=True, blank=True, max_length=100)
    industry = models.CharField(null=True, blank=True, max_length=100)
    cmp = models.IntegerField(default=0)
    date = models.CharField(null=True, blank=True, max_length=100)
    eps1 = models.FloatField(null=True, blank=True, default=None)
    eps2 = models.FloatField(null=True, blank=True, default=None)
    eps3 = models.FloatField(null=True, blank=True, default=None)
    eps4 = models.FloatField(null=True, blank=True, default=None)
    eps5 = models.FloatField(null=True, blank=True, default=None)
    eps6 = models.FloatField(null=True, blank=True, default=None)
    eps7 = models.FloatField(null=True, blank=True, default=None)
    eps8 = models.FloatField(null=True, blank=True, default=None)
    eps9 = models.FloatField(null=True, blank=True, default=None)
    cpe = models.FloatField(null=True, blank=True, default=None)
    ipe = models.FloatField(null=True, blank=True, default=None)
    pe1 = models.FloatField(null=True, blank=True, default=None)
    pe2 = models.FloatField(null=True, blank=True, default=None)
    pe3 = models.FloatField(null=True, blank=True, default=None)
    pe4 = models.FloatField(null=True, blank=True, default=None)
    pe5 = models.FloatField(null=True, blank=True, default=None)
    pe6 = models.FloatField(null=True, blank=True, default=None)
    pe7 = models.FloatField(null=True, blank=True, default=None)
    pe8 = models.FloatField(null=True, blank=True, default=None)
    pe9 = models.FloatField(null=True, blank=True, default=None)
    bv = models.FloatField(null=True, blank=True, default=None)
    der = models.FloatField(null=True, blank=True, default=None)
    fcf = models.FloatField(null=True, blank=True, default=None)
    sales = models.FloatField(null=True, blank=True, default=None)
    market_cap = models.FloatField(null=True, blank=True, default=None)

    def __str__(self):
        return self.stock_name

