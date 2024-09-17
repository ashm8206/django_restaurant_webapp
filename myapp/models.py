from django.db import models


class DrinksCategory(models.Model):
    category_name = models.CharField(max_length=200)


class Drink(models.Model):
    drink_name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    category_id = models.ForeignKey(
        DrinksCategory, on_delete=models.PROTECT, default=None)


class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    guest_count = models.IntegerField()
    reservation_time = models.DateField()
    comments = models.CharField(max_length=1000, blank=True)


class Employee(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    role = models.CharField(max_length=100)
    shift = models.IntegerField()

    def __str__(self):
        return self.first_name + " " + self.last_name


class Menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.CharField(max_length=1000, default='')

    def __str__(self):
        return self.name
