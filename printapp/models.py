from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    user_type_data = ((1, "Admin"), (2, "Employee"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)


class Admin(models.Model):
    main_id = models.AutoField(primary_key=True)
    user_design = models.OneToOneField(CustomUser, on_delete=models.CASCADE, default=True)
    contact = models.CharField(max_length=15)
    address = models.TextField()
    profile_pic = models.FileField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    objects = models.Manager()


class Employee(models.Model):
    main_id = models.AutoField(primary_key=True)
    user_design = models.OneToOneField(CustomUser, on_delete=models.CASCADE, default=True)
    contact = models.CharField(max_length=15)
    address = models.TextField()
    profile_pic = models.FileField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    objects = models.Manager()


# Getting started with Paper Configuration Helping Hand Models
class PaperType(models.Model):
    main_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=20)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    objects = models.Manager()


class PaperColor(models.Model):
    main_id = models.AutoField(primary_key=True)
    color = models.CharField(max_length=20)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    objects = models.Manager()


class PaperSize(models.Model):
    main_id = models.AutoField(primary_key=True)
    size = models.CharField(max_length=10)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    objects = models.Manager()


class PaperGsm(models.Model):
    main_id = models.AutoField(primary_key=True)
    gsm = models.CharField(max_length=10)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    objects = models.Manager()


# main Paper Configuration Model where inheriting fields from supporting Models.
class PaperConfiguration(models.Model):
    main_id = models.AutoField(primary_key=True)
    paper_name = models.CharField(max_length=20)
    paper_type = models.ForeignKey(PaperType, on_delete=models.CASCADE, default=True)
    paper_color = models.ForeignKey(PaperColor, on_delete=models.CASCADE, default=True)
    paper_gsm = models.ForeignKey(PaperGsm, on_delete=models.CASCADE, default=True)
    paper_per_rim_amount = models.CharField(max_length=6)
    paper_per_sheet_amount = models.FloatField()
    remarks = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    objects = models.Manager()


# Getting started with Plate Configuration Helping Hand Models
class PlateSize(models.Model):
    main_id = models.AutoField(primary_key=True)
    size = models.CharField(max_length=10)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    objects = models.Manager()


# Plate Model
class PlateConfiguration(models.Model):
    main_id = models.AutoField(primary_key=True)
    plate_size = models.ForeignKey(PlateSize, on_delete=models.CASCADE, default=True)
    plate_color = models.CharField(max_length=3)
    cost_of_plate = models.CharField(max_length=6)
    description = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    objects = models.Manager()


# Getting started with Printing Configuration Helping Hand Models
class PrintingSize(models.Model):
    main_id = models.AutoField(primary_key=True)
    size = models.CharField(max_length=10)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    objects = models.Manager()


# Printing Model
class PrintingConfiguration(models.Model):
    main_id = models.AutoField(primary_key=True)
    printing_size = models.ForeignKey(PrintingSize, on_delete=models.CASCADE, default=True)
    first_1000 = models.CharField(max_length=6)
    next_1000 = models.CharField(max_length=6)
    description = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    objects = models.Manager()


# Binding Models
class BindingConfiguration(models.Model):
    main_id = models.AutoField(primary_key=True)
    binding_type = models.CharField(max_length=30)
    binding_size = models.CharField(max_length=6)
    no_of_books = models.CharField(max_length=6)
    rates = models.CharField(max_length=6)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    objects = models.Manager()


# Customer Model
class CustomerConfiguration(models.Model):
    main_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=20)
    customer_contact = models.CharField(max_length=15)
    customer_address = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    objects = models.Manager()


# Job Model
class JobConfiguration(models.Model):
    main_id = models.AutoField(primary_key=True)
    job_name = models.CharField(max_length=20)
    job_description = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    objects = models.Manager()


# Lamination Model
class LaminationConfiguration(models.Model):
    main_id = models.AutoField(primary_key=True)
    lamination_size = models.CharField(max_length=10)
    first_1000 = models.CharField(max_length=10)
    next_1000 = models.CharField(max_length=10)
    description = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    objects = models.Manager()
