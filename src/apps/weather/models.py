# API KEY dca5866c7ce15e293544c5154fc22dc6
from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True


class City(TimestampedModel):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Cities'


class Forecast(TimestampedModel):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    temperature = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)
    description = models.CharField(max_length=256, blank=True)
    icon = models.CharField(max_length=64, blank=True)

    class TemperatureType(models.IntegerChoices):
        C = 1, "C"
        F = 2, "F"

    type = models.PositiveSmallIntegerField(choices=TemperatureType.choices, default=TemperatureType.C)

    def __str__(self):
        return f"{self.city.name} / {self.temperature}"

    class Meta:
        verbose_name_plural = 'Forecast'

