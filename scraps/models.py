from django.db import models
from django_mysql.models import ListCharField


class Item(models.Model):
    title = models.CharField(max_length=30)
    links =  ListCharField(
        base_field=models.CharField(max_length=10),
        max_length=(6 * 11)  # 6 * 10 character nominals, plus commas
    )