from django.db import models


class StockPrice(models.Model):
    date = models.DateField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    adj_close = models.FloatField()
    volume = models.BigIntegerField()

    def __str__(self):
        return f"{self.date} - Close: {self.close}"


class Annotation(models.Model):
    date = models.DateField()
    note = models.TextField()
    author = models.CharField(max_length=100, default="Anonymous")

    def __str__(self):
        return f"{self.date} - {self.author}: {self.note[:30]}"
