from django.db import models

# Create your models here.
class Passenger(models.Model):
    id=models.IntegerField(primary_key=True)
    firstName=models.CharField(max_length=50)
    lastName=models.CharField(max_length=50)
    travelPoints=models.IntegerField()

    def __str__(self):
        return self.id+self.firstName+self.lastName+self.travelPoints

