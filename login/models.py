from django.db import models

class customer(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    class Meta:
        db_table: "login_customer"

class admin(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    class Meta:
        db_table: "login_admin"


class deliveryman(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    class Meta:
        db_table: "login_deliveryman"


class location(models.Model):
    loc = models.CharField(max_length=255)

    class Meta:
        db_table: "login_location"

class shop(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    loc = models.ForeignKey(location, on_delete=models.CASCADE)
    class Meta:
        db_table: "login_shop"

