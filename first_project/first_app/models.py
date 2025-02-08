from django.db import models
from django.core.exceptions import ValidationError


class EmpDetails(models.Model):
    emp_name = models.CharField(max_length=255)
    emp_city = models.CharField(max_length=255)
    emp_company = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.emp_name}    {self.emp_city}    {self.emp_company}"

    class Meta:
        db_table = 'first_app_empdetails'




# Create your models here.
class PersonalData(models.Model):
    person_name= models.CharField(max_length=255)
    person_city= models.CharField(max_length=255)
    person_company= models.CharField(max_length=255)


    class Meta:
        db_table = "PersonalData"

    def __str__(self):
        return f"{self.person_name}"



# many to one
class Album(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)

class Song(models.Model):
    title = models.CharField(max_length=255)
    album = models.ForeignKey(Album,on_delete=models.CASCADE)


# many to many
class Author(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(max_length=300)

class Books(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(max_length=300)
    author= models.ManyToManyField(Author)

#one to one
def validate_val(value):
    if len(value) < 2:
        raise ValidationError(("%(value) should be greater than 2."),
                    params ={"value":value},
                    )


class Vehicle(models.Model):
    reg_no = models.IntegerField()
    owner = models.CharField(max_length=100,validators=[validate_val])


class Car(models.Model):
    vehicle = models.OneToOneField(Vehicle,on_delete=models.CASCADE,primary_key=True)
    car_model = models.CharField(max_length=100)

#
# from django.db import models
#
#
# class EmpDetails(models.Model):
#     name = models.CharField(max_length=100)
#
#     city = models.CharField(max_length=100)
#
#
#     class Meta:
#         db_table='EmpDetails'
