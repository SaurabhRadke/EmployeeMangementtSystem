from django.db import models
from rest_framework import serializers
class Depart(models.Model):
    Dname=models.CharField(max_length=100)
    Dloc=models.CharField(max_length=100)
    def __str__(self):
        return self.Dname
class Role(models.Model):
    role=models.CharField(max_length=100)
    def __str__(self):
        return self.role
class Employe(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    department=models.ForeignKey(Depart,on_delete=models.CASCADE)
    role=models.ForeignKey(Role,on_delete=models.CASCADE)
    salary=models.IntegerField(default=0)
    DOB=models.DateField()
    Bonus=models.IntegerField(default=0)
    Joining=models.DateTimeField()
    
    def __str__(self):
        return "%s %s"%(self.first_name ,self.last_name)
class EmployeSeri(serializers.ModelSerializer):
    class Meta:
        model=Employe
        fields="__all__"
class DepartSeri(serializers.ModelSerializer):
    emp=EmployeSeri(read_only=True,many=True)
    class Meta:
        model=Depart
        fields="__all__"
class RoleSeri(serializers.ModelSerializer):
    emp=EmployeSeri(read_only=True,many=True)
    class Meta:
        model=Role
        fields="__all__"




# Create your models here.
