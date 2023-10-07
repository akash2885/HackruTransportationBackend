from django.db import models

class Routes(models.Model):
    Olatitude = models.DecimalField(max_digits=100, decimal_places=20)
    Olongitude = models.DecimalField(max_digits=100, decimal_places=20)
    Dlatitude = models.DecimalField(max_digits=100, decimal_places=20)
    Dlongitude = models.DecimalField(max_digits=100, decimal_places=20)
    origin = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.origin + ' - ' + self.destination

