from django.db import models


class Fuel(models.Model):
    distance = models.DecimalField(max_digits=10, decimal_places=2)
    consumption = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.distance
