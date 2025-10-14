from django.db import models

class Owner(models.Model):
  name = models.CharField(max_length=20)
  balance = models.FloatField()
  def __str__(self):
    return self.name

class Species(models.Model):
  name = models.CharField(max_length=20)
  def __str__(self):
    return self.name

class Pet(models.Model):
  name = models.CharField(max_length=20)
  species = models.ForeignKey(Species, on_delete=models.CASCADE)
  owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
  def __str__(self):
    return self.name
